<!-- Do not edit! This file is generated with Tripper. -->

Keywords


## Properties on [Resource]

| Keyword      | Range              | Conformance | Definition | Usage note |
| ------------ | ------------------ | ----------- | ---------- | ---------- |
| [instrument] | [temgo:Instrument] |             |            |            |

[instrument]: https://www.ntnu.edu/temgemini/vocab/temgo#instrument
[temgo:Instrument]: https://www.ntnu.edu/temgemini/vocab/temgo#Instrument




## Properties on [SingleComponentComposition]
The fraction or amount of a single constituent of a substance.

| Keyword              | Range                                                              | Conformance | Definition                                                                                                                    | Usage note |
| -------------------- | ------------------------------------------------------------------ | ----------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [hasChemicalSpecies] | [emmo:EMMO_cbcf8fe6_6da6_49e0_ab4d_00f737ea9689]                   |             | A symbolic construct that stands for a chemical species.                                                                      |            |
| [hasSIQuantityValue] | [rdfs:Literal]<br>(emmo:EMMO_799c067b_083f_4365_9452_1f1433b03676) |             | Relates a physical quantity to its value specified as a string consisting of a numerical, a separator and a unit. Ex: '3 cm'. |            |
| [chemicalSymbol]     | [rdfs:Literal]<br>(xsd:string)                                     |             | Chemical symbol.                                                                                                              |            |

[hasChemicalSpecies]: https://w3id.org/emmo#EMMO_18fdd2cd_4b0a_43a5_a938_66d8290a066c
[emmo:EMMO_cbcf8fe6_6da6_49e0_ab4d_00f737ea9689]: https://w3id.org/emmo#EMMO_cbcf8fe6_6da6_49e0_ab4d_00f737ea9689
[hasSIQuantityValue]: https://w3id.org/emmo#EMMO_42806efc_581b_4ff8_81b0_b4d62153458b
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[chemicalSymbol]: https://www.ntnu.edu/temgemini/vocab/temgo#chemicalSymbol
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal




## Properties on [EMMO_90ae56e4_d197_49b6_be1a_0049e4756606]

| Keyword             | Range                            | Conformance | Definition | Usage note |
| ------------------- | -------------------------------- | ----------- | ---------- | ---------- |
| [hasDateOfReceival] | [rdfs:Literal]<br>(xsd:dateTime) |             |            |            |

[hasDateOfReceival]: https://www.ntnu.edu/temgemini/vocab/temgo#hasDateOfReceival
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal




## Properties on [Alloy]
Mixture with metallic character composed of two or more elements of which at least one is a metal.

| Keyword                         | Range                                            | Conformance | Definition                                                   | Usage note |
| ------------------------------- | ------------------------------------------------ | ----------- | ------------------------------------------------------------ | ---------- |
| [alloyName]                     | [emmo:EMMO_4207e895_8b83_4318_996a_72cfb32acd94] |             | Identifier of the material.                                  |            |
| [productionMethod]              | [emmo:EMMO_a4d66059_5dd3_4b90_b4cb_10960559441b] |             | The production method manufacturing method                   |            |
| [hasSingleComponentComposition] | [emmo:EMMO_172e2c96_180b_40f8_a3e7_b624471f40c2] |             | Relates an alloy to the amount of one of its elements.       |            |
| [producedBy]                    | [emmo:EMMO_c0afb341_7d31_4883_a307_ae4606df2a1b] |             | The manufacturer of the alloy.                               |            |
| [heatTreatment]                 | [rdfs:Literal]<br>(xsd:string)                   |             | A label for the heat treatment process.                      |            |
| [notes]                         | [rdfs:Literal]<br>(rdf:langString)               |             | A general note, for any purpose.                             |            |
| [received]                      | [rdfs:Literal]                                   |             | The data an object is received.                              |            |
| [studiedBy]                     | [rdfs:Literal]<br>(xsd:string)                   |             | Name of person who studied the documented object.            |            |
| [studiedFor]                    | [rdfs:Literal]<br>(xsd:string)                   |             | Description about what the documented object is studied for. |            |

[alloyName]: http://purl.org/dc/terms/identifier
[emmo:EMMO_4207e895_8b83_4318_996a_72cfb32acd94]: https://w3id.org/emmo#EMMO_4207e895_8b83_4318_996a_72cfb32acd94
[productionMethod]: https://w3id.org/emmo#EMMO_0e86a108_9d4d_4582_8126_f0c527d81901
[emmo:EMMO_a4d66059_5dd3_4b90_b4cb_10960559441b]: https://w3id.org/emmo#EMMO_a4d66059_5dd3_4b90_b4cb_10960559441b
[hasSingleComponentComposition]: https://w3id.org/emmo#EMMO_51f426a6_af4a_4e91_a392_2b0bb635e2d5
[emmo:EMMO_172e2c96_180b_40f8_a3e7_b624471f40c2]: https://w3id.org/emmo#EMMO_172e2c96_180b_40f8_a3e7_b624471f40c2
[producedBy]: https://w3id.org/emmo#EMMO_89c5fd4c_c7b5_4fde_bca8_7734cbda777a
[emmo:EMMO_c0afb341_7d31_4883_a307_ae4606df2a1b]: https://w3id.org/emmo#EMMO_c0afb341_7d31_4883_a307_ae4606df2a1b
[heatTreatment]: https://w3id.org/emmo/domain/microstructure#hasHeatTreatmentLabel
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[notes]: http://www.w3.org/2004/02/skos/core#note
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[received]: https://www.ntnu.edu/temgemini/vocab/temgo#dataOfReceival
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[studiedBy]: https://www.ntnu.edu/temgemini/vocab/temgo#studiedBy
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[studiedFor]: https://www.ntnu.edu/temgemini/vocab/temgo#studiedFor
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal




## Properties on [Property]
The class of RDF properties.

| Keyword            | Range                                                | Conformance | Definition | Usage note |
| ------------------ | ---------------------------------------------------- | ----------- | ---------- | ---------- |
| [relatedTechnique] | [rdfs:Literal]<br>(chameo:CharacterisationTechnique) |             |            |            |

[relatedTechnique]: https://www.ntnu.edu/temgemini/vocab/temgo#relatedTechnique
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal




## Properties on [Instrument]

- subClassOf: [chameo:CharacterisationMeasurementInstrument]

| Keyword                     | Range                           | Conformance | Definition | Usage note |
| --------------------------- | ------------------------------- | ----------- | ---------- | ---------- |
| [accelerationVoltage]       | [rdfs:Literal]<br>(xsd:double)  |             |            |            |
| [apertureDiameterObjective] | [rdfs:Literal]<br>(xsd:double)  |             |            |            |
| [beamCurrent]               | [rdfs:Literal]<br>(xsd:double)  |             |            |            |
| [detectorMode]              | [rdfs:Literal]<br>(xsd:string)  |             |            |            |
| [detectorName]              | [rdfs:Literal]<br>(xsd:string)  |             |            |            |
| [dwellTime]                 | [rdfs:Literal]<br>(xsd:double)  |             |            |            |
| [electronSource]            | [rdfs:Literal]<br>(xsd:string)  |             |            |            |
| [lineIntegration]           | [rdfs:Literal]<br>(xsd:integer) |             |            |            |
| [magnification]             | [rdfs:Literal]<br>(xsd:double)  |             |            |            |
| [sampleHolder]              | [temgo:SampleHolder]            |             |            |            |
| [stagePositionX]            | [rdfs:Literal]<br>(xsd:double)  |             |            |            |
| [stagePositionY]            | [rdfs:Literal]<br>(xsd:double)  |             |            |            |
| [stagePositionZ]            | [rdfs:Literal]<br>(xsd:double)  |             |            |            |
| [stageRotation]             | [rdfs:Literal]<br>(xsd:double)  |             |            |            |
| [stageTiltX]                | [rdfs:Literal]<br>(xsd:double)  |             |            |            |
| [stageTiltY]                | [rdfs:Literal]<br>(xsd:double)  |             |            |            |
| [workingDistance]           | [rdfs:Literal]<br>(xsd:double)  |             |            |            |

[accelerationVoltage]: https://www.ntnu.edu/temgemini/vocab/temgo#accelerationVoltage
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[apertureDiameterObjective]: https://www.ntnu.edu/temgemini/vocab/temgo#apertureDiameterObjective
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[beamCurrent]: https://www.ntnu.edu/temgemini/vocab/temgo#beamCurrent
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[detectorMode]: https://www.ntnu.edu/temgemini/vocab/temgo#detectorMode
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[detectorName]: https://www.ntnu.edu/temgemini/vocab/temgo#detectorName
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[dwellTime]: https://www.ntnu.edu/temgemini/vocab/temgo#dwellTime
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[electronSource]: https://www.ntnu.edu/temgemini/vocab/temgo#electronSource
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[lineIntegration]: https://www.ntnu.edu/temgemini/vocab/temgo#lineIntegration
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[magnification]: https://www.ntnu.edu/temgemini/vocab/temgo#magnification
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[sampleHolder]: https://www.ntnu.edu/temgemini/vocab/temgo#sampleHolder
[temgo:SampleHolder]: https://www.ntnu.edu/temgemini/vocab/temgo#SampleHolder
[stagePositionX]: https://www.ntnu.edu/temgemini/vocab/temgo#stagePositionX
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[stagePositionY]: https://www.ntnu.edu/temgemini/vocab/temgo#stagePositionY
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[stagePositionZ]: https://www.ntnu.edu/temgemini/vocab/temgo#stagePositionZ
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[stageRotation]: https://www.ntnu.edu/temgemini/vocab/temgo#stageRotation
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[stageTiltX]: https://www.ntnu.edu/temgemini/vocab/temgo#stageTiltX
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[stageTiltY]: https://www.ntnu.edu/temgemini/vocab/temgo#stageTiltY
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[workingDistance]: https://www.ntnu.edu/temgemini/vocab/temgo#workingDistance
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal






[Resource]: http://www.w3.org/ns/dcat#Resource
[SingleComponentComposition]: https://w3id.org/emmo#EMMO_172e2c96_180b_40f8_a3e7_b624471f40c2
[EMMO_90ae56e4_d197_49b6_be1a_0049e4756606]: https://w3id.org/emmo#EMMO_90ae56e4_d197_49b6_be1a_0049e4756606
[Alloy]: https://w3id.org/emmo/domain/microstructure#EMMO_e25884df-decb-52e1-b8c0-f5092dd40066
[Property]: http://www.w3.org/1999/02/22-rdf-syntax-ns#Property
[chameo:CharacterisationMeasurementInstrument]: https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationMeasurementInstrument
[Instrument]: https://www.ntnu.edu/temgemini/vocab/temgo#Instrument
[@id]: https://www.w3.org/TR/json-ld11/#syntax-tokens-and-keywords
[@type]: https://www.w3.org/TR/json-ld11/#syntax-tokens-and-keywords
[@context]: https://www.w3.org/TR/json-ld11/#syntax-tokens-and-keywords
[@base]: https://www.w3.org/TR/json-ld11/#syntax-tokens-and-keywords
[@vocab]: https://www.w3.org/TR/json-ld11/#syntax-tokens-and-keywords
[@graph]: https://www.w3.org/TR/json-ld11/#syntax-tokens-and-keywords
