# SmartLead AI

Studio Nova icin hazirlanmis Flask tabanli lead toplama ve yapay zeka sohbet MVP'si.

## Ozellikler

- Ziyaretci karşilama sayfasi
- Yapay zeka destekli sohbet API'si
- Isim, telefon ve mesaj ile lead kaydi
- Leadleri listeleyen yonetim paneli
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

`.env` dosyasi GitHub'a yuklenmez. Gercek Groq cevabi icin `GROQ_API_KEY` alanini doldurun.

## Render

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn run:app`
