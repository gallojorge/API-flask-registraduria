from flask import jsonify
from flask import request
from controllers.controllerParties import ControllerParties
from flask import Blueprint

routes_parties_get = Blueprint('routes_parties_get', __name__)
routes_parties_post = Blueprint('routes_parties_post', __name__)
routes_parties_get_id = Blueprint('routes_parties_get_id', __name__)
routes_parties_put = Blueprint('routes_parties_put', __name__)
routes_parties_delete = Blueprint('routes_parties_delete', __name__)

myControllerParties = ControllerParties()


@routes_parties_get.route("/parties", methods=['GET'])
def getCandidates():
    json = myControllerParties.index()
    return jsonify(json)


@routes_parties_post.route("/parties", methods=['POST'])
def crearCandidates():
    data = request.get_json()
    json = myControllerParties.create(data)
    return jsonify(json)


@routes_parties_get_id.route("/parties/<string:id>", methods=['GET'])
def getCandidates(id):
    json = myControllerParties.show(id)
    return jsonify(json)


@routes_parties_put.route("/parties/<string:id>", methods=['PUT'])
def modificarCandidates(id):
    data = request.get_json()
    json = myControllerParties.update(id, data)
    return jsonify(json)


@routes_parties_delete.route("/parties/<string:id>", methods=['DELETE'])
def eliminarCandidates(id):
    json = myControllerParties.delete(id)
    return jsonify(json)
