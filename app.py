from flask import Flask, render_template
from apps.api import api_blueprint

app = Flask(__name__)

# Registra as rotas da API
app.register_blueprint(api_blueprint, url_prefix="/api")


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
