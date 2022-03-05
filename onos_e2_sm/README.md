The aim of this doc is to explain the details of this python package! 

In this package, dataclasses is used along with protobuf (betterproto) to maintain different data fields in an organized manner! 

### used classes: 
  - dataclasses: [tutorial](https://realpython.com/python-data-classes/) 
    - A class making it easier to maintain data in a class! 
  - betterproto: 
    - It provides an improved experience when using Protobuf / gRPC in a modern Python environment! 


## e2sm_kpm
[onos_e2_sm/e2sm_kpm/v1beta1/__init__.py]

Reading data from protobuf, and its maintenance! 
The data includes but not limited to: 
- identifiers! (node, gnb, enb, cu, du, plmn, slice)
- Max number of ProtocolTests, Ricstyles, Qci, QoSflows, SliceItems, ContainerListItems, CellingNbdu, Containers
- ric: StyleType, FormatType
- event definition


## e2sm_kpm_v2
[onos_e2_sm/e2sm_kpm_v2/v2/__init__.py]

Reading data from protobuf, and its maintenance! 
The data includes but not limited to: 
- identifiers (Eutracgi, Nrcgi, CellGlobalId, Snssai)
- Measurements (FiveQi, Qci, Qfi, Arp, GranularityPeriod, MeasurementType(meas_name, meas_id), )
+ those in version 1
