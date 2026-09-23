from flask import Flask, render_template, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

GITHUB_REPO_URL = "https://github.com/vinushan20/AWSPractical.git"


@app.route("/")
def index():
    server_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    return render_template(
        "index.html",
        server_time=server_time,
        status="Healthy & Active",
        github_repo_url=GITHUB_REPO_URL,
    )


@app.route("/health")
def health():
    return jsonify(
        status="ok",
        server_time_utc=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
    )


if __name__ == "__main__":
    # For AWS Elastic Beanstalk, the WSGI entry point is typically "application"
    app.run(host="0.0.0.0", port=8000, debug=True)


# Elastic Beanstalk looks for a variable named "application" by default
application = app
