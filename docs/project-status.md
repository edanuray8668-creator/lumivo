# Lumivo SmartLead AI - Proje Durumu

Bu dosya bir sonraki oturumda projeye kaldığımız yerden devam etmek için hazırlanmıştır. PDF yönergesi kaynak alınmıştır: `SmartLead_AI_Proje_Yonergesi.pdf`.

## Proje Özeti

SmartLead AI, görme engelliler ve yakınları için akıllı gözlük üreten Lumivo markasına uyarlanmış bir lead toplama ve yapay zekâ sohbet projesidir.

Ürün bilgileri:

- Marka adı: Lumivo
- Slogan: Yol senin, destek Lumivo.
- Hedef kitle: Görme engelliler ve yakınları
- Ürün: Tek ürünlü akıllı gözlük
- Özellikler: kamera, sesli asistan, çevre ve nesne tanıma, metin okuma, navigasyon/yönlendirme, telefon bağlantısı
- Tahmini teslim süresi: 1 hafta
- Ton: güvenilir, ulaşılabilir, sıcak, yardımsever

## Önemli Linkler

- GitHub repo: `https://github.com/edanuray8668-creator/lumivo`
- Canlı Render backend: `https://lumivo-vucs.onrender.com`
- Health check: `https://lumivo-vucs.onrender.com/health`
- Yerel proje klasörü: `/Users/cankarabulut/smartlead_ai`
- PDF yönergesi: `/Users/cankarabulut/Downloads/SmartLead_AI_Proje_Yonergesi.pdf`

## Güvenlik Notları

- `.env` dosyası GitHub'a gönderilmez.
- `GROQ_API_KEY` yalnızca yerel `.env` ve Render Environment Variables içinde tutulmalı.
- GitHub tokenları commit edilmedi ve remote URL'e kaydedilmedi.
- Daha önce paylaşılmış GitHub PAT tokenları GitHub üzerinden revoke edilmelidir.
- Commit author/committer bilgileri düzeltilmiştir ve artık `edanuray8668-creator <edanuray8668-creator@users.noreply.github.com>` olarak görünür.

## PDF İsterlerine Göre Yapılanlar

### 1. Projenin Amacı ve Kişiselleştirme

Tamamlandı.

- SmartLead AI iskeleti Lumivo markasına uyarlandı.
- `BUSINESS_CONTEXT` Lumivo asistanına göre yazıldı.
- Arayüz metinleri Lumivo markasına göre düzenlendi.
- Türkçe karakterler düzeltildi.

### 2. Genel Kurallar

Tamamlandı.

- Modüler yapı kuruldu.
- `.env` GitHub'a gönderilmiyor.
- `.gitignore` hazır.
- API anahtarları kod içine yazılmadı.
- SQL sadece `app/database.py` içinde.
- AI çağrısı sadece `app/services/ai_service.py` içinde.
- API hataları JSON olarak dönüyor.
- SQL sorgularında `?` placeholder kullanılıyor.

### 3. Hedef Mimari

Tamamlandı.

Mevcut yapı:

```text
smartlead_ai/
├── run.py
├── config.py
├── requirements.txt
├── render.yaml
├── .env.example
├── .gitignore
├── README.md
├── docs/
│   ├── project-status.md
│   ├── render-deploy.md
│   └── wix-velo.md
├── wix/
│   ├── home-page.js
│   └── dashboard-page.js
└── app/
    ├── __init__.py
    ├── database.py
    ├── routes.py
    ├── templates/
    │   ├── index.html
    │   └── dashboard.html
    └── services/
        ├── __init__.py
        └── ai_service.py
```

Not: PDF'te istenen mimari korunmuştur. Ek olarak `docs/`, `wix/` ve `render.yaml` dosyaları yayın ve Wix bağlantısı için eklenmiştir.

### 4. Oturum Öncesi Hazırlık

Tamamlandı.

- Python sanal ortamı oluşturuldu: `venv`
- Bağımlılıklar kuruldu.
- Git deposu başlatıldı.
- GitHub repo oluşturuldu ve push edildi.
- Groq API key yerel `.env` ve Render tarafında kullanılacak şekilde yapılandırıldı.

### Modül A - Yapılandırma

Tamamlandı.

Dosya: `config.py`

İçerik:

- `Config`
- `DevelopmentConfig`
- `ProductionConfig`
- `SECRET_KEY`
- `DATABASE_URL`
- `GROQ_API_KEY`
- `AI_PROVIDER`
- `AI_MODEL`
- `CORS_ORIGINS`
- `BUSINESS_CONTEXT`

Varsayılan AI modeli:

```text
openai/gpt-oss-20b
```

PDF'teki `llama-3.1-8b-instant` modeli Groq tarafında erişilebilir olmadığı için güncel çalışan model kullanılmıştır.

### Modül B - Veritabanı

Tamamlandı.

Dosya: `app/database.py`

Fonksiyonlar:

- `get_db()`
- `init_db(app)`
- `lead_ekle(...)`
- `tum_leadler()`

Tablo: `leads`

Alanlar:

- `id`
- `isim`
- `telefon`
- `email`
- `ihtiyac`
- `teslim_tarihi`
- `tarih`

Not: İlk testlerden kalan eski SQLite verileri local dosyada olabilir; `smartlead.sqlite3` GitHub'a gönderilmez.

### Modül C - Yapay Zekâ Servisi

Tamamlandı.

Dosya: `app/services/ai_service.py`

İçerik:

- `AIService`
- `AIServiceError`
- `yanit_uret(mesaj, gecmis)`
- Groq chat completions çağrısı
- API key yoksa demo modu

Canlı Render ortamında gerçek Groq cevabı test edildi.

### Modül D - Rotalar

Tamamlandı.

Dosya: `app/routes.py`

Endpointler:

- `GET /`
- `GET /dashboard`
- `POST /api/sohbet`
- `POST /api/leads`
- `GET /api/leads`

Kurallar:

- API cevapları `basari` alanı içeriyor.
- Eksik veri için 400 dönüyor.
- AI servis hatası için 503 dönüyor.
- Yeni lead için 201 dönüyor.

### Modül E - Fabrika ve Giriş

Tamamlandı.

Dosyalar:

- `app/__init__.py`
- `run.py`

İçerik:

- `create_app()`
- CORS ayarı
- DB init
- Blueprint kayıtları
- `GET /health`

Render import hatası için ayrıca `app/__init__.py` içinde şu export eklendi:

```python
app = create_app()
```

Bu nedenle hem `gunicorn run:app` hem `gunicorn app:app` çalışır.

### Modül F - Çalıştırma ve Test

Tamamlandı.

Yerel testler:

- `/health` çalıştı.
- `/api/sohbet` demo ve gerçek Groq ile test edildi.
- `/api/leads` POST kayıt aldı.
- `/api/leads` GET kayıt listeledi.
- `/` ve `/dashboard` 200 döndü.

Canlı testler:

- `https://lumivo-vucs.onrender.com/health` 200 döndü.
- Canlı ana sayfa açıldı.
- Canlı lead kaydı 201 döndü.
- Canlı AI sohbeti gerçek cevap döndürdü.

### Modül G - Frontend ve Wix Bağlantısı

Kısmen tamamlandı.

Hazırlanan dosyalar:

- `docs/wix-velo.md`
- `wix/home-page.js`
- `wix/dashboard-page.js`

Durum:

- Wix Velo kodları hazır.
- Kodlardaki `API_BASE_URL` canlı Render adresine güncellendi:

```js
const API_BASE_URL = "https://lumivo-vucs.onrender.com";
```

Kalan:

- Wix editörde Velo açılacak.
- Ana sayfa elementleri oluşturulacak.
- Panel sayfası ve Repeater oluşturulacak.
- `wix/home-page.js` ana sayfa Page Code alanına yapıştırılacak.
- `wix/dashboard-page.js` panel sayfası Page Code alanına yapıştırılacak.
- Wix Preview ve canlı test yapılacak.

Ana sayfa Wix element ID'leri:

```text
#messageInput
#askButton
#answerText
#nameInput
#phoneInput
#emailInput
#needInput
#deliveryDatePicker
#saveLeadButton
#formStatusText
```

Panel Wix element ID'leri:

```text
#dashboardStatusText
#leadsRepeater
#leadNameText
#leadPhoneText
#leadEmailText
#leadNeedText
#leadDeliveryText
#leadDateText
```

Detaylar için: `docs/wix-velo.md`

### Modül H - GitHub + Render

Büyük ölçüde tamamlandı.

Tamamlanan:

- GitHub repo oluşturuldu.
- Kod GitHub'a push edildi.
- Commit author bilgileri `edanuray8668-creator` olarak düzeltildi.
- Render deploy yapıldı.
- Render import hatası düzeltildi.
- Canlı backend çalışıyor.

Kalan:

- Render URL'i Wix'e bağlandı ama Wix sitesinde henüz uygulanmadı.
- Wix canlı site bağlantısı henüz teslim seviyesinde hazır değil.
- README son teslim öncesi gözden geçirilmeli.
- Kısa demo/sunum metni hazırlanmalı.

## Son Git Durumu

Son bilinen başarılı commit:

```text
dbeba21 Point Wix integration to Render backend
```

Bu dosya eklendikten sonra yeni bir commit oluşacaktır.

GitHub `main` branch author bilgileri `edanuray8668-creator` olarak düzeltilmiştir.

## Bir Sonraki Oturumda Yapılacaklar

1. GitHub ve Render durumunu hızlı kontrol et:

```bash
cd /Users/cankarabulut/smartlead_ai
git status --short
git log --format='%h %an <%ae> | %s' -5
curl -s https://lumivo-vucs.onrender.com/health
```

2. Wix tarafına geç:

- Wix Velo aç.
- `docs/wix-velo.md` dosyasındaki ID listesine göre ana sayfa elementlerini oluştur.
- `wix/home-page.js` kodunu ana sayfaya yapıştır.
- Başvuru paneli sayfasını oluştur.
- Repeater ve text elementlerini ID listesine göre ayarla.
- `wix/dashboard-page.js` kodunu panel sayfasına yapıştır.

3. Wix Preview testleri:

- Asistana soru sor.
- Başvuru formunu doldur.
- Panelde başvurunun göründüğünü kontrol et.

4. Wix canlı yayın:

- Wix siteyi publish et.
- Yayınlanan Wix site URL'ini README veya teslim notlarına ekle.

5. Son teslim hazırlığı:

- README'yi son hale getir.
- GitHub repo bağlantısını teslim et.
- Render canlı backend bağlantısını teslim et.
- Wix canlı site bağlantısını teslim et.
- Kısa demo/sunum metni hazırla.

## Teslim Edilecekler Durumu

- GitHub deposu: tamamlandı
- Canlı Render backend: tamamlandı
- Wix site bağlantısı: bekliyor
- Kısa README: mevcut, son kontrol bekliyor
- Kısa sunum/demo: bekliyor

## Kullanılacak Komutlar

Yerel sunucu:

```bash
cd /Users/cankarabulut/smartlead_ai
source venv/bin/activate
python run.py
```

Health:

```bash
curl -s http://127.0.0.1:5000/health
curl -s https://lumivo-vucs.onrender.com/health
```

Git push için dikkat:

- Commit author `edanuray8668-creator` kalmalı.
- `.env` GitHub'a eklenmemeli.
- Tokenlar dosyaya veya remote URL'e kaydedilmemeli.
