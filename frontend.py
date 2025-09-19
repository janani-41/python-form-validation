import os
from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

# Backend URL
BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Login/Signup Form</title>
</head>
<body>
    <h2>Login/Signup Form</h2>

    <h3>Signup</h3>
    <form method="post" action="/signup">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required minlength="4">
        <button type="submit">Signup</button>
    </form>

    <h3>Login</h3>
    <form method="post" action="/login">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>

    {% if result %}
        <h3>Result:</h3>
        <pre>{{ result }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/signup", methods=["POST"])
def signup():
    username = request.form.get("username")
    password = request.form.get("password")
    try:
        response = requests.post(f"{BACKEND_URL}/signup/{username}/{password}")
        return render_template_string(HTML_TEMPLATE, result=response.json())
    except Exception as e:
        return render_template_string(HTML_TEMPLATE, result=f"Error: {e}")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    try:
        response = requests.post(f"{BACKEND_URL}/login/{username}/{password}")
        return render_template_string(HTML_TEMPLATE, result=response.json())
    except Exception as e:
        return render_template_string(HTML_TEMPLATE, result=f"Error: {e}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
