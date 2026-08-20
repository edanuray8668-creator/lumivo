# Wix Velo Bağlantısı

Bu doküman, PDF'teki Modül G için Lumivo Wix arayüzünü Flask API'ye bağlama adımlarını açıklar.

## 1. Backend Adresi

Render yayını yapılana kadar yerel adres yalnızca bilgisayarında çalışır:

```text
http://127.0.0.1:5000
```

Wix canlı site, yerel bilgisayarındaki bu adrese erişemez. Render sonrası `API_BASE_URL` şu formatta değiştirilecek:

```js
const API_BASE_URL = "https://YOUR-RENDER-APP.onrender.com";
```

Lumivo için güncel canlı API adresi:

```js
const API_BASE_URL = "https://lumivo-vucs.onrender.com";
```

## 2. Karşılama Sayfası Element ID'leri

Wix ana sayfasında şu elementleri oluştur ve ID'lerini birebir böyle ayarla:

| Element | Wix ID |
| --- | --- |
| Soru metin kutusu | `#messageInput` |
| Asistana sor butonu | `#askButton` |
| AI cevap metni | `#answerText` |
| İsim input | `#nameInput` |
| Telefon input | `#phoneInput` |
| E-posta input | `#emailInput` |
| İhtiyaç metin kutusu | `#needInput` |
| Teslim tarihi date picker | `#deliveryDatePicker` |
| Başvuru gönder butonu | `#saveLeadButton` |
| Form durum metni | `#formStatusText` |

Sayfa kodu: [`wix/home-page.js`](../wix/home-page.js)

## 3. Yönetim Paneli Element ID'leri

Wix panel sayfasında bir Repeater oluştur. Repeater ve içindeki text element ID'leri:

| Element | Wix ID |
| --- | --- |
| Repeater | `#leadsRepeater` |
| Durum metni | `#dashboardStatusText` |
| İsim text | `#leadNameText` |
| Telefon text | `#leadPhoneText` |
| E-posta text | `#leadEmailText` |
| İhtiyaç text | `#leadNeedText` |
| Teslim tarihi text | `#leadDeliveryText` |
| Kayıt tarihi text | `#leadDateText` |

Sayfa kodu: [`wix/dashboard-page.js`](../wix/dashboard-page.js)

## 4. API Sözleşmesi

Sohbet:

```http
POST /api/sohbet
Content-Type: application/json
```

```json
{
  "mesaj": "Lumivo annem için uygun mu?"
}
```

Başvuru kaydı:

```http
POST /api/leads
Content-Type: application/json
```

```json
{
  "isim": "Ayşe Yılmaz",
  "telefon": "05551112233",
  "email": "ayse@example.com",
  "ihtiyac": "Annem için dışarıda yön bulma desteği arıyoruz.",
  "teslim_tarihi": "2026-09-10"
}
```

Başvuru listesi:

```http
GET /api/leads
```

## 5. Wix'te Kontrol Listesi

- Velo aktif.
- Element ID'leri bu dokümandakiyle birebir aynı.
- `API_BASE_URL` Render adresiyle değiştirildi.
- Render üzerinde `CORS_ORIGINS=*` veya Wix domain'i izinli.
- Ana sayfada sohbet çalışıyor.
- Form gönderimi sonrası panelde kayıt görünüyor.
