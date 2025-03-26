import requests
import os
from config import KAKAO_API_KEY_REST  # .env에서 키를 불러올 수 있게 되어 있어야 함

def fetch_places_from_kakao(lat, lng):
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
        res = requests.get(url, headers=headers, params=params)

        print(f"📡 요청: {label} | 좌표: ({lat}, {lng}) | status: {res.status_code}")
        if res.status_code == 200:
            documents = res.json().get("documents", [])
            print(f"📦 {label} 결과 개수: {len(documents)}")
            names = [place["place_name"] for place in documents[:5]]
            results[label] = names if names else ["없음"]
        else:
            print(f"❌ Kakao 요청 실패: {res.text}")
            results[label] = ["없음"]

    return results