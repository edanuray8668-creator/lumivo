import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")
    DATABASE_URL = os.environ.get("DATABASE_URL", "smartlead.sqlite3")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
    AI_PROVIDER = os.environ.get("AI_PROVIDER", "groq")
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*")
    BUSINESS_CONTEXT = os.environ.get(
        "BUSINESS_CONTEXT",
        (
            "Sen Studio Nova adli grafik tasarim studyosunun asistani olarak "
            "konusuyorsun. Logo tasarimi, sosyal medya gorselleri, marka kimligi "
            "ve baski tasarimi hakkinda kisa, net ve yardimci cevaplar ver. "
            "Kullaniciyi proje detaylarini paylasmaya ve iletisim bilgisi "
            "birakmaya nazikce yonlendir. Turkce konus."
        ),
    )


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
