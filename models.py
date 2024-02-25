from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Anagrafica(db.Model):
    __tablename__ = "Anagrafica"
    id = db.Column(db.Integer, primary_key=True)
    CreatedOn = db.Column(db.DateTime(), default=datetime.now)
    UpdatedOn = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)

    Nome = db.Column(db.String(20), unique=False, nullable=False)
    Cognome = db.Column(db.String(20), unique=False, nullable=False)
    CodFis = db.Column(db.String(16), unique=True, nullable=False)

    debiti = relationship('Debito', cascade="all, delete-orphan")
    crediti = relationship('Credito', cascade="all, delete-orphan")

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)


class Debito(db.Model):
    __tablename__ = "Debito"
    id = db.Column(db.Integer, primary_key=True)
    CreatedOn = db.Column(db.DateTime(), default=datetime.now)
    UpdatedOn = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)

    CodTrib = db.Column(db.String(80), unique=False, nullable=False)
    Importo = db.Column(db.Float(), unique=False, nullable=False)

    Anagrafica_id = db.Column(db.Integer, db.ForeignKey('Anagrafica.id'), nullable=False)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)


class Credito(db.Model):
    __tablename__ = "Credito"
    id = db.Column(db.Integer, primary_key=True)
    CreatedOn = db.Column(db.DateTime(), default=datetime.now)
    UpdatedOn = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)

    CodTrib = db.Column(db.String(80), unique=False, nullable=False)
    Importo = db.Column(db.Float(), unique=False, nullable=False)

    Anagrafica_id = db.Column(db.Integer, db.ForeignKey('Anagrafica.id'), nullable=False)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
 
