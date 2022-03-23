## 2022-02-17
ORAN E2 Interface Integration
Between Sercomm gNodeB and ONF Near-RT RIC 
[Slides](https://docs.google.com/presentation/d/14QSXzAh3_mQHQtv67yka5-UOanNBmrKA_a4ImGQ-_ck/edit#slide=id.gb78c612887_0_0)

**Release 1.4**
- What's new in the platform
  - (A1t): Policy management interface with non-RT RIC, implementing A1. It's just like onos-e2t supporting 2t nodes
  - Automated Coversion Tool: Converts ASN <-> Protobuf
    - Go APER library => upgraded: not only to connvert service models but also E2-AP
  - onos-config: adding the capability of handling configuration of O1 interface
    - FCAPS interface
    - handles things more than configuration
- What's new in use cases
  - Traffic steering app from RIMEDO lab
    - it receives information from non-rt ric, and makes changes in the ran node
  - Intel connectivity management xApp
  - The relation between UseCase, xApps, service Model, and the undelying hardware can be found on their slides!
- What's new in intfa
  - 5G nodes now support Sercomm alongside Radisys!

**RIMEDO lab traffic steering xApp**


**A1t**
- onos-a1t is the a1 termination point in uONOS
- a proxy of a1 interface messages
  - encode/decode a1 messages
  - forward messages between non-RT RIC (north-bound using rest API) and xApps (south-bound using gRPC)
- a1 supported services [implementation state]
  - policy mngmnt [implenented]
  - a1 enrichment information [NBI -> done, SBI -> partially done, A1-E1 schema => not yet]
  - AI/ML model mngmnt [not yet]


**RAN UL & DL Slicing**
- enabling Ul slicing 
  - its featues is pretty much the same as DL slicing 



## 2022-02-03
[Link](https://drive.google.com/drive/folders/1XkHPClVf9_CR_lh6uvW-ClceqMZ7Mdfv)
- Powder wirelless project -> Univ. of Utah
- RAN Slicing on OSC RIC called NexRAN
  - E2E O-RAN stack to perform resource managment in a sliced RAN environemnt
  - Approach
    - Slices share the same spectrum
    - UEs ar edynamically assigned to a slice
    - Slice resources (RBs) dynamically adjusted
  - Implementation
    - OSC RIC source base - srsRAN enodeB and SRS-RAN
    - O-RAN E2 agent, RAN slicing/scheduling implemented in srsRAN eNodeB
    - O-RAN E2 service model to expose functionality to RIC
    - Custom xApp to control
      - c++
      - uses SC base libs
    - service models
      - KPM
      - NexRAN (I did not see anythin difference)
    - Scehudler
      - just round robin
      - subframe-based, proportional allocation
      - each subframe schedules a sinlge slice
        - other slices' UEs may schedule into unused RBs
      - round-robin across subframes:
        - if slice a has twice priority for slice b, then they assig twice number of subframes to it


## 2022-01-20
POWDER platform!


## 2022-01-06
A1 Termination component


## 2021-11-18
[Link](https://drive.google.com/drive/folders/1-ibo0xxvL_uXRanoXOcCrQEMuOVRu17t)
- Explaining different components of SD-RAN 
- onos-rsm
  - what it offers
  - assumptions:  
    - each CU is connected to one DU
  - How it works and is related to other stuff
  - resource slicing
    - maximum share of resoruces!
  - demo
    - connected to the sd-core
    - two UEs
    - one USRP
    - DU: running on Interl NUC 
    - CU: on another ran
    - DU and CU are connected to the onos-e2t
    - What they demostrate:
      - Slicing is working! when they try different weights, the rate is being affected!
- horizontal scalability


## 2021-09-16
[Link](https://drive.google.com/drive/folders/17lbHGrvP8mvnMJ-WS1FgAA82pRwl9hRN)
- Details of the procedures in RSM service model, exchaning messages, and other stuff!


## 2021-09-02
[Slides](https://docs.google.com/presentation/d/1ET-AElZNFImuUPZOeM_wgDVea-rfELCJ/edit#slide=id.p1)
#### scheduling and slicing detail! 
- Time frame and slice scheduling scheme!
  - in a milisec, a slice can utilize all PRBs available, will be dedicated to one slice in a time frame of 10 milisec
  - therefore, slices are randomized to avoid starvation of resoruces!
  - default slice is scheduled first, before any other slice!
  - it's a FDD solution in LTE

- They calim that this method is more efficient than PRB allocation between slices!
  - pinning slices to PRBs may lead to scenarios of collision and not having a fair share of resoruces
  - Also, some PRBs may not perform well comapred to other PRBs

- But, several consideration exist here
  - latency for the slices that are scheduled late would be a problem!
  - what if a slice do not exhast all the resoruces in one milisec?!
  - what if PRBs be not agnostic to different slices?!

#### demo
- Single carrier over FDD
- Band 7
- 5 MHz SISO - 25 PRBs
- CU on a server
- DU on a NUC

#### Other parameters that can be controlled from RIC
- Link adaptation algoritm specific parameters, independent of scheduler type! [deciding on ue's throughput]
  - CQI_cap: 0-15
  - RI_cap: 1/2
  - Aggregation_Level_cap: 1,2,4,8,16
  - Target_BLER_DL/Target_BLER_UL: 10%
  - Min_MCS/Max_MCS: 0-28
  - Transmission Mode: TM 1,2,3

- HARQ retransmission cap
  - MAX_HARQ_Rext_DL, MAX_HARQ_Rext_UL

- TTI Bundling feature at DU for providing UL Signal robustness, independent of scheduler type!

- Number of Carriers can be allowed

- defining the behaviour of UL power ontrol algorithm at DU, independent of scheduler type!
  - PUSCH_Target_SNR
  - PUCCH_Target_SNR

## 2021-08-19: mobile handover
[Slides](https://docs.google.com/presentation/d/1sSH5fO96I7WuwZXJT2xYt25Fri_-7BFDrNKc7Ns15sw/edit#slide=id.gb78c612887_0_0)

- There are two mechanisms to perform handover!
- Low-level detail on MHO
- Demo of MHO!

### MLB 
- decision of handover is made by CU. RIC and xApps find way to influence to handover happening in the RAN bu changing paramters that are used in A3 events.
- it uses AirHop eSON
- Works with RANSim in “native” mode

### MHO
- CU is not making the decison, but telling the RIC the coinditions in the RAN, and Apps can make decision to force a handover of a particular UE.
- it uses Intel connectivity mngmnt xApp -> inclduing an RL agents to decide about performing handover or not! -> GNN RL! 
- in this case, RIC not only has the cell-level information, but also it has UE-level statistics: UE RRC State, RSRP of the serving cell and neighbor cells, and stuff
- in this case, 
- Works with RANSim in “MHO” mode

## 2021-08-05
- Explaining details of V1.2 software, and hardware support! 
- Changes to different parts of
  - E2T Subsystem
  - Topology Subsystem
  - UE-NIB 
  - MLB

## 2021-07-01
Radisys! 

[Slides](https://drive.google.com/drive/folders/10kDFYO7s30EHcPt31WAhvBGki9yHOI-S)

## 2021-06-03
Radisys! 

[Slides](https://drive.google.com/drive/folders/1LKuTisU08B0ByVhCQo9DDS_ygbjNj_ha)


## 2021-05-20
Intel: Connection Management xAPP | 
[Material](https://drive.google.com/drive/folders/1pRwuALY6ctuyXk8LAPP18P4O2nTOX3B6)


## 2021-05-06
SD-RAN Trial @ DT | 
[Material](https://drive.google.com/drive/folders/1KRAk4vka621WOI17Y-J66UCvJU17v8x7)

## 2021-04-15
RANSim in SD-RAN 1.1

## 2021-03-18
Facebook-Airhop eSON xApp: basics and details

## 2021-03-04
Airhop eSON theory

## 2021-02-18
A1 and O1 interfaces - deep dive into non-RT RIC - ONAP

