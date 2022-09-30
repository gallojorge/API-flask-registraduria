from flask import jsonify
from flask import request
from controllers.controllerReports import ControllerReports
from flask import Blueprint

routes_report_get = Blueprint('routes_report_get', __name__)
routes_report_post = Blueprint('routes_report_post', __name__)
routes_report_get_id = Blueprint('routes_report_get_id', __name__)
routes_report_put = Blueprint('routes_report_put', __name__)
routes_report_delete = Blueprint('routes_report_delete', __name__)
#routes_results_partie = Blueprint('routes_results_partie', __name__)

myControllerReports = ControllerReports()

@routes_report_get.route("/report", methods=['GET'])
def getReport():
    json = myControllerReports.index()
    return jsonify(json)


@routes_report_post.route("/report", methods=['POST'])
def crearReport():
    data = request.get_json()
    json = myControllerReports.create(data)
    return jsonify(json)


@routes_report_get_id.route("/report/<string:id>", methods=['GET'])
def getReport(id):
    json = myControllerReports.show(id)
    return jsonify(json)


@routes_report_put.route("/report/<string:id>", methods=['PUT'])
def modificarReport(id):
    data = request.get_json()
    json = myControllerReports.update(id, data)
    return jsonify(json)


@routes_report_delete.route("/report/<string:id>", methods=['DELETE'])
def eliminar(id):
    json = myControllerReports.delete(id)
    return jsonify(json)


# @routes_candidates_partie.route("/candidates/<string:id>/parties/<string:id_parties>", methods=['PUT'])
# def asignarPartidoaCandidato(id, id_parties):
#     json = myControllerCandidates.asignarPartido(id, id_parties)
#     return jsonify(json)