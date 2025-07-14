from flask import Flask, request, jsonify, render_template, send_from_directory
from datetime import datetime
import os

app = Flask(__name__, static_url_path='/static')

# 🔸 Sample "risky" areas — you can replace with real data or an ML model
risk_zones = [
    {"lat": 9.0457, "lon": 7.4951, "message": "⚠️ High-risk zone (Abuja Central)"},
    {"lat": 6.5244, "lon": 3.3792, "message": "⚠️ Pickpocket hotspot (Lagos Island)"}
]

# 🔹 Serve the main web app
@app.route('/')
def index():
    return render_template('index.html')

# 🔹 Handle risk analysis
@app.route('/check_risk', methods=['POST'])
def check_risk():
    data = request.get_json()
    lat = data.get('latitude')
    lon = data.get('longitude')

    for zone in risk_zones:
        if abs(zone['lat'] - lat) < 0.01 and abs(zone['lon'] - lon) < 0.01:
            return jsonify({"risk": zone["message"]})
    
    return jsonify({"risk": None})

# 🔹 Handle SOS
@app.route('/sos', methods=['POST'])
def sos():
    print(f"🚨 SOS triggered at {datetime.now()}")
    # You can add: send email, SMS (with Twilio), Telegram bot, etc.
    return jsonify({"status": "SOS Received"})

# 🔹 Serve manifest.json
@app.route('/static/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')

# 🔹 Serve service worker
@app.route('/static/sw.js')
def service_worker():
    return send_from_directory('static', 'sw.js')

# 🔹 Serve app icons
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

# 🔹 Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
