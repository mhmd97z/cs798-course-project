## SD-RAN Simulator
With the help of [Honeycomb Topology Generator](https://github.com/onosproject/ran-simulator/blob/master/docs/topology_generator.md), you can define models on which SD-RAN simulator builds its simulation network. There are a few models available [here](https://github.com/onosproject/sdran-helm-charts/tree/master/ran-simulator/files/model).

### Honeycomb Topology Generator
The RAN simulator comes with an accompanying utility that generates a RAN topology YAML file that is ready to be loaded by the RAN simulator. This utility generates a hexagonal grid of RAN towers (E2 Nodes), each with a prescribed number of cells with equal arc of coverage. The following is the command-line usage:
``` Bash
  honeycomb topo outfile [flags]
‍‍‍‍Flags:
      --cell-types strings             List of cell size types (default [FEMTO,ENTERPRISE,OUTDOOR_SMALL,MACRO])
      --controller-addresses strings   List of E2T controller addresses or service names (default [onos-e2t])
      --controller-yaml string         if specified, location of yaml file for controller
      --deform-scale float             scale factor for perturbation (default 0.01)
      --earfcn-start uint32            start point for EARFCN generation (default 42)
      --gnbid-start string             GnbID start in hex (default "5152")
  -h, --help                           help for topo
  -a, --latitude float                 Map centre latitude in degrees (default 52.52)
  -g, --longitude float                Map centre longitude in degrees (default 13.405)
      --max-collisions uint            maximum number of collisions (default 8)
  -d, --max-neighbor-distance float    Maximum 'distance' between neighbor cells; see docs (default 3600)
      --max-neighbors int              Maximum number of neighbors a cell will have; -1 no limit (default 5)
      --max-pci uint                   maximum PCI value (default 503)
      --min-pci uint                   minimum PCI value
  -i, --pitch float32                  pitch between cells in degrees (default 0.02)
      --plmnid string                  PlmnID in MCC-MNC format, e.g. CCCNNN or CCCNN (default "315010")
  -s, --sectors-per-tower uint         sectors per tower (default 3)
      --service-models strings         List of service models supported by the nodes (default [kpm/1,rcpre2/3,kpm2/4,mho/5])
      --single-node                    generate a single node for all cells
  -t, --towers uint                    number of towers
      --ue-count uint                  User Equipment count
      --ue-count-per-cell uint         Desired UE count per cell (default 15)
```

Output YAML File: [shrtened version]
```
layout:
  center:
    lat: 52.52
    lng: 13.405
  zoom: 0
  locationsscale: 1.25
  fademap: false
  showroutes: false
  showpower: false
nodes:
  node1:
    gnbid: 20819
    controllers:
    - e2t-1
    servicemodels:
    - mho
    - rcpre2
    - kpm2
    cells:
    - 87893173159116801
    - 87893173159116802
    - 87893173159116803
    status: stopped
cells:
  cell1:
    ncgi: 87893173159116801
    sector:
      center:
        lat: 52.486405366824926
        lng: 13.412233915182187
      azimuth: 0
      arc: 120
      tilt: 1
      height: 43 
    color: green
    maxues: 99999
    neighbors:
    - 87893173159116802
    - 87893173159116803
    - 87893173159133185
    txpowerdb: 11
    measurementparams:
      timetotrigger: 0
      frequencyoffset: 0
      pcellindividualoffset: 0
      ncellindividualoffsets: {}
      hysteresis: 0
      eventa3params:
        a3offset: 0
        reportonleave: false
    pci: 218
    earfcn: 42
    celltype: 2
    rrcidlecount: 0
    rrcconnectedcount: 0
controllers:
  e2t-1:
  id: e2t-1
  address: onos-e2t
  port: 36421
servicemodels:
  kpm2:
    id: 4
    description: kpm2 service model
    version: 1.0.0
  mho:
    id: 5
    description: mho service model
    version: 1.0.0
  rcpre2:
    id: 3
    description: rcpre2 service model
    version: 1.0.0
ueCount: 10
ueCountPerCell: 15
plmnID: "138426"
plmnNumber: 1279014
apiKey: ""
```


### How to work with ran sim
The E2 nodes can be defined statically in the simulation model from the RAN simulator helm chart or can be added/removed at runtime using [RAN simulator APIs](https://github.com/onosproject/onos-api/). Additionally, there's a specific [cli](https://github.com/onosproject/onos-cli/blob/master/docs/cli/onos_ransim.md) for that in onos-cli! 
- Simulation model
  - Using honeycomb
- RAN simulator gRPC APIs
  - **Model API**: provides means to create, delete and read RAN simulation model such as E2 nodes and cells.
  - **Metrics API**: provides means to create, delete, and read metrics for the specified entity ( e.g. A node, a cell, or a UE)
  - **Traffic Sim API**: provides means to create, list, and monitor UEs.
  - 


### onos-ransim
- Get: 
  - get: Commands for retrieving RAN simulator model and other information
    - cells:
      - NCGI
      - #UEs
      - Max UEs
      - TxDB
      - Lat
      - Lng
      - Azimuth 
      - Arc
      - A3Offset
      - TTT
      - A3Hyst
      - PCellOffset
      - FreqOffset
      - PCI 
      - Color
      - Idle
      - Conn
      - Neighbors(NCellOffset)
    - layout:
      - Center
      - Zoom
      - Fade
      - ShowRoutes
      - ShowPower
      - LocationsScale
    - metrics: [Get all metrics of an entity - entityID must be given] ????
      - 
    - nodes: [Get all E2 nodes]
      - GnbID
      - Status 
      - Service Models 
      - E2T Controllers 
      - Cell NCGIs 
    - plmnid: prints one value!
    - routes: [get all ue routes]
      - IMSI
      - Color
      - µkm/h
      - -∂km/h
      - Waypoints [a list of (lat, long)]
    - ues: 
      - IMSI
      - Serving Cell
      - CRNTI
      - Admitted
      - RRC
    - ueCount: [get ue count]
- Set (+Get):
  - create: Commands for creating simulated entities
    - 
  - set: Commands for setting RAN simulator model metrics and other information
    - cell
    - metric
    - node
    - ue
    - ueCount
  - delete: Commands for deleting simulated entities
    - cell
    - metric
    - node
    - route
  - load: Load model and/or metric data
    - a path to a YAML file must be given
  - start: Start E2 node agent
    - 
  - stop: Stop E2 node agent
    - 
  - clear: Clear the simulated nodes, cells and metrics
    - 
