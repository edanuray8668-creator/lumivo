# Lumivo SmartLead AI

Lumivo için hazırlanmış Flask tabanlı lead toplama ve yapay zekâ sohbet MVP'si.
Lumivo, görme engelliler ve yakınları için akıllı gözlük üreten tek ürünlü
bir assistive-tech marka demosudur.

## Ozellikler

- Ziyaretci karşilama sayfasi
- Yapay zekâ destekli sohbet API'si
- İsim, telefon, e-posta, ihtiyaç ve teslim tarihi ile lead kaydı
- Leadleri listeleyen yönetim paneli
- SQLite veritabani
- Katmanli mimari: config, database, services, routes

## Kurulum

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python run.py
```

Tarayicida:

- `http://127.0.0.1:5000`
- `http://127.0.0.1:5000/dashboard`
- `http://127.0.0.1:5000/health`

## Ortam Degiskenleri

`.env` dosyası GitHub'a yüklenmez. Gerçek Groq cevabı için `GROQ_API_KEY` alanını doldurun.
Varsayılan Groq modeli `AI_MODEL=openai/gpt-oss-20b` olarak ayarlanmıştır.

## Render

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn run:app`
