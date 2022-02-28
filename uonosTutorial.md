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
