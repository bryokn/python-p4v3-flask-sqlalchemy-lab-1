from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model,SerializerMixin):
    _tablename_ = "earthquakes"
    id = db.Column(db.Integer, primary_key = True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)
    
    def _repr_(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
