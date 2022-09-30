from flask import jsonify
from flask import request
from controllers.controllerCandidates import ControllerCandidates
from flask import Blueprint

routes_candidates_get = Blueprint("routes_candidates_get", __name__)
routes_candidates_post = Blueprint("routes_candidates_post", __name__)
routes_candidates_get_id = Blueprint("routes_candidates_get_id", __name__)
routes_candidates_put = Blueprint("routes_candidates_put", __name__)
routes_candidates_delete = Blueprint("routes_candidates_delete", __name__)
routes_candidates_partie = Blueprint("routes_candidates_partie", __name__)

myControllerCandidates = ControllerCandidates()


@routes_candidates_get.route("/candidates", methods=["GET"])
def getCandidates():
    json = myControllerCandidates.index()
    return jsonify(json)


@routes_candidates_post.route("/candidates", methods=["POST"])
def crearCandidates():
    data = request.get_json()
    json = myControllerCandidates.create(data)
    return jsonify(json)


@routes_candidates_get_id.route("/candidates/<string:id>", methods=["GET"])
def getCandidates(id):
    json = myControllerCandidates.show(id)
    return jsonify(json)


@routes_candidates_put.route("/candidates/<string:id>", methods=["PUT"])
def modificarCandidates(id):
    data = request.get_json()
    json = myControllerCandidates.update(id, data)
    return jsonify(json)


@routes_candidates_delete.route("/candidates/<string:id>", methods=["DELETE"])
def eliminarCandidates(id):
    json = myControllerCandidates.delete(id)
    return jsonify(json)


@routes_candidates_partie.route(
    "/candidates/<string:id>/parties/<string:id_parties>", methods=["PUT"]
)
def asignarPartidoaCandidato(id, id_parties):
    json = myControllerCandidates.asignarPartido(id, id_parties)
    return jsonify(json)
