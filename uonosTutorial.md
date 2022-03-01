## uONOS 

### Basics
- ONOS RIC consists of multiple micro-services, each is deployed as a Kubernetes pod, and communication between micro-services are mainly done through gRPC.
- The majority of the micro-services are implemented in GO, with the E2 interface decoding and encoding implemented in C.


### Architecture
- **onos-e2t**
  - **onos-e2t** micro-service is the one that actually connects E2 nodes with xApps. This micro-service terminates E2 interfaces, manages subscriptions, and hosts xApps.
  - In the implementation of ONOS RIC, communication between **onos-e2t** and xApps are done through Protobuf messages, instead of E2 messages (which are in ASN.1 syntax).
  - **onos-e2t** micro-service is also responsible for maintaining topology of all E2 nodes connected and storing a list of RAN functions supported by each E2 node using information gathered from setup stage and service update requests. This micro-service stores information using APIs exposed by **onos-topo** and **onos-uenib**.
- **onos-topo**
  - ONOS RIC uses **onos-topo** as a R-NIB storage. Specifically, information regarding E2 nodes and their relationship, information regarding cells and slicing are stored using **onos-topo** to manage and provide a shared view of the overall RAN system.
- **onos-uenib**
  - UE-related information is stored using APIs provided by **onos-uenib**, a new micro-service designed specifically to store and track UE information with minimum latency and high throughput rate.
- **onos-e2-sm**
  - Service models are implemented in **onos-e2-sm**. It is a shared library that contains all supported service models and mapping between the ASN.1 definition (for E2 messages) and protobuf definition (for xApps) of the service models. By using a separate library, ONOS RIC decouples service model with the remaining system, making ONOS RIC capable of handling any E2SM.


### Supported Service Model and xApps
Currently, all E2SMs and xApps supported by ONOS RIC are implemented in GO, however, a Python SDK is now in the beta stage and we could see xApps implemented in Python coming in the future. 
- KPM: allows gathering metric data from E2 nodes
  - **onos-kpimon** xApp is provided as a sample xApp that runs over this service model to collect metric data. The collected data can be retrieved through **onos-cli** command-line interface.
- NI: currently, only the protobuf definition of this service model has been implemented
  - No xApps that run over this service model is provided by SD-RAN project.
- RC: [RAN Control] This service model allows RIC to gather cells (PCI) and neighbor relationship.
  - SD-RAN project provides the **onos-pci** xApp to demonstrate this service model. This xApp provides access to PCI resources through **onos-cli** command-line interface. It allows the collection of data related to PCI and PCI conflicts. This xApp is also capable of detecting and resolving PCI conflicts using built-in algorithms.
- MHO: [Mobile Handover] This service model handles all mobile handover procedure-related operations. This service model allows collection of signal metric data for UEs and RRC state change data. It also allows control signalling for initiating mobile handover procedures.
  - The **onos-mho** xApp runs over this service model and serves as a sample use case for this service model.
- RSM: [RAN Slicing Management] This service model allows creating, updating and deleting RAN slices
  - SD-RAN project provides a simple xApp **onos-rsm** that runs over this service model. This app allows creating, updating and deleting RAN slices through a command-line interface. User is also capable of specifying a UE to a slice through the command line. This xApp would also store and update the topology and UE properties related to RAN slicing operations using **onos-topo** and **onos-uenib** accordingly.


### onos-kpimon
- [docLink](https://docs.sd-ran.org/master/onos-kpimon/README.html) | [gitRepo](https://github.com/onosproject/onos-kpimon) | [dockerImage](https://hub.docker.com/r/onosproject/onos-kpimon)
- This xApp provides this set of KPIs:
  - Node ID
  - Cell Object ID
  - Cell Global ID
  - Time
  - RRC.Conn.{Avg & Max}
  - RRC.ConnEstabAtt.Sum
  - RRC.ConnEstabSucc.Sum
  - RRC.ConnReEstabAtt.{HOFail & Other & Sum & reconfigFail}
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
