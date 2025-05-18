"""Reusable functions and classes for working with TEM Gemini Ontology"""

import pandas as pd

from tripper import EMMO, OWL, RDFS, XSD
from tripper import Literal, Namespace, Triplestore
from tripper.datadoc.dataset import add


MDO = Namespace(
    iri="https://w3id.org/emmo/domain/microstructure#",
    label_annotations=True,
    check=True,
)
DOM = Namespace(
    iri="https://w3id.org/emmo/domain/microscopy#",
    label_annotations=True,
    check=True,
)
MAT = Namespace("https://www.ntnu.edu/temgemini/alloys#")


# Maps column alias to standardised column name
known_columns = {
    "Alloy name": "alloyName",
    "Notes": "notes",
    "Produced by": "producedBy",
    "Production method": "productionMethod",
    "Received (Year/date)": "received",
    "Heat treatment": "heatTreatment",
    "Studied by (name)": "studiedBy",
    "Studied for": "studiedFor",
}

# Cache mapping chemical symbol to IRI of species class
_species_classes = {}


def get_emmo():
    """Returns a Triplestore instance populated with EMMO."""
    if not EMMO._triplestore:
        ts = Triplestore("rdflib")
        ts.parse(str(EMMO))
        EMMO._triplestore = ts
    return EMMO._triplestore


def get_species_classes():
    """Returns dict mapping chemical symbols to species class IRIs."""
    if not _species_classes:
        ts = get_emmo()
        result = ts.query(f"""
            PREFIX rdfs: <{RDFS}>
            PREFIX owl: <{OWL}>
            SELECT ?sym ?iri
            WHERE {{
                ?iri rdfs:subClassOf ?r .
                ?r a owl:Restriction .
                ?r owl:onProperty <{EMMO.hasSymbolValue}> .
                ?r owl:hasValue ?sym .
            }}
        """)
        _species_classes.update(result)
    return _species_classes


def composition_dict(species, value, unit="wt%"):
    """Returns a json-ld dict describing the composition."""
    # Hardcode until EMMO 1.0.2 is released
    hasChemicalSpecies = (
        "https://w3id.org/emmo#EMMO_18fdd2cd_4b0a_43a5_a938_66d8290a066c"
    )

    species_classes = get_species_classes()
    return {
        "@type": EMMO.SingleComponentComposition,
        "hasChemicalSpecies": {
            "@type": species_classes[species],
            "chemicalSymbol": species,
        },
        "hasSIQuantityValue": f"{value} {unit}",
    }


def get_alloy_dicts(filename, alloy_prefix="mat", type=MDO.Alloy, **kw):
    """Load alloys from `filename` and return it as a list of dicts.

    Keyword arguments are passed on to `pd.read_excel()`.
    """
    df = pd.read_excel(filename, **kw)

    alloy_names = [str(s).strip() for s in df["Alloy name"]]

    seen = set()
    duplicates = {x for x in alloy_names if x in seen or seen.add(x)}
    if duplicates:
        s = ', '.join(str(x) for x in duplicates)
        raise ValueError("Duplicated alloy names: {s}")

    prefix = alloy_prefix if ":" in str(alloy_prefix) else f"{alloy_prefix}:"
    species_classes = get_species_classes()

    dicts = []
    for dct in df.to_dict("records"):
        d = {}
        name = str(dct['Alloy name']).strip().replace(" ", "_")
        d["@id"] = f"{prefix}{name}"
        d["@type"] = type
        for k, v in dct.items():
            if pd.isna(v):
                continue
            colname = k.strip()
            value = v.strip() if isinstance(v, str) else v
            if colname in known_columns:
                d[known_columns[colname]] = value
            elif colname in species_classes:
                comp = composition_dict(colname, value, "wt%")
                add(d, "hasSingleComponentComposition", comp)
            else:
                raise ValueError(f"Invalid header name: {k}")
        dicts.append(d)

    return dicts
