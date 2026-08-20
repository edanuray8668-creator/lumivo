import requests
from flask import current_app


class AIServiceError(Exception):
    pass


class AIService:
    def sistem_talimati(self):
        return current_app.config["BUSINESS_CONTEXT"]

    def yanit_uret(self, mesaj, gecmis=None):
        if not current_app.config["GROQ_API_KEY"]:
            return (
                "Demo modu aktif. API anahtarı eklenince gerçek Lumivo asistanı "
                "cevabı dönecek. İhtiyacınızı kısaca paylaşırsanız akıllı gözlük "
                "hakkında ön bilgi ve başvuru süreci için yardımcı olabilirim."
            )

        try:
            return self._groq_yanit_uret(mesaj, gecmis or [])
        except requests.RequestException as exc:
            raise AIServiceError("Yapay zekâ servisine ulaşılamadı.") from exc

    def _groq_yanit_uret(self, mesaj, gecmis):
        messages = [
            {"role": "system", "content": self.sistem_talimati()},
            {
                "role": "system",
                "content": (
                    "Lumivo'nun doğrulanmış özellikleri kamera, sesli asistan, çevre "
                    "ve nesne tanıma, metin okuma, navigasyon/yönlendirme ve telefon "
                    "bağlantısıdır. Tahmini teslim süresi 1 haftadır. Fiyat, stok, "
                    "tıbbi tedavi veya kesin sonuç vaadi verme."
                ),
            },
        ]
        messages.extend(gecmis)
        messages.append({"role": "user", "content": mesaj})

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {current_app.config['GROQ_API_KEY']}",
                "Content-Type": "application/json",
            },
            json={
                "model": current_app.config["AI_MODEL"],
                "messages": messages,
                "temperature": 0.5,
            },
            timeout=20,
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]


ai_service = AIService()
