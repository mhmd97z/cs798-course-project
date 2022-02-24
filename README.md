**This is the repository for the course project of CS798-01 and CS798-02 at the CS dept of UWaterloo**

## ToDo List
- [ ] Deploying uONOS and SD-RAN Simulator! 


## Taken steps to Deploy SD-RAN Components
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


## Useful Kub commands
- ``kubeadm version --output=short``: get the kubeadm version
- ``kubectl label node oran-worker node-role.kubernetes.io/worker=worker``: add worker label 
- ``kubectl -n micro-onos get pods``: get pods on the micro-onos namesapce
- ``kubectl -n kube-system get pods``: get pods on the kube-system namesapce
- ``kubectl get namespace``: get kubernetes namespaces
- ``kubectl get nodes``: get nodes
- ``kubectl describe nodes my-node``: get the detail of a node
- ``kubectl describe pods my-pod``: get the detail of a pod
