"""""
    Fill the database with a test/garbage
"""""
from flask import Flask
# from config import *
from models import db, Anagrafica, Credito, Debito

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)


with app.app_context():
    db.create_all()

    Ana = Anagrafica(Nome="Piani", Cognome="Gianni", CodFis="PIANIGIANICFXXXX")
    db.session.add(Ana)
    db.session.flush()
    db.session.add(Debito(CodTrib="4001", Importo=101, Anagrafica_id=Ana.id))
    db.session.add(Debito(CodTrib="5001", Importo=201, Anagrafica_id=Ana.id))
    db.session.add(Debito(CodTrib="6001", Importo=301, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="7001", Importo=441, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="8001", Importo=551, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="9001", Importo=661, Anagrafica_id=Ana.id))

    Ana = Anagrafica(Nome="Bauh", Cognome="Sola", CodFis="BAUSOLAAAACFXXXX")
    db.session.add(Ana)
    db.session.flush()
    db.session.add(Debito(CodTrib="4002", Importo=11102, Anagrafica_id=Ana.id))
    db.session.add(Debito(CodTrib="5002", Importo=22202, Anagrafica_id=Ana.id))
    db.session.add(Debito(CodTrib="6002", Importo=33302, Anagrafica_id=Ana.id))
    db.session.add(Debito(CodTrib="7002", Importo=44402, Anagrafica_id=Ana.id))
    db.session.add(Debito(CodTrib="8002", Importo=55502, Anagrafica_id=Ana.id))
    db.session.add(Debito(CodTrib="9002", Importo=66602, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="7002", Importo=24442, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="8002", Importo=25552, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="9002", Importo=26662, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="A002", Importo=27772, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="B002", Importo=28882, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C002", Importo=29992, Anagrafica_id=Ana.id))

    Ana = Anagrafica(Nome="Shigeru", Cognome="Miyamoto", CodFis="CFSPRMARIOITSAME")
    db.session.add(Ana)
    db.session.flush()
    db.session.add(Debito(CodTrib="4003", Importo=33103, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="7003", Importo=33443, Anagrafica_id=Ana.id))

    Ana = Anagrafica(Nome="Hidetaka", Cognome="Miyazaki", CodFis="CFBLOODBORNEXXXX")
    db.session.add(Ana)
    db.session.flush()
    db.session.add(Debito(CodTrib="4004", Importo=44104, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="7004", Importo=44444, Anagrafica_id=Ana.id))

    Ana = Anagrafica(Nome="Hideo", Cognome="Kojima", CodFis="CFMTLGERSOLIDDDD")
    db.session.add(Ana)
    db.session.flush()
    db.session.add(Debito(CodTrib="D015", Importo=555105, Anagrafica_id=Ana.id))
    db.session.add(Debito(CodTrib="D025", Importo=555205, Anagrafica_id=Ana.id))
    db.session.add(Debito(CodTrib="D035", Importo=555305, Anagrafica_id=Ana.id))
    db.session.add(Debito(CodTrib="D015", Importo=555405, Anagrafica_id=Ana.id))
    db.session.add(Debito(CodTrib="D025", Importo=555505, Anagrafica_id=Ana.id))
    db.session.add(Debito(CodTrib="D035", Importo=555605, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C001", Importo=155445, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C002", Importo=255445, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C003", Importo=355445, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C004", Importo=455445, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C005", Importo=555445, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C006", Importo=655445, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C007", Importo=755445, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C008", Importo=855445, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C009", Importo=955445, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C010", Importo=115445, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C011", Importo=125445, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C012", Importo=135445, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C013", Importo=145445, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C014", Importo=155445, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C015", Importo=165445, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C016", Importo=177445, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C017", Importo=185445, Anagrafica_id=Ana.id))
    db.session.add(Credito(CodTrib="C018", Importo=195445, Anagrafica_id=Ana.id))

    db.session.commit()
