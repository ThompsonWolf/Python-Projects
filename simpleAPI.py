# Here's a simple API using Python's built-in http.server module, without external libraries. This will allow you to create a basic web servver that can handle GET and POST requests

"""
Explanation:

1. SimpleAPIHandler: This class defines handlers for GET and POST requests.
    > GET: Returns a JSON response with a simple message
    > POST: Reads JSON data sent in the request body, parses it, and responds with the sama data along with a message

2. run function sets up the server on port 8080 and starts it.
"""


from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Define the request handler
class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Define a simple data response
        response = {
            "message": "Hello, this is a GET request !",
            "path": self.path
        }

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        # Write the JSON response
        self.wfile.write(json.dumps(response).encode("utf-8"))

    def do_POST(self):
        # Read the content length to know how much data to read
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)

        # Parse the received data as JSON
        try:
            data = json.loads(post_data)
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'{"error": "Invalid JSON"}')
            return

        # Process the data and send a response
        response = {
            "message": "Hello, this is a POST requests !",
            "received_data": data
        }

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        # Write the JSON response
        self.wfile.write(json.dumps(response).encode("utf-8"))
        
        
# Set up the server
def run(server_class=HTTPServer, handler_class = SimpleAPIHandler, port=8080):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}.....")
    httpd.serve_forever()


# Run the server
if __name__ == "__main__":
    run()

