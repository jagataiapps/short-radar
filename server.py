"""
SHORT RADAR — Binance Proxy Server
Kullanım:
  pip install flask flask-cors requests
  python server.py
Sonra tarayıcıda crypto-short-radar.html dosyasını aç.
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Tüm origins'e izin ver

BINANCE = "https://fapi.binance.com"

@app.route("/api/ticker")
def ticker():
    r = requests.get(f"{BINANCE}/fapi/v1/ticker/24hr", timeout=10)
    return jsonify(r.json())

@app.route("/api/klines")
def klines():
    symbol   = request.args.get("symbol")
    interval = request.args.get("interval", "15m")
    limit    = request.args.get("limit", "30")
    r = requests.get(
        f"{BINANCE}/fapi/v1/klines",
        params={"symbol": symbol, "interval": interval, "limit": limit},
        timeout=10
    )
    return jsonify(r.json())

@app.route("/api/exchangeinfo")
def exchangeinfo():
    r = requests.get(f"{BINANCE}/fapi/v1/exchangeInfo", timeout=15)
    return jsonify(r.json())

if __name__ == "__main__":
    print("✅ SHORT RADAR proxy başlatıldı → http://localhost:5000")
    print("   Şimdi crypto-short-radar.html dosyasını tarayıcıda aç")
    app.run(port=8888, debug=False)
