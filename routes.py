from flask import Blueprint, request, jsonify
from utils import fetch_places_from_kakao

bp = Blueprint("recommendation", __name__)

@bp.route("/recommend", methods=["GET"])
def recommend():
    raw_lat = request.args.get("lat")
    raw_lng = request.args.get("lng")

    print(f"💬 받은 쿼리 파라미터: lat={raw_lat}, lng={raw_lng}")

    try:
        lat = float(raw_lat.strip())
        lng = float(raw_lng.strip())
    except (TypeError, ValueError, AttributeError):
        return jsonify({"error": "위도/경도 값이 유효하지 않습니다."}), 400

    try:
        places = fetch_places_from_kakao(lat, lng)
        return jsonify({"places": places})
    except Exception as e:
        return jsonify({"error": str(e)}), 500