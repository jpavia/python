from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import sys
import json
import os

# Get environment variables
SYMBOL = os.getenv('SYMBOL')
APIKEY = os.getenv('APIKEY')
NDAYS = int(os.getenv('NDAYS'))

print(f"NDAYS is {NDAYS} type {type(NDAYS)}")
print(f"SYMBOL is {SYMBOL}")
hostName = "0.0.0.0"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.request import urlopen
        url = "https://www.alphavantage.co/query?apikey="+APIKEY+"function=TIME_SERIES_DAILY_ADJUSTED&symbol="+SYMBOL
        response = urlopen(url)
        stock = (json.loads(response.read()))
        stock=(stock['Time Series (Daily)'])
        #day=(stock["2022-11-18"])
        n=0
        sum=0.0
        cprice=[]
        for i in stock:
            n=n + 1
            day=(stock[i])
            price=day["4. close"]
            price=float(price)
            cprice.append(price)
            sum=sum + price
            if n==NDAYS:
                break
        avg=sum/int(NDAYS) 
     

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Stock Symbol: %s</p>" % SYMBOL, "utf-8"))
        self.wfile.write(bytes("<p>Average Closing Price for last %s days</p>" % NDAYS, "utf-8"))
        self.wfile.write(bytes("<p>Daily Prices: %s</p>" % cprice, "utf-8"))
        self.wfile.write(bytes("<p>Average Closing Price: %s</p>" % avg, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")