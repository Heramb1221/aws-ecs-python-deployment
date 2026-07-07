from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from ECS 🚀"

@app.route("/health")
def health():
    return jsonify({"status": "App is healthy"}), 200

if __name__ == "__main__":
    # Host 0.0.0.0 is required for Docker port mapping to work correctly
    app.run(host="0.0.0.0", port=5000)