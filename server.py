"""
SHORT RADAR — Binance Proxy Server
"""
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

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
    port = int(os.environ.get('PORT', 8888))
    print(f"✅ SHORT RADAR proxy başlatıldı → http://localhost:{port}")
    app.run(host='0.0.0.0', port=port, debug=False)
