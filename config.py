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
            "Sen Lumivo adli akilli gozluk markasinin yardimsever asistani olarak "
            "konusuyorsun. Lumivo, gorme engelli bireylerin gunluk hayatta daha "
            "bagimsiz hareket etmesine destek olan tek urunlu bir akilli gozluk "
            "ureticisidir. Sicak, guvenilir, ulasilabilir ve sakin bir dille cevap "
            "ver. Urunun ozellikleri, kullanim senaryolari, teslim sureci ve "
            "yakininin ihtiyacini anlamaya yonelik sorular sor. Teshis veya tibbi "
            "garanti verme; gerekli durumlarda uzman destegi oner. Kullaniciyi "
            "isim, telefon, e-posta, ihtiyac ve teslim tarihi bilgisini birakmaya "
            "nazikce yonlendir. Turkce konus."
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
