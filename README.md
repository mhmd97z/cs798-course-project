**This is the repository for the course project of CS798-01 and CS798-02 at the CS dept of UWaterloo**

## ToDo List
- [x] Deploying uONOS and SD-RAN Simulator! 
- [x] Investigating uONOS components: 
  - [x] onos-kpimon [gathering metrics] 
  - [x] onos-mho [responsible for mobile handover] 
  - [x] onos-rsm [RAN slicing management] 
  - [x] onos-uenib 
  - [x] onos-topo 
  - [x] onos-api 
  - [x] onos-mlb 
- [x] Investigating Honeycomb Topology Generator options in modelling RAN
  - [x] model.yaml file detail 
    - [ ] pitch between cells
    - [x] max-collisions 
    - [ ] earfcn 
    - [ ] deform 
    - [ ] measurement params: timetotrigger, frequencyoffset, pcellindividualoffset, pcellindividualoffset, ncellindividualoffsets, hysteresis, eventa3params [a3offset, reportonleave] 
- [ ] Investigating RAN simulator gRPC APIs and onos cli 
  - [x] Protobuf structure 
  - [ ] provided gRPC
- [x] Read about NR Terminology
  - [x] onos components 
  - [x] Investigating RRC protocol to understand what are the provided KPIs 
- [ ] * How PRBs are being allocated accross slices?
- [ ] * How to simulate a scenario comprising of sending traffic 
  - [ ] * What about the core? Do we need?
- [ ] * Watching sd-ran community sessions!
  - [ ] * 
  - [ ] * 
- [ ] * Investigating python sdk
- [ ] + Overhead  of collecting CQI values: 
  - [ ] + How often it's changing 
  - [ ] + Actual data Vs headers 
- [ ] + VNFs
- [ ] + Non-real-time RIC. How would that be compatible with this setup?


## Steps to Deploy SD-RAN Components using Kubernetes
- Setting up Kubernetes
  - Insalling utilities on the master and worker nodes using this [link](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
  - Setting up the cluster using this [link](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
    - ``kubeadm init --apiserver-advertise-address=<MASTER IP ADDR>``
    - this will give you a token that worker nodes need to use for authentication
    - Just need to run this on the worker nodes:``kubeadm join 10.10.0.213:6443 --token 1ms8en.e7odz1p9wk6xupb1	--discovery-token-ca-cert-hash sha256:051d68ecbe193de503614fc6402c872daabc1cd1131dcdd7496349f7036972dc``
    - it will print some commands needs to be run as well!
  - Moving on, you need to enable networking add-on. Here I chose to use weavenet:
    - ``kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"``
  - If you want to reinit the cluster, do what follows:
    - [https://www.techrunnr.com/how-to-reset-kubernetes-cluster/](https://www.techrunnr.com/how-to-reset-kubernetes-cluster/)
- Deploying prerequisites of SD-RAN  
  - Starting form the Prerequisites section on this [page](https://docs.onosproject.org/developers/deploy_with_helm/)
- Deploying SD-RAN and RAN-Simulator
  - Using this [page](https://github.com/onosproject/ran-simulator/blob/master/docs/quick_start.md)
  - You should take a step here nit mentioned in the instruction: ``make dep``
  - Then, you will first deploy sd-ran components [in the sd-ran namespace], after which you'd deploy ran-simulator [again, in the sd-ran namespace].

**Note:**
- RAN simulator is not enabled in the sd-ran chart by default. You can enable it when you deploy sd-ran helm chart using the following command
``helm install sd-ran sd-ran -n sd-ran --set import.ran-simulator.enabled=true``
- By default, RANSim uses the model.yaml model file. To use a different model, e.g. the two-cell-two-node-model, specify the model as follows:
``helm install --set import.ran-simulator.enabled=true --set import.onos-mho.enabled=true --set ran-simulator.pci.modelName=two-cell-two-node-model sd-ran sd-ran``


### Useful Kub commands
- ``kubeadm version --output=short``: get the kubeadm version
- ``kubectl label node oran-worker node-role.kubernetes.io/worker=worker``: add worker label 
- ``kubectl -n micro-onos get pods``: get pods on the micro-onos namesapce
- ``kubectl -n kube-system get pods``: get pods on the kube-system namesapce
- ``kubectl get namespace``: get kubernetes namespaces
- ``kubectl get nodes``: gues what?! 
- ``kubectl get all``: guess what?! 
- ``kubectl get svc``: get 
- ``kubectl describe nodes my-node``: get the detail of a node
- ``kubectl describe pods my-pod``: get the detail of a pod
- ``docker exec -it -u root <Container_ID> /bin/bash``: to get root access to the docker, run this command on the corresponding node
- ``kubectl delete --all pods --namespace=foo``
- ``helm delete -n micro-onos onos-uenib``:  uninstall the onos-uenib chart

### Deployed pods

``` Bash
~/$ kubectl get pods -n micro-onos
NAME                           READY   STATUS    RESTARTS   AGE
onos-cli-86448f879f-tzw67      1/1     Running   0          2d6h
onos-config-6546c457fc-h5vwg   6/6     Running   0          2d6h
onos-consensus-store-0         1/1     Running   0          2d6h
onos-gui-65f4754c5f-lx5r8      2/2     Running   0          2d6h
onos-topo-8666cfb4bf-h9tts     3/3     Running   0          2d6h
```

``` Bash
~/$ kubectl get pods -n sd-ran
NAME                             READY   STATUS    RESTARTS   AGE
onos-a1t-7cd8c9697b-4kn5p        2/2     Running   0          98m
onos-cli-769bbf9d4f-q45tg        1/1     Running   0          98m
onos-config-6ccff5d6b9-djwlr     4/4     Running   0          98m
onos-consensus-store-0           1/1     Running   0          98m
onos-e2t-59fbcb6d54-mhxwq        3/3     Running   0          98m
onos-topo-7448789796-jndsn       3/3     Running   0          98m
onos-uenib-645fbc8574-4hjj4      3/3     Running   0          98m
ran-simulator-6c9697b594-mrgg8   1/1     Running   0          57m
```

## SD-RAN commands cheatsheet! 
- Getting access to the **onos-cli**:

You can either setup it from [here](https://docs.onosproject.org/onos-cli/docs/setup/),
``` Bash
kubectl -n micro-onos exec -it $(kubectl -n micro-onos get pods -l type=cli -o name) -- /bin/sh
```

OR run your commands using ``kubectl exec`` with this [instruction](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#exec). Like: 

``` Bash
clipod=$(kubectl -n sd-ran get pods | grep onos-cli | cut -d\  -f1)
kubectl -n sd-ran exec --stdin $clipod -- /usr/local/bin/onos ransim get nodes
```

- Working with ``onos-kpimon``
``` Bash
onos kpimon list metrics
```
- Working with ``onos-mho``
``` Bash
onos mho get cells
onos mho get ues
onos uenib get ues [-v]
onos uenib get ue <ueID> [-v]
```
- Working with ``onos-ransim`` | [docLink](https://github.com/onosproject/onos-cli/blob/master/docs/cli/onos_ransim.md)
``` Bash
onos ransim get cells
onos ransim get ues
onos ransim get ue <ueID>
```
- Working with ``onos-rsm``
``` Bash
## Creating a slice
onos rsm create slice --e2NodeID <DU_E2_NODE_ID> --scheduler <SCHEDULER_TYPE> --sliceID <SLICE_ID> --weight <WEIGHT> --sliceType <SLICE_TYPE>
# example:
onos rsm create slice --e2NodeID e2:4/e00/3/c8 --scheduler RR --sliceID 1 --weight 30 --sliceType DL

## Update a slice
onos rsm update slice --e2NodeID <DU_E2_NODE_ID> --scheduler <SCHEDULER_TYPE> --sliceID <SLICE_ID> --weight <WEIGHT> --sliceType <SLICE_TYPE>
# example:
onos rsm update slice --e2NodeID e2:4/e00/3/c8 --scheduler RR --sliceID 1 --weight 50 --sliceType DL
 
## Delete a slice
onos rsm delete slice --e2NodeID <DU_E2_NODE_ID> --sliceID <SLICE_ID> --sliceType <SLICE_TYPE>
# example:
onos rsm delete slice --e2NodeID e2:4/e00/3/c8 --sliceID 1 --sliceType DL

## UE-slice association
onos rsm set association --dlSliceID <SLICE_ID> --e2NodeID <DU_E2_NODE_ID> --drbID <DRB_ID> --DuUeF1apID <DU_UE_F1AP_ID>
# example:
onos rsm set association --dlSliceID 1 --e2NodeID e2:4/e00/3/c8 --drbID 5 --DuUeF1apID 1240
```
- Working with ``onos-uenib``
``` Bash
onos uenib get ues --aspect onos.uenib.CellInfo # List CellInfo and SubscriberData of all UEs, that have these aspects.
onos uenib create ue 9182838476 --aspect operator.CustomData='{"foo": "bar", "special": true}'
 # Create a new CustomData aspect for a UE:
onos uenib get ue 9182838476 --verbose # Show all aspect data in verbose form for a given UE:
onos uenib watch ues --no-replay # Watch all changes in the UE NIB, without replay of existing UE information:
onos uenib delete ue 9182838476 --aspect operator.CustomData # Delete CustomData aspect for a specific UE:
```
- Working with ``onos-cli`` | [docLink](https://github.com/onosproject/onos-cli/blob/master/docs/cli/onos_topo.md)
``` Bash
onos topo get entities # List all entities
onos topo get entities --kind e2node # List all entities of e2node kind.
onos topo get entities --related-to 5153 --related-via contains # List all e2cell entities related to the specified e2node via contains relation.
onos topo get entity 1454c001 -v # Show verbose information on entity 1454c001
onos topo get relations --kind neighbors # Show all neighbors relations
onos topo create entity "virtual" --aspect onos.topo.Configurable='{"type": "devicesim-1.0.x", "version": "1.0.0"}' # Create a new entity with sparsely populated Configurable aspect
```
- Working with ``onos-mlb`` | [docLink]()
``` Bash
onos mlb list ocns # to see Ocn values for each cell
onos mlb list parameters # to see mlb parameters
onos mlb set parameters --interval 20 # to change mlb parameters

```

### Useful links!
- [General Instructions](https://docs.onosproject.org/onos-cli/docs/cli/onos/) 
- [SD-RAN Documentation](https://docs.sd-ran.org/master/index.html)
- [RIC Agent deployment with OAI CU DU](https://github.com/onosproject/openairinterface5g)
- [OAI 5G RF simulator deployment (RAN and CORE) tutorial](https://gitlab.flux.utah.edu/powder-mirror/openairinterface5g/-/tree/de8d4f431821f865672e17fcb3c0176eb5775907/ci-scripts/yaml_files/5g_rfsimulator)

### Timeline
- Deploy a testbed based on open-source solutions offered by ONF, we will be using their SD-RANsimulator to implement the different RAN data plane components and theμonos nRT-RIC asthe control plane -> 
- Explore the available features and telemetry that we obtain from the data plane to serve as inputto our RRM algorithm and its control knobs. -> 
- Study existing developed RRM xApps, investigate their shortcomings and determine what im-provements can be done. -> 
- Replicating some existing solutions as the baseline. -> 
- Develop an algorithm based on machine or reinforcement learning methods for radio resourcemanagement. -> 
