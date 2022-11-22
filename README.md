Simple web service running on localhost:8080 which returns the closing stock price for a specified number of days for a given stock symbol, which are passed in as environment variables in config.yaml, as well as an average price.

Based on image at https://hub.docker.com/repository/docker/jpavia/python

In order to run:

1. enter bash shell
2. run "./startup.sh" in top directory of repo
3. open new terminal
4. run  "kubectl port-forward service/rock 8080:8080"
5. browse to http://localhost:8080
6. For Windows, enter the commands in startup.sh or convert to .bat


