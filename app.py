from flask import Flask, render_template, request

from backend_requests import backend, scenario_runner_api, controller1

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/scenarios/<id>")
def view_scenario(id):
    scenario = scenario_runner_api.get_scenario(id)
    if scenario is None or scenario.status == "COMPLETED": # or scenario.status != "CREATED"
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

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/index")
def index():
    return render_template("index.html", scenarios=backend.get_scenarios())

@app.route("/api/scenario/<id>", methods=["DELETE"])
def delete_scenario(id):
    backend.delete_scenario(id)
    return ""

@app.route("/api/scenario/<id>", methods=["GET"])
def get_scenario(id):
    response = scenario_runner_api.get_scenario(id)
    if response is None:
        return "Not found", 404
    return response.model_dump()

@app.route("/api/scenario/", methods=["POST"])
def create_scenario():
    vehicles = request.form.get('vehicles', 5, int)
    customers = request.form.get('customers', 10, int)
    app.logger.info("vehicles %d customers %d", vehicles, customers)
    return render_template("fragment/single_scenario_in_list.html", scenario=backend.create_scenario(vehicles, customers).model_dump())

@app.route("/api/scenario/<id>/launch", methods=["POST"])
def launch_scenario(id):
    return render_template("fragment/launch_scenario.html", result=scenario_runner_api.launch_scenario(id, 0.1))

@app.route("/api/scenario/<id>/assign")
def assign(id):
    #controller.step(scenario_runner_api.get_scenario(id))
    scenario = scenario_runner_api.get_scenario(id)
    if not controller1.piority_customer:
        controller1.piority_customer = [1] * len(scenario.customers)
    controller1.step(scenario)
    return ""


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(port=5001, debug=True)

# 1. Create in backend => Not in ScenarioRunner
# 2. Init in ScenarioRunner => Status = CREATED
# 3. Launch => Status = RUNNING
# 3.1 Init => ERROR already running
# 4. Update => Status = RUNNING
# 5. Launch => Status = RUNNING
