from http.server import BaseHTTPRequestHandler, HTTPServer
import base64

class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. Basic Auth kontrolü
        auth_header = self.headers.get('Authorization')
        if not auth_header or not auth_header.startswith("Basic "):
            self.send_response(401)
            self.send_header("WWW-Authenticate", "Basic realm=\"Erişim için giriş yapınız\"")
            self.end_headers()
            self.wfile.write(b"401 Unauthorized - Kimlik bilgisi eksik")
            return

        # 2. Kullanıcı adı ve şifre kontrolü
        encoded_credentials = auth_header.split(" ")[1]
        decoded_credentials = base64.b64decode(encoded_credentials).decode()
        username, password = decoded_credentials.split(":")

        if username != "pelinbingol" or password != "1234":
            self.send_response(401)
            self.end_headers()
            self.wfile.write(b"401 Unauthorized - Hatali kullanici adi veya sifre")
            return

        # 3. POST verisini al
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode()

        # 4. "student" kontrolü
        if "student" in post_data:
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"200 OK - student info received")
        else:
            self.send_response(400)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"400 Bad Request - invalid input")

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8080), MyServer)
    print("Server çalışıyor (port 8080) - Basic Auth kontrolüyle")
    server.serve_forever()
