import json
import BaseHTTPServer
import SocketServer

port = 8080
latitude, longitude = 40.3788236,-79.8191923
accuracy = 50

class handler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({
            "location": {
                "lat": latitute,
                "lng": longitude
            },
            "accuracy": accuracy
        }))

    def do_POST(self):
        return self.do_GET()

httpd = SocketServer.TCPServer(("", port), handler)
print ("Dumping Geolocation {0} - {1} with accuracy of {2} at port:{3}".format(latitude, longitude, accuracy, port))