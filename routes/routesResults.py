from flask import jsonify
from flask import request
from controllers.controllerResults import ControllerResults
from flask import Blueprint 

routes_results_get = Blueprint('routes_results_get', __name__)
routes_results_post = Blueprint('routes_results_post', __name__)
routes_results_get_id = Blueprint('routes_results_get_id', __name__)
routes_results_put = Blueprint('routes_results_put', __name__)
routes_results_delete = Blueprint('routes_results_delete', __name__)
# routes_results_partie = Blueprint('routes_results_partie', __name__)

myControllerResults = ControllerResults()

@routes_results_get.route("/results", methods=['GET'])
def getResults():
    json = myControllerResults.index()
    return jsonify(json)


@routes_results_post.route("/results", methods=['POST'])
def crearResults():
    data = request.get_json()
    json = myControllerResults.create(data)
    return jsonify(json)


@routes_results_get_id.route("/results/<string:id>", methods=['GET'])
def getResults(id):
    json = myControllerResults.show(id)
    return jsonify(json)


@routes_results_put.route("/results/<string:id>", methods=['PUT'])
def modificarResults(id):
    data = request.get_json()
    json = myControllerResults.update(id, data)
    return jsonify(json)


@routes_results_delete.route("/results/<string:id>", methods=['DELETE'])
def eliminar(id):
    json = myControllerResults.delete(id)
    return jsonify(json)


# @routes_candidates_partie.route("/candidates/<string:id>/parties/<string:id_parties>", methods=['PUT'])
# def asignarPartidoaCandidato(id, id_parties):
#     json = myControllerCandidates.asignarPartido(id, id_parties)
#     return jsonify(json)