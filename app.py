from flask import Flask, render_template

from backend_requests import backend, scenario_runner_api

app = Flask(__name__)

@app.route("/")
def view_all_scenarios():
    return render_template("index.html", scenarios=backend.get_scenarios())

@app.route("/scenarios/<id>")
def view_scenario(id):
    scenario = scenario_runner_api.get_scenario(id)
    if scenario is None:
        scenario = backend.get_scenario(id)
        scenario_runner_api.initialize_scenario(scenario, None)
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
        scenario=scenario.model_dump(),
        centerX=(min(xs) + max(xs)) / 2, centerY=(min(ys) + max(ys)) / 2)

@app.route("/api/scenario/<id>", methods=["DELETE"])
def deleteScenario(id):
    backend.delete_scenario(id)
    return ""

if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True)
