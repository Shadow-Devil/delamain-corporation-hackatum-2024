from flask import Flask, render_template

import backend_requests.backend

app = Flask(__name__)


@app.route("/")
def view_all_scenarios():
    return render_template("index.html", scenarios=backend_requests.backend.get_all_scenarios())


if __name__ == "__main__":
    app.run(debug=True)
