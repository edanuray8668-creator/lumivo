# Render Yayınlama

Bu doküman PDF'teki Modül H için Lumivo backend'ini Render'da yayına alma adımlarını açıklar.

## 1. GitHub Repo

Kod GitHub'a gönderildi:

```text
https://github.com/edanuray8668-creator/lumivo
```

## 2. Render Web Service

Render panelinde:

1. `New +` seç.
2. `Web Service` seç.
3. GitHub hesabını bağla.
4. `edanuray8668-creator/lumivo` reposunu seç.

Render `render.yaml` dosyasını görürse Blueprint olarak da kurulum önerebilir. Manuel kurulumda şu değerleri kullan:

```text
Name: lumivo
Runtime: Python
Build Command: pip install -r requirements.txt
Start Command: gunicorn run:app
```

## 3. Environment Variables

Render > Environment bölümünde şu değişkenleri ekle:

```text
FLASK_ENV=production
AI_PROVIDER=groq
AI_MODEL=openai/gpt-oss-20b
CORS_ORIGINS=*
```

`SECRET_KEY` için Render'ın otomatik ürettiği güvenli değer kullanılabilir.

`GROQ_API_KEY` değerini Render paneline gizli olarak ekle. Bu değer GitHub'a yazılmamalı.

## 4. Kontrol

Deploy tamamlanınca Render URL'sinde şu adresi aç:

```text
https://YOUR-RENDER-APP.onrender.com/health
```

Beklenen cevap:

```json
{
  "basari": true,
  "durum": "aktif"
}
```

## 5. Wix Güncellemesi

Render URL'si belli olunca şu dosyalardaki `API_BASE_URL` değerini değiştir:

- `wix/home-page.js`
- `wix/dashboard-page.js`

Örnek:

```js
const API_BASE_URL = "https://lumivo.onrender.com";
```
