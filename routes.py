from flask import Blueprint, request, jsonify
from utils import fetch_places_from_kakao

bp = Blueprint("recommendation", __name__)

@bp.route("/recommend", methods=["GET"])
def recommend():
    lat = request.args.get("lat")
    lng = request.args.get("lng")

    if not lat or not lng:
        return jsonify({"error": "위도/경도가 없습니다."}), 400

    try:
        places = fetch_places_from_kakao(lat, lng)
        return jsonify({"places": places})
    except Exception as e:
        return jsonify({"error": str(e)}), 500