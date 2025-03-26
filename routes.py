from flask import Blueprint, request, jsonify
from utils import fetch_places_from_kakao

bp = Blueprint("recommendation", __name__)

@bp.route("/recommend", methods=["GET"])
def recommend():
    try:
        lat = float(request.args.get("lat", "").strip())
        lng = float(request.args.get("lng", "").strip())
    except (TypeError, ValueError):
        return jsonify({"error": "위도/경도 값이 유효하지 않습니다."}), 400

    try:
        places = fetch_places_from_kakao(lat, lng)
        return jsonify({"places": places})
    except Exception as e:
        return jsonify({"error": str(e)}), 500