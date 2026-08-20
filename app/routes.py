from flask import Blueprint, jsonify, render_template, request

from app.database import lead_ekle, tum_leadler
from app.services.ai_service import AIServiceError, ai_service


page_bp = Blueprint("pages", __name__)
api_bp = Blueprint("api", __name__)


@page_bp.get("/")
def index():
    return render_template("index.html")


@page_bp.get("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@api_bp.post("/sohbet")
def sohbet():
    data = request.get_json(silent=True) or {}
    mesaj = (data.get("mesaj") or "").strip()
    gecmis = data.get("gecmis") or []

    if not mesaj:
        return jsonify({"basari": False, "hata": "Mesaj zorunludur."}), 400

    try:
        cevap = ai_service.yanit_uret(mesaj, gecmis)
    except AIServiceError:
        return (
            jsonify(
                {
                    "basari": False,
                    "hata": "Asistan su anda yanit veremiyor. Lutfen tekrar deneyin.",
                }
            ),
            503,
        )

    return jsonify({"basari": True, "cevap": cevap})


@api_bp.post("/leads")
def lead_kaydet():
    data = request.get_json(silent=True) or {}
    isim = (data.get("isim") or "").strip()
    telefon = (data.get("telefon") or "").strip()
    email = (data.get("email") or "").strip()
    ihtiyac = (data.get("ihtiyac") or "").strip()
    teslim_tarihi = (data.get("teslim_tarihi") or "").strip()

    if not isim or not telefon or not email or not ihtiyac:
        return (
            jsonify(
                {
                    "basari": False,
                    "hata": "Isim, telefon, e-posta ve ihtiyac bilgisi zorunludur.",
                }
            ),
            400,
        )

    yeni_id = lead_ekle(isim, telefon, email, ihtiyac, teslim_tarihi)
    return jsonify({"basari": True, "id": yeni_id}), 201


@api_bp.get("/leads")
def leadleri_getir():
    return jsonify({"basari": True, "leads": tum_leadler()})
