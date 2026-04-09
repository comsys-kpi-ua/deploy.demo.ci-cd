from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    version = os.getenv("APP_VERSION", "1.0.0")
    return f"<h1>Hello! App Version: {version}</h1>"

@app.route('/health')
def health():
    if os.path.exists("crash.txt"):
        return "Internal Server Error", 500
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
