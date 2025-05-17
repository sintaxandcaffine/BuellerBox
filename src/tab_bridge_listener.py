"""
tab_bridge_listener.py
-----------------------
A Flask server that receives tab data from the Bueller Chrome extension
and logs it to the console or processes it further.

Author: SinTaxAndCaffeine
"""

from flask import Flask, request, jsonify
import os
import datetime
import json

app = Flask(__name__)
log_dir = os.path.join(os.getcwd(), "tab_logs")
os.makedirs(log_dir, exist_ok=True)

@app.route("/tabs", methods=["POST"])
def receive_tabs():
    data = request.json
    tabs = data.get("tabs", [])

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(log_dir, f"tabs_{timestamp}.json")

    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(tabs, f, indent=2)

    print(f"✅ Received {len(tabs)} tabs from extension. Logged to {log_file}")
    return jsonify({"status": "success", "received": len(tabs)})

if __name__ == "__main__":
    print("🧠 Bueller Box Tab Listener running on http://localhost:5000/tabs")
    app.run(host="127.0.0.1", port=5000)
