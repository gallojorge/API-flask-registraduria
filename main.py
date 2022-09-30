from flask import Flask
from flask_cors import CORS
import json
from waitress import serve
from routes.routesCandidates import *
from routes.routesParties import *
from routes.routesTables import *
from routes.routesResults import *
from routes.routesReports import *


app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(routes_candidates_get)  # Rutas Candidate
app.register_blueprint(routes_candidates_post)
app.register_blueprint(routes_candidates_get_id)
app.register_blueprint(routes_candidates_put)
app.register_blueprint(routes_candidates_delete)

app.register_blueprint(routes_candidates_partie)  # Rutas Parties
app.register_blueprint(routes_parties_get)
app.register_blueprint(routes_parties_post)
app.register_blueprint(routes_parties_get_id)
app.register_blueprint(routes_parties_put)
app.register_blueprint(routes_parties_delete)

app.register_blueprint(routes_tables_candidates)  # Rutas Tables
app.register_blueprint(routes_tables_get)
app.register_blueprint(routes_tables_post)
app.register_blueprint(routes_tables_get_id)
app.register_blueprint(routes_tables_put)
app.register_blueprint(routes_tables_delete)

# app.register_blueprint(routes_results_partie)  # Rutas Results
app.register_blueprint(routes_results_get)
app.register_blueprint(routes_results_post)
app.register_blueprint(routes_results_get_id)
app.register_blueprint(routes_results_put)
app.register_blueprint(routes_results_delete)

app.register_blueprint(routes_report_get)
app.register_blueprint(routes_report_post)
app.register_blueprint(routes_report_get_id)
app.register_blueprint(routes_report_put)
app.register_blueprint(routes_report_delete)


def loadFileConfig():
    with open("config.json") as f:
        data = json.load(f)
    return data

def run():
    dataConfig = loadFileConfig()
    print(
        "Server running : "
        + "http://"
        + dataConfig["url-backend"]
        + ":"
        + str(dataConfig["port"])
    )
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])


if __name__ == "__main__": 
    run()
