## uONOS

## Basics
- ONOS RIC consists of multiple micro-services, each is deployed as a Kubernetes pod, and communication between micro-services are mainly done through gRPC.
- The majority of the micro-services are implemented in GO, with the E2 interface decoding and encoding implemented in C.


### Architecture
- **onos-e2t**
  - **onos-e2t** micro-service is the one that actually connects E2 nodes with xApps. This micro-service terminates E2 interfaces, manages subscriptions, and hosts xApps.
  - In the implementation of ONOS RIC, communication between **onos-e2t** and xApps are done through Protobuf messages, instead of E2 messages (which are in ASN.1 syntax).
  - **onos-e2t** micro-service is also responsible for maintaining topology of all E2 nodes connected and storing a list of RAN functions supported by each E2 node using information gathered from setup stage and service update requests. This micro-service stores information using APIs exposed by **onos-topo** and **onos-uenib**.
  - Get:
    - subscriptions
      - Service Model ID -> oran-e2sm-mho:v2, oran-e2sm-kpm:v2
      - E2 NodeID -> Entity id: e2:1/5154, e2:1/5153
      - State -> SUBSCRIPTION_COMPLETE
- **onos-e2-sm**
  - Service models are implemented in **onos-e2-sm**. It is a shared library that contains all supported service models and mapping between the ASN.1 definition (for E2 messages) and protobuf definition (for xApps) of the service models. By using a separate library, ONOS RIC decouples service model with the remaining system, making ONOS RIC capable of handling any E2SM.
- **onos-topo**
  - ONOS RIC uses **onos-topo** as a R-NIB storage. Specifically, information regarding E2 nodes and their relationship, information regarding cells and slicing are stored using **onos-topo** to manage and provide a shared view of the overall RAN system.
  - Get:
    - NaN
  - Set (+Get) 
    - entity
      - Entity ID
      - Kind ID -> e2cell, e2t, a1t, e2node, onos-config
      - Labels 
      - Aspects -> onos.topo.E2Cell, onos.topo.E2TInfo,onos.topo.Lease, onos.topo.A1TInfo, onos.topo.MastershipState,onos.topo.E2Node, onos.topo.Lease
    - kind 
      - Kind ID -> e2t, e2cell, e2node, neighbors, controls, contains, 
      - Name
      - Labels
      - Aspects 
    - relation
      - Relation ID
      - Kind ID -> contains [e2node controls e2cell], controls [e2t controls e2node]
      - Source ID -> Entity ID 
      - Target ID -> Entity ID 
      - Labels 
      - Aspects 
    - wipeout: Delete All Relations and Entities
- **onos-uenib**
  - UE-related information is stored using APIs provided by **onos-uenib**, a new micro-service designed specifically to store and track UE information with minimum latency and high throughput rate.
  - Get:
    - NaN 
  - Set (+Get):
    - ue information 
      - UE ID 
      - Aspect Types -> RRCState, RSRP-Neighbors, RSRP-Serving, CGI, 5QI [how can I get the values of these fields?]


### Supported Service Models 
Currently, all E2SMs and xApps supported by ONOS RIC are implemented in GO, however, a Python SDK is now in the beta stage and we could see xApps implemented in Python coming in the future. 
- KPM: allows gathering metric data from E2 nodes
- NI: currently, only the protobuf definition of this service model has been implemented
  - No xApps that run over this service model is provided by SD-RAN project.
- RC: [RAN Control] This service model allows RIC to gather cells (PCI) and neighbor relationship.  
- MHO: [Mobile Handover] This service model handles all mobile handover procedure-related operations. This service model allows collection of signal metric data for UEs and RRC state change data. It also allows control signalling for initiating mobile handover procedures.
- RSM: [RAN Slicing Management] This service model allows creating, updating and deleting RAN slices


### xApps
- **onos-kpimon** xApp runs over KPM service model to collect metric data. 
  - Get:
    - Node ID
    - Cell Object ID
    - Cell Global ID
    - Time
    - RRC.Conn.{Avg & Max}
    - RRC.ConnEstabAtt.Sum
    - RRC.ConnEstabSucc.Sum
    - RRC.ConnReEstabAtt.{HOFail & Other & Sum & reconfigFail}
  - Set (+Get): 
    - 
- **onos-pci** xApp demonstrates RC service model. It allows the collection of data related to PCI and PCI conflicts. This xApp is also capable of detecting and resolving PCI conflicts using built-in algorithms.
  - [ERROR] rpc error: code = Unknown desc = no measurements entries stored
  - Get: 
    - 
  - Set (+Get): 
    - 
- **onos-mho** xApp runs over MHO service model.
  - Get:
    - cells
      - CGI
      - Num UEs
      - Handovers-in
      - Handovers-out
    - UEs
      - UeID
      - CellGlobalID
      - RrcState -> CONNECTED, IDLE
  - Set (+Get): 
    - NaN 
- **onos-rsm** xApp runs over RSM service model. 
  - This app allows creating, updating and deleting RAN slices through a command-line interface. User is also capable of specifying a UE to a slice through the command line. 
  - This xApp would also store and update the topology and UE properties related to RAN slicing operations using **onos-topo** and **onos-uenib** accordingly.
  - Get:
    - NaN
  - Set (+Get): 
    - creat slice
      - SCHEDULER_TYPE
      - SLICE_TYPE
      - WEIGHT
- **onos-mlb** xApp balances load among connected cells.
  - The application adjusts neighbor cells’ cell individual offset (Ocn). If a cell becomes overloaded, this application tries to offload the cell’s load to the neighbor cells that have enough capacity. Adjusting neighbor cells’ Ocn triggers measurement events; it triggers handover events from a cell to it’s neighbor cells. As a result, by adjusting Ocn, the load of overloaded cell will be offloaded to the neighbor cells.
  - Get:
    - ocn 
      - sCell
      - node ID
      - sCell PLMN ID
      - sCell cell ID
      - sCell object ID
      - nCell PLMN ID
      - nCell cell ID
      - Ocn [dB]
  - Set (+Get): 
    - parameters
      - interval [sec]
      - Delta Ocn per step
      - Overload threshold [%]
      - Target threshold [%]

## Detailed CLI
### onos-kpimon
- [docLink](https://docs.sd-ran.org/master/onos-kpimon/README.html) | [gitRepo](https://github.com/onosproject/onos-kpimon) | [dockerImage](https://hub.docker.com/r/onosproject/onos-kpimon)
- **onos-kpimon** makes a subscription with E2 nodes connected to **onos-e2t** through **onos-topo** based ONOS xApplication SDK. Creating a subscription, **onos-kpimon** sets **report interval** and **granularity period** which are the monitoring interval parameters.
- Noticeable stuff:
  - **report interval** and **granularity period** are set to 1000 ms. I'm not sure what is the possbile minimum value.
  

### onos-mho
- [docLink](https://docs.sd-ran.org/master/onos-mho/README.html) | [gitRepo](https://github.com/onosproject/onos-mho) | [dockerImage] (https://hub.docker.com/r/onosproject/onos-mho)
- It's a sample xApplication that implements a simple A3 [an interface b/w BSs] event based handover function to demonstrate the mobility management capabilities of µONOS RIC platform.
- The **onos-mho** xApp interfaces with µONOS RIC, using the Golang SDK, to subscribe for A3 measurement reports from E2 nodes that support the E2SM-MHO service model. In addition to the A3 Events, **onos-mho** can be configured to subscribe to RRC state changes and periodic UE measurement reports as well. **onos-mho** processes the measurement event based on its configured A3 Event parameters. If a handover decision is made, **onos-mho** sends a handover control message to the E2 node to trigger a handover. In addition, onos-mho also updates UE-NIB with UE related information such as RRC state, signal strengths for serving and neighbor cells.
- The E2SM-MHO service model is currently only supported by RANSim and not by real CU/DU/gNB. 
- The generic model.yaml model, which simulates UEs moving on randomly generated routes, can be used with **onos-mho** to test handovers. Alternatively, the two-cell-two-node-model.yaml model can be used to test **onos-mho** handover functionality in a more controlled and deterministic manner


### onos-rsm
- [docLink](https://docs.sd-ran.org/master/onos-rsm/README.html) | [gitRepo](https://github.com/onosproject/onos-rsm) | [dockerImage] (https://hub.docker.com/r/onosproject/onos-rsm)
- With the purpose of ran slice management. The RAN slice has definitions related with Quality of Service (QoS) for associated UEs, such as time frame rates and scheduling algorithms.
- In order to manage the RAN slice, this xApplication creates, deletes, and updates RAN slices through CLI. Also, this xApplication associates a specific UE to a RAN slice so that the UE can achieve the QoS that is defined in the associated RAN slice.
- It subscribes to CU and DU through **onos-e2t**. CU nodes report the EPC Mobility Management (EMM) event while DU nodes receive control messages for RAN slice management and UE-slice association.
- The **onos-rsm** xApplication stores all RAN slice information to **onos-topo** and **onos-uenib**.
- When a user creates/deletes/updates a slice through **onos-cli**, **onos-rsm** sends a control message to DU. Likewise, the user associates UE with a created slice through **onos-cli**, **onos-rsm** sends a control message to DU. After sending the control message successfully, **onos-rsm** updates **onos-topo** and **onos-uenib**, accordingly.
- Features of a slice (when it comes creating/updating a slice):
  - SCHEDULER_TYPE: scheduler type such as round robin (RR) and proportional fair (PF)
  - WEIGHT: time frame rates (e.g., 30). It should be less than 80.
  - SLICE_TYPE: downlink (DL) or uplink (UL)
- The commands requires two ids: target DU’s E2 Node ID & slice’s ID 


### onos-uenib
- [docLink](https://docs.sd-ran.org/master/onos-uenib/README.html) | [gitRepo](https://github.com/onosproject/onos-uenib) | [dockerImage] (https://hub.docker.com/r/onosproject/onos-uenib)
- This subsystem provides a central location for tracking information associated with RAN user equipment (UE).
- Applications can associate various aspects of information with each UE either for their one purpose or for sharing such state with other applications. The API and the system itself is designed to allow for high rate of data mutation and with minimum latency.
- Each UE object has a unique identifier that can be used to directly look it up, update or delete it.
- Since different use-cases or applications require tracking different information, and these may vary for different types of user equipment, the schema must be extensible to carry various aspects of information. This is where the notion of Aspect comes in. 
- An Aspect is a collection of structured information, modeled as a Protobuf message (although this is not strictly necessary), which is attached to the UE. In fact, UE entity carries only its unique identifier, and the rest of the information is expressed via aspects, which are tracked as a map of aspect type (TypeURL) and Protobuf Any message bindings.
- For example, to track UE cell connectivity, the system uses the CellInfo aspect defined as a CellConnection for the serving cell and the list of candidate cells
- [API Examples for Golang](https://docs.sd-ran.org/master/onos-uenib/docs/api-go.html)


### onos-topo
- [docLink](https://docs.sd-ran.org/master/onos-topo/README.html) | [gitRepo](https://github.com/onosproject/onos-topo) | [dockerImage] (https://hub.docker.com/r/onosproject/onos-topo)
- The µONOS Topology subsystem provides topology management for µONOS core services and applications. 
The topology subsystem structures the topology information as a set of objects, which can be either Entity, Relation or a Kind.
  - **Entity** objects are nodes in a graph and are generally intended to represent network devices, control entities, control domains, and so on.
  - **Relation** objects are edges in a graph and are intended to represent various types of relations between two Entity objects, e.g. contains, controls, implements.
  - **Kind** objects can be thought of as template or schema objects that represent an entity or a relation kind. Strictly speaking, Entity or Relation instances do not have to be associated with a Kind, but maintaining Kind associations can be used for schema validation and speeding up queries and is therefore highly encouraged.
- Each Entity, Relation and Kind objects has a unique identifier that can be used to directly look it up, update or delete it.
- The Entity and Relation objects themselves carry only the essential information for 
  - identifying them
  - associating them with a particular kind
  - in case of Relation, for associating the two Entity objects
- This is not sufficient to allow the platform or applications to track other pertinent information about the entities and relations. Since different use-cases or applications require tracking different information, and these may vary for different types of devices or network domains, the topology schema must be extensible to carry various aspects of information
  - This is where the notion of Aspect comes in
  - An Aspect is a collection of structured information, modeled as a Protobuf message (although this is not strictly necessary), which is attached to any type of object; generally mostly an Entity or a Relation.
  - Each object carries a mapping of aspect type (TypeURL) and Protobuf Any message
  - For example, to track a geo-location of a network element, one can associate **onos.topo.Location** instance, populated with the appropriate longitude and latitude with the Entity that represents that network element.
  - Similarly, to track information about the cone of signal coverage for a radio-unit, one can attach onos.topo.Coverage instance to an Entity representing the radio unit.
- To assist in categorization of the topology objects, each object can carry a number of labels as meta-data. Each label carries a value.
  - For example the deployment label can have production or staging or testing as values. 
  - Or similarly, tier label can have access, fabric or backhaul as values to indicate the area of network where the entity belongs.
- The topology API provides a **List** method to obtain a collection of objects. The caller can specify a number of different filters to narrow the results. All topology objects will be returned if the request does not contain any filters.
  - Type Filter: specifies which type(s) of objects should be included, e.g. Entity, Relation or Kind 
  - Kind Filter: specifies which kind(s) of objects should be included, e.g. contains, controls
  - Labels Filter: specifies which label name/value(s) should be included, e.g. tier=fabric
  - Relation Filter: specifies target entities related to a given source entity via a relation of a given kind
- 


### onos-api
- [docLink](https://docs.sd-ran.org/master/onos-api/README.html) | [gitRepo](https://github.com/onosproject/onos-api) | [dockerImage] (https://hub.docker.com/r/onosproject/onos-api) 
- gRPC API definitions for the µONOS platform.
- All of the protobuf definitions are available [here](https://github.com/onosproject/onos-api/tree/master/proto)
- It also includes python definitions.


### onos-mlb
- [docLink](https://docs.sd-ran.org/master/onos-mlb/README.html) | [gitRepo](https://github.com/onosproject/onos-mlb) | [dockerImage] (https://hub.docker.com/r/onosproject/onos-mlb)
- The xApplication for ONOS SD-RAN (µONOS Architecture) to balance load among connected cells (mobility load balancing)
- To begin with, onos-mlb defines each cell’s load as the number of active UEs, not considering other factors yet. If a cell services the most active UEs, the onos-mlb application considers that the cell suffers from the heaviest load. Then, this application defines two thresholds: (i) overload threshold and (ii) target threshold. A cell with the load that exceeds the overloaded threshold is an overloaded cell. On the other hands, a cell with the load that is less than target threshold has enough capacity.
- With the above definition, there are two conditions. (1) if a cell’s load > overload threshold and its neighbor cell’s load < target threshold, the xApplication increases Ocn of the neighbor cell. (2) if a cell’s load < target threshold, the xApplication decreases all neighbors’ Ocn.
- The increased Ocn makes the measurement event happening sensitively, which brings about more handover events happening to move some UEs to the neighbor cells, i.e., offloading. On the contrary, the measurement events happen conservatively with the decreased Ocn; it leads to the less handover events happening to avoid neighbor cells overloaded.
- The described algorithm runs periodically. By default, it is set to 10 seconds. The Ocn delta value (i.e., how many the application changes Ocn value) is configurable. By default, it is set to 3 to 6.

