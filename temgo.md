<!-- Do not edit! This file is generated with Tripper. -->

Keywords


## Properties on [Resource]
Resource published or curated by an agent.

- subClassOf: [rdfs:Resource]

| Keyword      | Range              | Conformance | Definition                  | Usage note |
| ------------ | ------------------ | ----------- | --------------------------- | ---------- |
| [instrument] | [temgo:Instrument] |             | Reference to the instrument |            |

[instrument]: https://www.ntnu.edu/temgemini/vocab/temgo#instrument
[temgo:Instrument]: https://www.ntnu.edu/temgemini/vocab/temgo#Instrument




## Properties on [EMMO_90ae56e4_d197_49b6_be1a_0049e4756606]

| Keyword          | Range                                            | Conformance | Definition                                                   | Usage note |
| ---------------- | ------------------------------------------------ | ----------- | ------------------------------------------------------------ | ---------- |
| [dateOfReceival] | [rdfs:Literal]<br>(xsd:date)                     |             | The date an object is received.                              |            |
| [studiedBy]      | [emmo:EMMO_2480b72b_db8d_460f_9a5f_c2912f979046] |             | The Agent who studied the documented object.                 |            |
| [studiedFor]     | [rdfs:Literal]<br>(xsd:string)                   |             | Description about what the documented object is studied for. |            |

[dateOfReceival]: https://www.ntnu.edu/temgemini/vocab/temgo#dateOfReceival
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[studiedBy]: https://www.ntnu.edu/temgemini/vocab/temgo#studiedBy
[emmo:EMMO_2480b72b_db8d_460f_9a5f_c2912f979046]: https://w3id.org/emmo#EMMO_2480b72b_db8d_460f_9a5f_c2912f979046
[studiedFor]: https://www.ntnu.edu/temgemini/vocab/temgo#studiedFor
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal




## Properties on [Property]

| Keyword            | Range                                                | Conformance | Definition                                                                             | Usage note |
| ------------------ | ---------------------------------------------------- | ----------- | -------------------------------------------------------------------------------------- | ---------- |
| [relatedTechnique] | [rdfs:Literal]<br>(chameo:CharacterisationTechnique) |             | Relates a property to a characterisation technique that this property is relevant for. |            |

[relatedTechnique]: https://www.ntnu.edu/temgemini/vocab/temgo#relatedTechnique
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal




## Properties on [Instrument]
Device used for making measurements, alone or in conjunction with one or more supplementary devices.

- subClassOf: [chameo:CharacterisationMeasurementInstrument]

| Keyword                     | Range                           | Conformance | Definition                                                                                                                                                                                                                                                                  | Usage note |
| --------------------------- | ------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [accelerationVoltage]       | [rdfs:Literal]<br>(xsd:double)  |             | Electron acceleration voltage                                                                                                                                                                                                                                               |            |
| [apertureDiameterObjective] | [rdfs:Literal]<br>(xsd:double)  |             | Diameter of objective aperture                                                                                                                                                                                                                                              |            |
| [beamCurrent]               | [rdfs:Literal]<br>(xsd:double)  |             | Current of the electron beam                                                                                                                                                                                                                                                |            |
| [detectorMode]              | [rdfs:Literal]<br>(xsd:string)  |             | Detecor's mode, e.g., SE                                                                                                                                                                                                                                                    |            |
| [detectorName]              | [rdfs:Literal]<br>(xsd:string)  |             | Detecor's name, e.g., ETD                                                                                                                                                                                                                                                   |            |
| [dwellTime]                 | [rdfs:Literal]<br>(xsd:double)  |             | Beam dwell time on each pixel during scan.                                                                                                                                                                                                                                  |            |
| [electronSource]            | [rdfs:Literal]<br>(xsd:string)  |             | Electron source, e.g., FEG                                                                                                                                                                                                                                                  |            |
| [lineIntegration]           | [rdfs:Literal]<br>(xsd:integer) |             | Number of times each line was scanned for intensity integration.                                                                                                                                                                                                            |            |
| [magnification]             | [rdfs:Literal]<br>(xsd:double)  |             | Magnification                                                                                                                                                                                                                                                               |            |
| [sampleHolder]              | [temgo:SampleHolder]            |             | Reference to sample holder.                                                                                                                                                                                                                                                 |            |
| [PositionX]                 | [rdfs:Literal]<br>(xsd:double)  |             | X position of the stage/specimen relative to origin                                                                                                                                                                                                                         |            |
| [PositionY]                 | [rdfs:Literal]<br>(xsd:double)  |             | Y position of the stage/specimen relative to origin                                                                                                                                                                                                                         |            |
| [PositionZ]                 | [rdfs:Literal]<br>(xsd:double)  |             | Z position of the stage/specimen relative to origin                                                                                                                                                                                                                         |            |
| [stageRotation]             | [rdfs:Literal]<br>(xsd:double)  |             | In-plane rotation of the SEM sample stage about the beam relative to the chamber X-axis. Positive rotation is clockwise.                                                                                                                                                    |            |
| [stageRotationMax]          | [rdfs:Literal]<br>(xsd:double)  |             | Maximum in-plane rotation of the SEM sample stage about the beam relative to the chamber X-axis. Positive rotation is clockwise.                                                                                                                                            |            |
| [stageRotationMin]          | [rdfs:Literal]<br>(xsd:double)  |             | Minimum in-plane rotation of the SEM sample stage about the beam relative to the chamber X-axis. Positive rotation is clockwise.                                                                                                                                            |            |
| [TiltX]                     | [rdfs:Literal]<br>(xsd:double)  |             | Tilt of the stage (SEM) or specimen holder (TEM) about the X-axis. For SEM, the X-axis is defined in the chamber coordinate system (left-right). For TEM, this corresponds to ?-tilt (perpendicular to the holder's longitudinal axis). Positive tilt is clockwise.         |            |
| [TiltXMax]                  | [rdfs:Literal]<br>(xsd:double)  |             | Maximum tilt of the stage (SEM) or specimen holder (TEM) about the X-axis. For SEM, the X-axis is defined in the chamber coordinate system (left-right). For TEM, this corresponds to ?-tilt (perpendicular to the holder's longitudinal axis). Positive tilt is clockwise. |            |
| [TiltXMin]                  | [rdfs:Literal]<br>(xsd:double)  |             | Minimum tilt of the stage (SEM) or specimen holder (TEM) about the X-axis. For SEM, the X-axis is defined in the chamber coordinate system (left-right). For TEM, this corresponds to ?-tilt (perpendicular to the holder's longitudinal axis). Positive tilt is clockwise. |            |
| [TiltY]                     | [rdfs:Literal]<br>(xsd:double)  |             | Tilt of the TEM specimen holder about the ? axis (orthogonal to ? axis). Positive tilt is clockwise.                                                                                                                                                                        |            |
| [TiltYMax]                  | [rdfs:Literal]<br>(xsd:double)  |             | Maximum tilt of the TEM specimen holder about the ? axis (orthogonal to ? axis). Positive tilt is clockwise.                                                                                                                                                                |            |
| [TiltYMin]                  | [rdfs:Literal]<br>(xsd:double)  |             | Minimum tilt of the TEM specimen holder about the ? axis (orthogonal to ? axis). Positive tilt is clockwise.                                                                                                                                                                |            |
| [workingDistance]           | [rdfs:Literal]<br>(xsd:double)  |             | Distance between the sample and the electron polepiece.                                                                                                                                                                                                                     |            |

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
[PositionX]: https://www.ntnu.edu/temgemini/vocab/temgo#stagePositionX
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[PositionY]: https://www.ntnu.edu/temgemini/vocab/temgo#stagePositionY
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[PositionZ]: https://www.ntnu.edu/temgemini/vocab/temgo#stagePositionZ
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[stageRotation]: https://www.ntnu.edu/temgemini/vocab/temgo#stageRotation
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[stageRotationMax]: https://www.ntnu.edu/temgemini/vocab/temgo#stageRotationMax
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[stageRotationMin]: https://www.ntnu.edu/temgemini/vocab/temgo#stageRotationMin
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[TiltX]: https://www.ntnu.edu/temgemini/vocab/temgo#stageTiltX
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[TiltXMax]: https://www.ntnu.edu/temgemini/vocab/temgo#stageTiltXMax
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[TiltXMin]: https://www.ntnu.edu/temgemini/vocab/temgo#stageTiltXMin
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[TiltY]: https://www.ntnu.edu/temgemini/vocab/temgo#stageTiltY
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[TiltYMax]: https://www.ntnu.edu/temgemini/vocab/temgo#stageTiltYMax
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[TiltYMin]: https://www.ntnu.edu/temgemini/vocab/temgo#stageTiltYMin
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal
[workingDistance]: https://www.ntnu.edu/temgemini/vocab/temgo#workingDistance
[rdfs:Literal]: http://www.w3.org/2000/01/rdf-schema#Literal






[rdfs:Resource]: http://www.w3.org/2000/01/rdf-schema#Resource
[Resource]: http://www.w3.org/ns/dcat#Resource
[EMMO_90ae56e4_d197_49b6_be1a_0049e4756606]: https://w3id.org/emmo#EMMO_90ae56e4_d197_49b6_be1a_0049e4756606
[Property]: http://www.w3.org/1999/02/22-rdf-syntax-ns#Property
[chameo:CharacterisationMeasurementInstrument]: https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationMeasurementInstrument
[Instrument]: https://www.ntnu.edu/temgemini/vocab/temgo#Instrument
[@id]: https://www.w3.org/TR/json-ld11/#syntax-tokens-and-keywords
[@type]: https://www.w3.org/TR/json-ld11/#syntax-tokens-and-keywords
[@context]: https://www.w3.org/TR/json-ld11/#syntax-tokens-and-keywords
[@base]: https://www.w3.org/TR/json-ld11/#syntax-tokens-and-keywords
[@vocab]: https://www.w3.org/TR/json-ld11/#syntax-tokens-and-keywords
[@graph]: https://www.w3.org/TR/json-ld11/#syntax-tokens-and-keywords
