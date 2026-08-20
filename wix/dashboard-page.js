import { fetch } from "wix-fetch";

const API_BASE_URL = "https://YOUR-RENDER-APP.onrender.com";

$w.onReady(function () {
  loadLeads();
});

async function loadLeads() {
  $w("#dashboardStatusText").text = "Başvurular yükleniyor...";

  try {
    const response = await fetch(`${API_BASE_URL}/api/leads`);
    const data = await response.json();

    if (!data.basari || data.leads.length === 0) {
      $w("#dashboardStatusText").text = "Henüz başvuru kaydı yok.";
      $w("#leadsRepeater").data = [];
      return;
    }

    $w("#dashboardStatusText").text = `${data.leads.length} başvuru bulundu.`;
    $w("#leadsRepeater").data = data.leads.map((lead) => ({
      _id: String(lead.id),
      isim: lead.isim,
      telefon: lead.telefon,
      email: lead.email || "-",
      ihtiyac: lead.ihtiyac || "-",
      teslim_tarihi: lead.teslim_tarihi || "-",
      tarih: lead.tarih
    }));

    $w("#leadsRepeater").onItemReady(($item, itemData) => {
      $item("#leadNameText").text = itemData.isim;
      $item("#leadPhoneText").text = itemData.telefon;
      $item("#leadEmailText").text = itemData.email;
      $item("#leadNeedText").text = itemData.ihtiyac;
      $item("#leadDeliveryText").text = itemData.teslim_tarihi;
      $item("#leadDateText").text = itemData.tarih;
    });
  } catch (error) {
    $w("#dashboardStatusText").text = "Başvurular alınamadı. Lütfen tekrar deneyin.";
  }
}
