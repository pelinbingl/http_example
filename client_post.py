import http.client

# Bağlantı aç
conn = http.client.HTTPConnection("localhost", 8080)

# Header tanımla
headers = {'Content-type': 'application/x-www-form-urlencoded'}

# POST verisi (burada student bilgisi var)
student_data = "student=pelin_bingol_211312082"

# POST isteği gönder
conn.request("POST", "/", student_data, headers)

# Yanıtı al ve yazdır
response = conn.getresponse()
print("Durum:", response.status)
print("Yanıt:", response.read().decode())

