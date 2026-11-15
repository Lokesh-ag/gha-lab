from flask import Flask

app = Flask(__name__)


def add(a: int, b: int) -> int:
    return a - b


@app.route("/")
def index():
    return "hello from gha-lab"


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
