import { fetch } from "wix-fetch";

const API_BASE_URL = "https://lumivo-vucs.onrender.com";

$w.onReady(function () {
  $w("#answerText").text = "Merhaba. Lumivo hakkında merak ettiklerini yazabilirsin.";

  $w("#askButton").onClick(async () => {
    const mesaj = $w("#messageInput").value.trim();

    if (!mesaj) {
      $w("#answerText").text = "Lütfen önce sorunuzu veya ihtiyacınızı yazın.";
      return;
    }

    $w("#answerText").text = "Lumivo Asistanı yanıt hazırlıyor...";

    try {
      const response = await fetch(`${API_BASE_URL}/api/sohbet`, {
        method: "post",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mesaj })
      });
      const data = await response.json();
      $w("#answerText").text = data.basari ? data.cevap : data.hata;
    } catch (error) {
      $w("#answerText").text = "Asistana şu anda ulaşılamıyor. Lütfen tekrar deneyin.";
    }
  });

  $w("#saveLeadButton").onClick(async () => {
    const payload = {
      isim: $w("#nameInput").value.trim(),
      telefon: $w("#phoneInput").value.trim(),
      email: $w("#emailInput").value.trim(),
      ihtiyac: $w("#needInput").value.trim(),
      teslim_tarihi: formatDate($w("#deliveryDatePicker").value)
    };

    if (!payload.isim || !payload.telefon || !payload.email || !payload.ihtiyac) {
      $w("#formStatusText").text = "İsim, telefon, e-posta ve ihtiyaç bilgisi zorunludur.";
      return;
    }

    $w("#formStatusText").text = "Başvuru gönderiliyor...";

    try {
      const response = await fetch(`${API_BASE_URL}/api/leads`, {
        method: "post",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      const data = await response.json();
      $w("#formStatusText").text = data.basari
        ? "Başvuru bilgileriniz alındı. Lumivo ekibi sizinle iletişime geçecek."
        : data.hata;
    } catch (error) {
      $w("#formStatusText").text = "Başvuru gönderilemedi. Lütfen tekrar deneyin.";
    }
  });
});

function formatDate(value) {
  if (!value) return "";
  return value.toISOString().slice(0, 10);
}
