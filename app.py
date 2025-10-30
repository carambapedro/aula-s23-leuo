from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# rota principal
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome", "anônimo")
        return render_template("index.html", nome=nome, submitted=True)
    return render_template("index.html", nome=None, submitted=False)

@app.route("/sobre")
def sobre():
    return "<h2>Sobre</h2><p>Aplicação exemplo com Flask.</p>"

if __name__ == "__main__":
    # porta 5000 por padrão; debug True para desenvolvimento
    app.run(debug=True, host="0.0.0.0", port=5000)
