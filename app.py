from flask import Flask, render_template
from content import DATA

app = Flask(__name__)


@app.route("/")
def index():
    # We’ll use DATA inside index.html via Jinja later
    return render_template("index.html", data=DATA)


if __name__ == "__main__":
    # debug=True is only for local development
    app.run(debug=True)

