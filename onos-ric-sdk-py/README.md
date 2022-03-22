# onos-ric-sdk-py
Python Application SDK for ONOS RIC (µONOS Architecture)

## Description
This SDK contains two modules, E2 and SDL.

The SDK uses a sidecar proxy which implements the client side distributed system and load-balancing logic necessary to communicate to the RIC.

In addition, *onos_ric_sdk_py* creates an HTTP server for xApp configuration/ Developers can add their own endpoints to this server for their own
application logic.

Have a look at **docs/index.rst**


### E2 module
The E2 module contains functions that interact with E2 nodes (**onos_api.e2t** python package). Apps can subscribe and unsubscribe to service models, and apps can send E2 control messages to make changes to E2 nodes. The E2 module interacts with the e2t node.

Methods of the class **E2Client**:
- control
  - Send a control message to the RIC to initiate or resume some functionality
  - Args
    - e2_node_id: The target E2 node ID.
    - service_model_name: The service model name
    - service_model_version: The service model version
    - header: The RIC control header
    - message: The RIC control message
- subscribe
  - Establish an E2 subscription
  - Args
    - e2_node_id: The target E2 node ID
    - service_model_name: The service model name
    - service_model_version: The service model version
    - subscription_id: The ID to use for the subscription
    - trigger: The event trigger
    - actions: A sequence of RIC service actions
  - Yields
    - The next indication header and message, if available
- unsubscribe
  - Delete an E2 subscription
  - Args
    - e2_node_id: The target E2 node ID
    - service_model_name: The service model name
    - service_model_version: The service model version
    - subscription_id: The ID of the subscription to delete


### SDL module
The SDL module contains functions to get topology information from the RIC, for entities such as E2 nodes and cells (**onos_api.topo** python package). This module to also includes functions to read and write properties for E2 nodes and cells.

Methods of the class **E2Client**:
- get_cells
  - Get the cells corresponding to the given E2 node ID
  - Args:
    - e2_node_id: The target E2 node ID
  - Returns:
    - A list of cells that belong to ``e2_node_id``
- _get_cell_entity_id
  - given e2_node_id and cell_global_id, returns entity id
  - returns None if cell_global_id is not found
- get_cell_data
  - get data referenced by key attached to a cell_id, if available otherwise returns None
- set_cell_data
  - set data referenced by key attached to a cell_id remove data referenced by key if data is None
- watch_e2_connections
  - Stream for newly available E2 node connections
  - Yields
    - An available E2 node and its ID.
  - 
