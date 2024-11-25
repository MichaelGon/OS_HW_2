from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        self.wfile.write(b"Hello, this is a response to your GET request!")

    def do_POST(self):
        self.send_response(405)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=HTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
