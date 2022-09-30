from flask import jsonify
from flask import request
from controllers.controllerTables import ControllerTables
from flask import Blueprint

routes_tables_get = Blueprint("routes_tables_get", __name__)
routes_tables_post = Blueprint("routes_tables_post", __name__)
routes_tables_get_id = Blueprint("routes_tables_get_id", __name__)
routes_tables_put = Blueprint("routes_tables_put", __name__)
routes_tables_delete = Blueprint("routes_tables_delete", __name__)
routes_tables_candidates = Blueprint("routes_tables_candidates", __name__)

myControllerTables = ControllerTables()


@routes_tables_get.route("/tables", methods=['GET'])
def getTables():
    json = myControllerTables.index()
    return jsonify(json)


@routes_tables_post.route("/tables", methods=['POST'])
def crearTables():
    data = request.get_json()
    json = myControllerTables.create(data)
    return jsonify(json)


@routes_tables_get_id.route("/tables/<string:id>", methods=["GET"])
def getTables(id):
    json = myControllerTables.show(id)
    return jsonify(json)


@routes_tables_put.route("/tables/<string:id>", methods=["PUT"])
def modificarTables(id):
    data = request.get_json()
    json = myControllerTables.update(id, data)
    return jsonify(json)


@routes_tables_delete.route("/tables/<string:id>", methods=["DELETE"])
def eliminarTables(id):
    json = myControllerTables.delete(id)
    return jsonify(json)


@routes_tables_candidates.route(
    "/tables/<string:id>/candidates/<string:id_candidates>", methods=["PUT"]
)
def asignarCandidates(id, id_candidates):
    json = myControllerTables.asignarCandidates(id, id_candidates)
    return jsonify(json)
