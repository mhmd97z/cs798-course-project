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
