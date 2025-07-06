import http.client

conn = http.client.HTTPConnection("localhost", 8000)
conn.request("GET", "/")
response = conn.getresponse()

print("Durum Kodu:", response.status)
print("Yanıt:", response.read().decode())