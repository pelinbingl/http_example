# IoT Kimlik Doğrulama Mekanizmaları (HTTP / TLS / Mutual Auth)

📅 **Tarih:** 26.06.2025  
👨‍💻 **Hazırlayan:** Pelin Bingöl
🎓 **Öğrenci No:** 211312082

---

## 📌 Ödev Kapsamı

Bu proje, IoT (Nesnelerin İnterneti) cihazlarının kimlik doğrulama süreçlerini aşağıdaki başlıklar altında simüle etmektedir:

1. **HTTP Basic Authentication (Temel Kimlik Doğrulama)**
2. **TLS ile Güvenli İletişim**
3. **Karşılıklı TLS (Mutual TLS) ile Kimlik Doğrulama**
4. **Sertifika Tabanlı Doğrulama**
5. **Wireshark ile Trafik İncelemesi**

---

# ✅ Gerçekleştirilen Görevler

## 🔹 A. HTTP Bağlantısı (Basic Authentication)
- ✔️ http.server ve requests kullanılarak istemci/sunucu yapısı kuruldu
- ✔️ Kullanıcı adı/parola ile temel kimlik doğrulama desteği eklendi
- ✔️ Authorization: Basic base64(user:pass) başlığı kontrol edildi
- ✔️ Yanıt kodları doğru olarak döndürüldü (200 OK, 401 Unauthorized)

## 🔹 B. POST Mesaj İşleme
- ✔️ Sunucu, aşağıdaki JSON verisi ile gelen POST isteğini işler.

- ✔️ Geçerli veriler için 200 OK döner

- ❌ Eksik ya da hatalı veriler için hata mesajı döner


## 🔹 C. TLS Tabanlı Kimlik Doğrulama (Tek Taraflı)
- ✔️ Sunucu, kendinden imzalı TLS sertifikası ile yapılandırıldı

- ✔️ İstemci, sertifikadaki Common Name (CN) bilgisini doğruladı

- ✔️ Kullanılan SSL versiyonu: TLSv1.3

- ✔️ Tüm işlem Wireshark ile analiz edildi

## 🔹 D. Karşılıklı TLS (Mutual Authentication)
- ✔️ Hem istemci hem sunucu için CA tarafından imzalanmış sertifikalar üretildi

- ✔️ İstemcinin sertifikası sunucu tarafından doğrulandı

- ✔️ Sertifika süresi, doğruluk kontrolü ve UID eşleştirme işlemleri gerçekleştirildi

- ✔️ device_id ↔️ certificate UID eşlemesi yapıldı

## 🧪 Kullanılan Araçlar
- Python 3.11+

- http.server, requests, ssl, socket

- OpenSSL (sertifika üretimi için)

- Wireshark (ağ trafiği inceleme için)

## 📥 Wireshark Çıktısı
- TLS el sıkışma (handshake) süreci wireshark_output/ klasöründe .pcapng dosyası olarak sunulmuştur.

## 🔐 Güvenlik Önlemleri
- Parolalar SHA-256 algoritması ve salt ile hash'lendi

- Hiçbir yerde düz metin (plain text) parola saklanmadı

- Sertifika geçerlilik ve süresi kontrol edildi

- PKI hiyerarşisi (CA Root → Sertifikalar) kurallarına uygun yapı
