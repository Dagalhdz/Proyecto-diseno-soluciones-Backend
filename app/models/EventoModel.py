import mongoengine as me


class EventoModel(me.Document):
    userEmail = me.EmailField(required=True)
    nombre_Tarea = me.StringField(required=True, max_length=100)
    # descripcion: me.StringField(required=True, max_length=300)
    # tipo_evento: me.BooleanField(required=True)
