import requests
import os
from dotenv import load_dotenv

print("🔧 [utils.py] dotenv 로드 시작")
load_dotenv(dotenv_path="/app/.env")

KAKAO_API_KEY_REST = os.getenv("KAKAO_API_KEY_REST")
print("🔍 [utils.py] KAKAO_API_KEY_REST =", KAKAO_API_KEY_REST)

def fetch_places_from_kakao(lat, lng):
    print(f"📍 [utils.py] fetch_places_from_kakao 호출: lat={lat}, lng={lng}")

    headers = {
        "Authorization": f"KakaoAK {KAKAO_API_KEY_REST}",
        "Host": "dapi.kakao.com",
        "Referer": "https://developers.kakao.com",
        "Origin": "https://developers.kakao.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/91.0.4472.124 Safari/537.36",
        "KA": "sdk/1.0 os/python lang/ko-KR device/pc"
    }

    categories = {
        "카페": "CE7",
        "음식점": "FD6",
        "관광명소": "AT4"
    }

    results = {}

    for label, code in categories.items():
        url = "https://dapi.kakao.com/v2/local/search/category.json"
        params = {
            "category_group_code": code,
            "x": lng,
            "y": lat,
            "radius": 1500,
            "sort": "distance"
        }

        print(f"📡 [utils.py] 카카오 요청: {label} - {params}")
        res = requests.get(url, headers=headers, params=params)
        print(f"📡 [utils.py] status_code: {res.status_code}, text: {res.text[:200]}...")  # 너무 길면 자름

        if res.status_code == 200:
            documents = res.json().get("documents", [])
            print(f"📦 {label} 결과 개수: {len(documents)}")
            names = [place["place_name"] for place in documents[:5]]
            results[label] = names if names else ["없음"]
        else:
            results[label] = ["없음"]

    return results