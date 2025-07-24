from flask import Flask, render_template_string
import json

app = Flask(__name__)

@app.route("/")
def home():
    try:
        with open("report.json") as f:
            data = json.load(f)
            summary = data.get("summary", {})
    except Exception:
        summary = {"error": "No report found"}

    return render_template_string("""
    <html>
    <head><title>Test Report</title></head>
    <body>
        <h1>Playwright Test Summary</h1>
        {% if summary.error %}
            <p>{{ summary.error }}</p>
        {% else %}
            <ul>
                <li>Total: {{ summary.total }}</li>
                <li>Passed: {{ summary.passed }}</li>
                <li>Failed: {{ summary.failed }}</li>
                <li>Skipped: {{ summary.skipped }}</li>
            </ul>
        {% endif %}
    </body>
    </html>
    """, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)