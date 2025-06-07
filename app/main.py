from http.server import BaseHTTPRequestHandler, HTTPServer

HOST, PORT = "0.0.0.0", 8080


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        message = "👋 Hello from inside a Docker container!"
        self.wfile.write(message.encode('utf-8'))


if __name__ == "__main__":
    httpd = HTTPServer((HOST, PORT), HelloHandler)
    print(f"Serving on http://{HOST}:{PORT}")
    httpd.serve_forever()
