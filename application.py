from flask import Flask, render_template_string, jsonify
from datetime import datetime, timezone
import os

GITHUB_REPO_URL = os.environ.get(
    "GITHUB_REPO_URL",
    "https://github.com/vinushan20/AWSPractical"
)

application = Flask(__name__)


@application.route("/")
def home():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

    env_name = os.environ.get(
        "AWS_EB_ENVIRONMENT_NAME",
        "LOCAL_DEBUG"
    )

    aws_region = os.environ.get(
        "AWS_REGION",
        "us-east-1"
    )

    return render_template_string(
        HTML_TEMPLATE,
        current_time=now,
        github_url=GITHUB_REPO_URL,
        env_name=env_name,
        aws_region=aws_region
    )


@application.route("/health")
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "AURA",
        "environment": os.environ.get(
            "AWS_EB_ENVIRONMENT_NAME",
            "LOCAL_DEBUG"
        ),
        "region": os.environ.get(
            "AWS_REGION",
            "us-east-1"
        ),
        "timestamp_utc": datetime.now(
            timezone.utc
        ).isoformat()
    }), 200


@application.route("/api/info")
def api_info():
    return jsonify({
        "application": "AURA",
        "platform": "AWS Elastic Beanstalk",
        "runtime": "Python + Flask + Gunicorn",
        "status": "operational"
    }), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(
        host="0.0.0.0",
        port=port
    )
