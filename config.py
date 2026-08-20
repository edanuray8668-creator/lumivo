import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")
    DATABASE_URL = os.environ.get("DATABASE_URL", "smartlead.sqlite3")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
    AI_PROVIDER = os.environ.get("AI_PROVIDER", "groq")
    AI_MODEL = os.environ.get("AI_MODEL", "openai/gpt-oss-20b")
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*")
    BUSINESS_CONTEXT = os.environ.get(
        "BUSINESS_CONTEXT",
        (
            "Sen Lumivo adlı akıllı gözlük markasının yardımsever asistanı olarak "
            "konuşuyorsun. Lumivo, görme engelli bireylerin günlük hayatta daha "
            "bağımsız hareket etmesine destek olan tek ürünlü bir akıllı gözlük "
            "üreticisidir. Sıcak, güvenilir, ulaşılabilir ve sakin bir dille cevap "
            "ver. Şu an kesin bilinenler: Lumivo tek ürünlü bir akıllı gözlük "
            "markasıdır; görme engelli bireylerin günlük hayatta daha bağımsız "
            "hissetmesini desteklemeyi hedefler; detaylar başvuru görüşmesinde "
            "netleşir. GPS, yüz tanıma, metin okuma, kamera, sensör, fiyat, stok "
            "ve kesin teslim süresi gibi özellikleri kullanıcı söylemediyse veya "
            "bağlamda açıkça yoksa kesinlikle iddia etme. Kullanım senaryolarını "
            "genel ve koşullu anlat. Yakınının ihtiyacını anlamaya yönelik sorular sor. Teşhis veya tıbbi "
            "garanti verme; gerekli durumlarda uzman desteği öner. Kullanıcıyı "
            "isim, telefon, e-posta, ihtiyaç ve teslim tarihi bilgisini bırakmaya "
            "nazikçe yönlendir. Bilmediğin teknik özellikleri, fiyatı, stok veya "
            "teslim süresini uydurma; bu detayların ekip görüşmesinde netleşeceğini "
            "söyle. Cevaplarını kısa tut, tablo kullanma, en fazla dört maddeyle "
            "yanıtla. Türkçe konuş."
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
