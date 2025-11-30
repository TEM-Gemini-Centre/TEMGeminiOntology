# TEM Gemini Ontology (TEMGO)
An EMMO-based application-level ontology that defines standardised TEM and SEM characterisation procedures, workflows, instruments and tools used within the TEM Gemini Centre.

The ontology is available from this IRI: https://tem-gemini-centre.github.io/TEMGeminiOntology/temgo.ttl


## Resources
* [List of concepts] in TEMGO.
* [Reference documentation] for ontology experts.
* [Asserted ontology]
* [Inferred ontology] (using the HermiT reasoner).


### Imported ontologies
Version dependencies on imported ontologies:

| Version | [EMMO] | [CHAMEO] | [MDO] | [DOM] |
|---------|--------|----------|-------|-------|
| 0.0.1   | 1.0.0  | 1.0.0    | 0.3.1 | 0.0.1 |
| 0.1.0   | 1.0.0  | 1.0.0    | 0.3.1 | 0.0.1 |



## Python integration
TEMGO is an application ontology. But it includes a json-ld context and a keywords file that can be made available to python applications by installing TEMGO as a Python package:

    pip install git+https://github.com/TEM-Gemini-Centre/TEMGeminiOntology.git@master


### Developers
As a developer, may want to install [pre-commit] to automatically synchronise the json-ld context and documentation to the ontology expressed in the turtle files.

    pip install pre-commit
    pre-commit intstall




## License
This ontology is released under the [Creative Commons Attribution 4.0
International](https://creativecommons.org/licenses/by/4.0/legalcode)
license (CC BY 4.0).


### Acknowledgment
This work has been supported by the following projects:
  - [TEM Gemini Centre](https://www.ntnu.edu/temgemini/) is the Trondheim node of [NORTEM](https://nortem.no/) that is funded by the Research Council of Norway.
  - [SFI PhysMet](https://www.ntnu.edu/physmet/) (2020-2028) that receives funding from the Research Council of Norway, project no. 309584.
  - [MatCHMaker](https://he-matchmaker.eu/) (2023-2027) that receives funding from the European Unio's Horizon Europe Research and Innovation Programme, under Grant Agreement n. 101091687.



[EMMO]: https://github.com/emmo-repo/EMMO
[CHAMEO]: https://github.com/emmo-repo/domain-characterisation-methodology
[DOM]: https://github.com/emmo-repo/domain-microscopy
[MDO]: https://github.com/emmo-repo/domain-microstructure

[List of concepts]: https://github.com/TEM-Gemini-Centre/TEMGeminiOntology/blob/gh-pages/temgo.md
[Reference documentation]: https://tem-gemini-centre.github.io/TEMGeminiOntology/widoco/index-en.html
[Asserted ontology]: https://tem-gemini-centre.github.io/TEMGeminiOntology/temgo.ttl
[Inferred ontology]: https://tem-gemini-centre.github.io/TEMGeminiOntology/temgo-inferred.ttl
