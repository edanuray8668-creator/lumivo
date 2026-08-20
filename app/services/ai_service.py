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
                "Demo modu aktif. API anahtari eklenince gercek yapay zeka "
                "cevabi donecek. Projenizi anlatirsaniz size uygun tasarim "
                "hizmetine yonlendirebilirim."
            )

        try:
            return self._groq_yanit_uret(mesaj, gecmis or [])
        except requests.RequestException as exc:
            raise AIServiceError("Yapay zeka servisine ulasilamadi.") from exc

    def _groq_yanit_uret(self, mesaj, gecmis):
        messages = [{"role": "system", "content": self.sistem_talimati()}]
        messages.extend(gecmis)
        messages.append({"role": "user", "content": mesaj})

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {current_app.config['GROQ_API_KEY']}",
                "Content-Type": "application/json",
            },
            json={
                "model": "llama-3.1-8b-instant",
                "messages": messages,
                "temperature": 0.5,
            },
            timeout=20,
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]


ai_service = AIService()
