from flask import Flask, render_template

import backend_requests.backend

app = Flask(__name__)


@app.route("/")
def view_all_scenarios():
    return render_template("index.html", scenarios=backend_requests.backend.get_all_scenarios())

@app.route("/scenarios/<id>")
def view_scenario(id):
    scenario = backend_requests.backend.get_scenario(id)
    xs = [
        *map(lambda v: v.coordX, scenario.vehicles),
        *map(lambda c: c.coordX, scenario.customers),
        *map(lambda c: c.destinationX, scenario.customers)]

    ys = [
        *map(lambda v: v.coordY, scenario.vehicles),
        *map(lambda c: c.coordY, scenario.customers),
        *map(lambda c: c.destinationY, scenario.customers)]
    return render_template(
        "scenario.html",
        scenario=scenario,
        centerX=(min(xs) + max(xs)) / 2, centerY=(min(ys) + max(ys)) / 2)


if __name__ == "__main__":
    app.run(debug=True)
