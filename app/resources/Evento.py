from flask_restful import Resource, reqparse, fields

from ..models.EventoModel import EventoModel
from flask import jsonify


class Evento(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userEmail', type=str, required=True)
        parser.add_argument('nombre_Tarea', type=str, required=True)
        args = parser.parse_args()
        evento = EventoModel(
            userEmail=args['userEmail'], nombre_Tarea=args['nombre_Tarea'])
        evento.save()

        return jsonify(evento)

    def get(self):
        data = EventoModel.objects.get(id="644639a45f766914279fe7a3")
        return jsonify(data)
