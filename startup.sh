 kubectl delete deployments rock
 sleep 10
 kubectl apply -f k8s/deployment.yaml
 kubectl apply -f k8s/service.yaml
 kubectl apply -f k8s/config.yaml
 kubectl apply -f k8s/secret.yaml
 sleep 10
 #kubectl port-forward service/rock 8080:8080 &