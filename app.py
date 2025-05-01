from http.server import SimpleHTTPRequestHandler, HTTPServer

HOST, PORT = "0.0.0.0", 8080
Handler = SimpleHTTPRequestHandler

with HTTPServer((HOST, PORT), Handler) as httpd:
    print(f"Serving HTTP on {HOST}:{PORT}")
    httpd.serve_forever()

