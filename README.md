**This is the repository for the course project of CS798-01 and CS798-02 at the CS dept of UWaterloo**

## ToDo List
- [x] Deploying uONOS and SD-RAN Simulator! 
- [ ] Simulating a RAN instance: a few BSs and UEs, etc.


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
