from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        user_input = request.form.get("user_input")
        response = f"Hello, {user_input}!"
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug = True)