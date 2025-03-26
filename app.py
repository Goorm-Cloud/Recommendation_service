import os
from flask import Flask
from flask_cors import CORS
from routes import bp
from dotenv import load_dotenv

load_dotenv(dotenv_path="/app/.env")

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.secret_key = os.urandom(24)
    CORS(app)

    # 환경변수 확인 예시
    if not os.getenv("KAKAO_API_KEY_REST"):
        raise ValueError("❌ KAKAO_API_KEY_REST가 설정되지 않았습니다!")

    # 블루프린트 등록
    app.register_blueprint(bp)

    return app

# WSGI용 앱 객체 생성
app = create_app()