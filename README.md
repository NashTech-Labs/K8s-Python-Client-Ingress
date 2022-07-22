### Install Kubernetes Python Client:

`git clone --recursive https://github.com/kubernetes-client/python.git cd`

`cd python`

`python setup.py install`

### Installation from pip:

`pip install kubernetes`

For Ingress on local cluster e.g minikube we use following command:

`config. load_kube_config()`

### Authentication to the Kubernetes Python Client in other cluster is done by: 

`configuration.api_key = {"authorization": "Bearer" + bearer_token}`

We will use here the Bearer Token which enable requests to authenticate using an access key.

In get-create-ingress.py file there is a functions for creating ingress:


1. Create Ingress

In this we have to pass the namespace in which we will update Ingress:
namespace="default"

Give your cluster details:
```
cluster_details={
        "bearer_token":"Your_cluster_bearer_token",
        "api_server_endpoint":"Your_cluster_IP"
    }
```

### Running the File:
```
python3 get-create-ingress.py
```

### Check the Ingress:
```
kubectl get ingress
```