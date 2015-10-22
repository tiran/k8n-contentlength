kubectl delete pod contentlength 
kubectl delete service contentlength
kubectl create -f contentlength-bug-pod.yaml
kubectl create -f contentlength-bug-service.yaml
