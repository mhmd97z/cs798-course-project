## SD-RAN Simulator
With the help of [Honeycomb Topology Generator](https://github.com/onosproject/ran-simulator/blob/master/docs/topology_generator.md), you can define models on which SD-RAN simulator builds its simulation network. There are a few models available [here](https://github.com/onosproject/sdran-helm-charts/tree/master/ran-simulator/files/model). 

### Honeycomb Topology Generator
The RAN simulator comes with an accompanying utility that generates a RAN topology YAML file that is ready to be loaded by the RAN simulator. This utility generates a hexagonal grid of RAN towers (E2 Nodes), each with a prescribed number of cells with equal arc of coverage. The following is the command-line usage:

### How to work with that!
The E2 nodes can be defined statically in the simulation model from the RAN simulator helm chart or can be added/removed at runtime using [RAN simulator APIs](https://github.com/onosproject/onos-api/). Additionally, there's a specific [cli](https://github.com/onosproject/onos-cli/blob/master/docs/cli/onos_ransim.md) for that in onos-cli! 
- Simulation model
  - Using honeycomb
- RAN simulator gRPC APIs
  - **Model API**: provides means to create, delete and read RAN simulation model such as E2 nodes and cells.
  - **Metrics API**: provides means to create, delete, and read metrics for the specified entity ( e.g. A node, a cell, or a UE)
  - **Traffic Sim API**: provides means to create, list, and monitor UEs.
  - 
