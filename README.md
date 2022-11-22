Simple web service running on localhost:8080 which returns the closing stock price for a specified number of days for a given stock symbol, which are passed in as environment variables in config.yaml, as well as an average price.

Based on image at https://hub.docker.com/repository/docker/jpavia/python

In order to run:

1. enter bash shell
2. run "./startup.sh" in top directory of repo
3. open new terminal
4. run  "kubectl port-forward service/rock 8080:8080"
5. browse to http://localhost:8080

From Command Line

1. kubectl apply -f k8s/deployment.yaml
2. kubectl apply -f k8s/service.yaml
3. kubectl apply -f k8s/config.yaml
4. kubectl apply -f k8s/secret.yaml
5. open new terminal
6. run  "kubectl port-forward service/rock 8080:8080"
7. browse to http://localhost:8080
