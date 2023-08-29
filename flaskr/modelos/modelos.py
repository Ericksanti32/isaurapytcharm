from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import  fields
import  enum

db = SQLAlchemy()

class EnumADiccionario(fields.Field)
    def _serialize(self, value, attr,  obj, **kwargs):
        if value is None:
            return None
        return {'llave':value.name, 'valor':value.value}


class AlbumSchema(SQLAlchemyAutoSchema)
    medio = EnumADiccionario(attribute=('medio'))
    class Meta:
        model = Album
        include_relations = True
        load_instance = True
class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.minutos, self.segundos, self.interprete)


class Usuario(db.Model):
    tablename = db.Column(db.String(30))
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(50))
    contraseña = db.Column(db.String(30))

    def __repr__(self):
        return "{}-{}".format(self.id, self.nombre_usuario)


class Album(db.Model):
    tablename = db.Column(db.String(30))
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(30))
    año = db.Column(db.Integer)
    description = db.Column(db.String(60))
    medio = db.Column(db.String(50))

    def __repr__(self):
        return "{}-{}-{}".format(self.id, self.titulo, self.año)
