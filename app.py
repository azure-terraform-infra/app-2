import os
from flask import Flask

app = Flask(__name__)

# Read version from environment
APP_VERSION = os.environ.get("APP_VERSION", "unknown")

@app.route("/")
def hello():
    return f"Hello from Flask-2 inside Docker! Version: {APP_VERSION}"

@app.route("/health")
def health():
    return {'status': 'healthy'}, 200

@app.route("/ready")
def ready():
    # Check database connection, etc.
    return {'status': 'ready'}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
