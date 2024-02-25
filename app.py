from flask import Flask, request, render_template, redirect, url_for
from models import db, Anagrafica, Credito, Debito
from sqlalchemy import exc

import secrets

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

# read the secret key
try:
    with open('.secret', 'r') as secretfile:
        app.config['SECRET_KEY'] = secretfile.read().strip()
except FileNotFoundError:
    # build a valid secret key
    print('Building a valid .secretkey')
    app.config['SECRET_KEY'] = secrets.token_hex(24)
    # write to disk
    with open('.secret', 'w') as secretfile:
        secretfile.write(app.config['SECRET_KEY'])


# route to home
@app.route('/')
@app.route('/home')
def app_home():
    return render_template('home.html')


# route to about
@app.route('/about')
def app_about():
    return render_template('about.html', APP_NAME=app.config['APP_NAME'], APP_RELEASE=app.config['APP_RELEASE'])


# route to anagrafica (ALL)
@app.route('/ana/all')
def app_ana_all():
    """ Mostra tutte le dichiarazioni in archivio (Zoom) """
    return render_template('ana_all.html', Anagrafiche=Anagrafica.query.all())


# route to anagrafica (UPDATE)
@app.route('/ana/<int:id>', methods=['GET', 'POST'])
def app_ana_update(id):
    """ Mostra/Aggiorna la dichiarazione  """
    ana = Anagrafica.query.filter_by(id=id).first()
    if ana:
        if request.method == 'POST':
            # Update
            ana.Nome = request.form['Nome']
            ana.Cognome = request.form['Cognome']
            ana.CodFis = request.form['CodFis']

            try:
                db.session.commit()
                return render_template('ana_update.html', Anagrafica=ana)
            except exc.IntegrityError as e:
                db.session.rollback()
                return render_template('ana_err.html', msg=f"Update failed " + e.__str__())
        else:
            return render_template('ana_update.html', Anagrafica=ana)
    else:
        return render_template('ana_err.html', msg=f"Anagrafica with id ={id} not found")


# route to anagrafica (INSERT)
@app.route('/ana/insert', methods=['GET', 'POST'])
def app_ana_insert():
    """ Inserisce una nuova Anagrafica  """
    if request.method == 'POST':
        ana = Anagrafica()
        ana.Nome = request.form['Nome']
        ana.Cognome = request.form['Cognome']
        ana.CodFis = request.form['CodFis']
        if ana:
            try:
                db.session.add(ana)
                db.session.commit()
                return render_template('ana_update.html', Anagrafica=ana)
            except exc.IntegrityError as e:
                db.session.rollback()
                return render_template('ana_err.html', msg=f"Insert failed " + e.__str__())
        else:
            return render_template('ana_err.html', msg=f"Insert in Anagrafica failed")

    else:
        return render_template('ana_insert.html')


# route to anagrafica (DELETE)
@app.route('/ana/delete/<int:id>', methods=['POST'])
def app_ana_delete(id):
    """ Cancella la dichiarazione """
    try:
        ana = Anagrafica.query.filter_by(id=id).first()
        db.session.delete(ana)
        db.session.commit()
        return redirect(url_for('app_ana_all'))
    except exc.IntegrityError as e:
        db.session.rollback()
        return render_template('ana_err.html', msg=f"Delete failed " + e.__str__())


# route to debito (ALL)
@app.route('/deb/all')
def app_deb_all():
    """ Mostra tutti i debiti di ogni dichiarazione (zoom) """
    return render_template('deb_all.html', Debiti=Debito.query.all())


# route to debito (ALL)
@app.route('/ana/<int:id>/deb', methods=['GET'])
def app_ana_deb_all(id):
    """ Mostra tutti i debiti di una determinata dichiarazione (zoom) """
    ana = Anagrafica.query.filter_by(id=id).first()    
    if ana:
        try:
            return render_template('ana_deb_all.html', Anagrafica=ana, Debiti=Debito.query.filter_by(Anagrafica_id=id))
        except Exception as e:
            return render_template('deb_err.html', msg=f"Debiti failed " + e.__str__())
    else:
        # anagrafica must exist
        return render_template('deb_err.html', msg=f"Anagrafica with id ={id} not found")


# route to debito 
@app.route('/ana/<int:id>/deb/<int:id_deb>', methods=['GET', 'POST'])
def app_ana_deb(id, id_deb):
    """ Mostra il debito id_deb della dichiarazione id """
    ana = Anagrafica.query.filter_by(id=id).first()    
    if ana:
        if request.method == 'POST':
            # Update
            deb = Debito.query.filter(Debito.Anagrafica_id == id, Debito.id == id_deb).first()
            if deb:
                deb.CodTrib = request.form['CodTrib']
                deb.Importo = float(request.form['Importo'].replace(",", ""))
                try:
                    db.session.commit()
                    return render_template('ana_deb.html', Anagrafica=ana, Debiti=deb)
                except Exception as e:
                    db.session.rollback()
                    return render_template('deb_err.html', msg=f"Update failed " + e.__str__())
            else:                    
                return render_template('deb_err.html', msg=f"Debito with id ={id_deb} not found")

        else:
            # View
            try:
                return render_template('ana_deb.html', Anagrafica=ana, Debiti=Debito.query.filter(Debito.Anagrafica_id == id, Debito.id == id_deb).first())
            except Exception as e:
                return render_template('deb_err.html', msg=f"Debiti failed " + e.__str__())
    else:
        # anagrafica must exist
        return render_template('deb_err.html', msg=f"Anagrafica with id ={id} not found")


# route to debito (DELETE)
@app.route('/ana/<int:id>/deb/delete/<int:id_deb>', methods=['POST'])
def app_ana_deb_delete(id, id_deb):
    """ Cancella il debito """
    try:
        ana = Anagrafica.query.filter_by(id=id).first()
        if ana:
            deb = Debito.query.filter(Debito.Anagrafica_id == id, Debito.id == id_deb).first()
            if deb:
                db.session.delete(deb)
                db.session.commit()
                return redirect(url_for('app_ana_deb_all', id=id))
            else:
                # anagrafica must exist
                return render_template('deb_err.html', msg=f"Debito with id ={id_deb} not found")
        else:
            # anagrafica must exist
            return render_template('deb_err.html', msg=f"Anagrafica with id ={id} not found")
    except exc.IntegrityError as e:
        db.session.rollback()
        return render_template('deb_err.html', msg=f"Delete failed " + e.__str__())


# route to credito (ALL)
@app.route('/cre/all')
def app_cre_all():
    """ Mostra tutti i crediti di ogni dichiarazione (zoom) """
    return render_template('cre_all.html', Crediti=Credito.query.all())


# route to credito (ALL)
@app.route('/ana/<int:id>/cre', methods=['GET'])
def app_ana_cre_all(id):
    """ Mostra tutti i crediti di una determinata dichiarazione (zoom) """
    ana = Anagrafica.query.filter_by(id=id).first()    
    if ana:
        try:
            return render_template('ana_cre_all.html', Anagrafica=ana, Crediti=Credito.query.filter_by(Anagrafica_id=id))
        except Exception as e:
            return render_template('cre_err.html', msg=f"Crediti failed " + e.__str__())
    else:
        # anagrafica must exist
        return render_template('cre_err.html', msg=f"Anagrafica with id ={id} not found")


# route to credito
@app.route('/ana/<int:id>/cre/<int:id_cre>', methods=['GET', 'POST'])
def app_ana_cre(id, id_cre):
    """ Mostra il credito id_cre della dichiarazione id """
    ana = Anagrafica.query.filter_by(id=id).first()    
    if ana:
        if request.method == 'POST':
            # Update
            cre = Credito.query.filter(Credito.Anagrafica_id == id, Credito.id == id_cre).first()
            if cre:
                cre.CodTrib = request.form['CodTrib']
                cre.Importo = float(request.form['Importo'].replace(",", ""))
                try:
                    db.session.commit()
                    return render_template('ana_cre.html', Anagrafica=ana, Crediti=cre)
                except Exception as e:
                    db.session.rollback()
                    return render_template('cre_err.html', msg=f"Update failed " + e.__str__())
            else:                    
                return render_template('cre_err.html', msg=f"Credito with id ={id_cre} not found")

        else:
            # View
            try:
                return render_template('ana_cre.html', Anagrafica=ana, Crediti=Credito.query.filter(Credito.Anagrafica_id == id, Credito.id == id_cre).first())
            except Exception as e:
                return render_template('cre_err.html', msg=f"Crediti failed " + e.__str__())
    else:
        # anagrafica must exist
        return render_template('cre_err.html', msg=f"Anagrafica with id ={id} not found")


# route to credito (DELETE)
@app.route('/ana/<int:id>/cre/delete/<int:id_cre>', methods=['POST'])
def app_ana_cre_delete(id, id_cre):
    """ Cancella il credito """
    try:
        ana = Anagrafica.query.filter_by(id=id).first()
        if ana:
            cre = Credito.query.filter(Credito.Anagrafica_id == id, Credito.id == id_cre).first()
            if cre:
                db.session.delete(cre)
                db.session.commit()
                return redirect(url_for('app_ana_cre_all', id=id))
            else:
                # anagrafica must exist
                return render_template('cre_err.html', msg=f"Credito with id ={id_cre} not found")
        else:
            # anagrafica must exist
            return render_template('cre_err.html', msg=f"Anagrafica with id ={id} not found")
    except exc.IntegrityError as e:
        db.session.rollback()
        return render_template('cre_err.html', msg=f"Delete failed " + e.__str__())


if __name__ == "__main__":
    # you can run dbutil.py to fill the database with garbage/test value
    try:
        with app.app_context():
            db.create_all()
    finally:
        app.run(host='0.0.0.0', debug=True)
