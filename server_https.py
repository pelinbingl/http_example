from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

class SimpleHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print("POST verisi:", post_data.decode())
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"200 OK - SSL ile alindi")

httpd = HTTPServer(('localhost', 4444), SimpleHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='server.crt', keyfile='server.key', server_side=True)

print("HTTPS server çalışıyor: https://localhost:4444")
httpd.serve_forever()
