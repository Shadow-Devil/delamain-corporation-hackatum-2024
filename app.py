from flask import Flask, render_template, request

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
def delete_scenario(id):
    backend.delete_scenario(id)
    return ""

@app.route("/api/scenario/", methods=["POST"])
def create_scenario():
    vehicles = request.args.get('vehicles', 5, int)
    customers = request.args.get('customers', 10, int)
    return render_template("single_scenario_in_list.html", scenario=backend.create_scenario(vehicles, customers).model_dump())


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(port=5001, debug=True)
