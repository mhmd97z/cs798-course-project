**This is the repository for the course project of CS798-01 and CS798-02 at the CS dept of UWaterloo**

## ToDo List
- [x] Deploying uONOS and SD-RAN Simulator! 
- [ ] Simulating a RAN instance: a few BSs and UEs, etc.

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
  - The **onos-mho** xApp runs over this service model and serves as a sample use case for this service model
- RSM: [RAN Slicing Management] This service model allows creating, updating and deleting RAN slices
  - SD-RAN project provides a simple xApp **onos-rsm** that runs over this service model. This app allows creating, updating and deleting RAN slices through a command-line interface. User is also capable of specifying a UE to a slice through the command line. This xApp would also store and update the topology and UE properties related to RAN slicing operations using **onos-topo** and **onos-uenib** accordingly.


## Steps to Deploy SD-RAN Components using Kubernetes
- Setting up Kubernetes
  - Insalling utilities on the master and worker nodes using this [link](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
  - Setting up the cluster on the master node using this [link](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
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
RAN simulator is not enabled in the sd-ran chart by default. You can enable it when you deploy sd-ran helm chart using the following command
``helm install sd-ran sd-ran -n sd-ran --set import.ran-simulator.enabled=true``

### Useful Kub commands
- ``kubeadm version --output=short``: get the kubeadm version
- ``kubectl label node oran-worker node-role.kubernetes.io/worker=worker``: add worker label 
- ``kubectl -n micro-onos get pods``: get pods on the micro-onos namesapce
- ``kubectl -n kube-system get pods``: get pods on the kube-system namesapce
- ``kubectl get namespace``: get kubernetes namespaces
- ``kubectl get nodes``: get nodes
- ``kubectl describe nodes my-node``: get the detail of a node
- ``kubectl describe pods my-pod``: get the detail of a pod

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

## Working with SD-RAN APIs
At first, onos cli is not readily accessible. You can either setup it from [here](https://docs.onosproject.org/onos-cli/docs/setup/), or run your commands using ``kubectl exec`` with this [instructions](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#exec) 

### Useful links!
- [General Instructions](https://docs.onosproject.org/onos-cli/docs/cli/onos/) 
- 