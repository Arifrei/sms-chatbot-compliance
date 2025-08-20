from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

app.route("/")
def home():
    return redirecrt("/sms-chatbot", code=302)

@app.route("/sms-chatbot")
def chatbot_service():
    return render_template("service.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

if __name__ == "__main__":
    app.run(debug=True)