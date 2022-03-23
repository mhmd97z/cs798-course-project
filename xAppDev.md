## python xApp development

### onos-ric-sdk-py
It includes two main modules: E2 and SDL!

With **E2** module, you can send control messages to the RIC and subscribe/unsubscribe to e2 nodes service model.

With **SDL** module, you can get topology information from the RIC, for entities such as E2 nodes and cells + read and write properties for E2 nodes and cells.
- Get the cells corresponding to the given E2 node ID
- get/set data referenced by key attached to a cell_id
- Stream for newly available E2 node connections

### onos-e2-sm
TBD!


### xApp python examples: fb-kpimon-xapp
**How to use this package**
- Creating sdk.E2Client and sdk.SDLClient!
- Looking 2t nodes using sdl_client.watch_e2_connections  
  - going over service_models to find oid = KPM_SERVICE_MODEL_OID_V2
  - running **kpimon.run**
    - app_config, e2_client, sdl_client, e2_node_id, e2_node, service_model

**How the package works**
- it defines a list of actions and a trigger to establish a subscroption and then periodaclly gethers data from the cells and updates the prometheus gauge endpoint
- But I geuss the kind of measuements it can get is defined in the service model, and this xapp only goes over on that and sets the corresponding values!

### xApp python examples: fb-ah-xapp
- This app is an adapter to Airhop's eSON service, covering physical cell identifier (PCI) confict resolution, and mobility load balancing (MLB).
- An E2 subscription to the rc-pre service model is made. Cell information such as PCI and neighbor information is received pushed to the Airhop eSON service.
  - PCI information of the cell and its neighbors are used by the eSON PCI conflict algorithm.
  - Cell individual offset of the cell and its neighbors are used by the eSON MLB algorithm.
- An E2 subscription to the KPM service model is also made. The cell capacity information is sent to the eSON service and used by the MLB algorithm.
- The app listens to changes from the eSON service. PCI change requests are issued via the eSON's conflict resolution algorithm, neighbor cell individual offset change requests are issued by eSON's MLB algorithm. When a change request is received, the app will issue an E2 control message to the expected E2 node.
- This all also responds to http requests to view or modify the cell information.
- Since the Airhop eSON service is a commercial product, it is not included in this package, instead a test server is included that mimics messages that could be sent from the eSON service. The messages do not perform the PCI conflict and MLB algorithms, but will send arbitrary PCI change requests and cell individual offset change requests to exercise the E2 control pathways.