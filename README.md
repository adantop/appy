# appy
Python API with flask

## Requirements
- Docker
- minikube
- kubectl

## Steps
```git clone https://github.com/adantop/appy.git
cd appy
service docker start
docker build -t appy:{vers_no} .
minikube start --driver=docker
eval $(minikube docker-env)
kubectl apply -f ./deployments/appy.yaml
kubectl expose deployment appy-deployment --type=NodePort
minikube service appy-deployment --url
```
