from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='assets')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route("/assets/<path:filename>")
def serve_assets(filename):
    return send_from_directory(os.path.join(BASE_DIR, 'assets'), filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
