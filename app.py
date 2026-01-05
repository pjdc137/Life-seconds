from flask import Flask, render_template, request, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

AVERAGE_LIFESPAN_SECONDS = 78.8 * 365.25 * 24 * 60 * 60

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json

    dob = datetime(
        int(data["year"]),
        int(data["month"]),
        int(data["day"]),
        int(data["hour"]),
        int(data["minute"]),
        tzinfo=timezone.utc,
    )

    now = datetime.now(timezone.utc)
    seconds_lived = (now - dob).total_seconds()
    seconds_left = max(0, AVERAGE_LIFESPAN_SECONDS - seconds_lived)

    return jsonify({
        "seconds_lived": int(seconds_lived),
        "seconds_left": int(seconds_left),
        "timestamp": now.timestamp()
    })

if __name__ == "__main__":
    import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

