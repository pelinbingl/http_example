import http.client
import base64

# Kullanıcı adı ve şifre
username = "pelinbingol"
password = "1234"

# Kullanıcı bilgilerini base64 ile encode et
credentials = f"{username}:{password}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

# Header oluştur
headers = {
    'Authorization': f'Basic {encoded_credentials}',
    'Content-type': 'application/x-www-form-urlencoded'
}

# Veri
student_data = "student=pelin_bingol_211312082"

# Bağlantı
conn = http.client.HTTPConnection("localhost", 8080)
conn.request("POST", "/", student_data, headers)

# Yanıtı al ve yazdır
response = conn.getresponse()
print("Durum:", response.status)
print("Yanıt:", response.read().decode())