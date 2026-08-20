# Lumivo SmartLead AI

Lumivo için hazırlanmış Flask tabanlı lead toplama ve yapay zekâ sohbet MVP'si.
Lumivo, görme engelliler ve yakınları için akıllı gözlük üreten tek ürünlü
bir assistive-tech marka demosudur.

Canlı backend: `https://lumivo-vucs.onrender.com`

## Özellikler

- Ziyaretçi karşılama sayfası
- Yapay zekâ destekli sohbet API'si
- İsim, telefon, e-posta, ihtiyaç ve teslim tarihi ile lead kaydı
- Leadleri listeleyen yönetim paneli
- SQLite veritabanı
- Katmanlı mimari: config, database, services, routes
- Lumivo ürün özellikleri: kamera, sesli asistan, çevre/nesne tanıma, metin okuma, navigasyon ve telefon bağlantısı
- Tahmini teslim süresi: 1 hafta
- Wix Velo bağlantı kodları: `wix/`

## Kurulum

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python run.py
```

Tarayıcıda:

- `http://127.0.0.1:5000`
- `http://127.0.0.1:5000/dashboard`
- `http://127.0.0.1:5000/health`

## Ortam Değişkenleri

`.env` dosyası GitHub'a yüklenmez. Gerçek Groq cevabı için `GROQ_API_KEY` alanını doldurun.
Varsayılan Groq modeli `AI_MODEL=openai/gpt-oss-20b` olarak ayarlanmıştır.

## Render

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn run:app`
- Render blueprint: `render.yaml`
- Detaylı yönerge: `docs/render-deploy.md`

## Wix

Wix Velo kurulum adımları için `docs/wix-velo.md` dosyasını kullanın.
