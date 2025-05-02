from http.server import SimpleHTTPRequestHandler, HTTPServer

HOST, PORT = "0.0.0.0", 8080

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Always return 200 and a friendly message
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'👋 Hello from inside a Docker container!')

if __name__ == "__main__":
    httpd = HTTPServer((HOST, PORT), HelloHandler)
    print(f"Serving on http://{HOST}:{PORT}")
    httpd.serve_forever()
