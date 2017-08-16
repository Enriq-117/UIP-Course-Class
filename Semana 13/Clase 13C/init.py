from flask import Flask, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY DATABASE_URI'] = 'sqlite: ///estudiantes.sqlite3'
app.config['SECRET_KEY'] = 'uippc3'

db = SQLAlchemy(app)

class Estudiantes(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    ciudad = db.Column(db.String(50))
    direccion = db.Column(db.String(200))
    pin = db.Column(db.String(10))
    def __init__ (self, nombre, ciudad, direccion, pin):
        self.nombre = nombre
        self.ciudad = ciudad
        self.direccion = direccion
        self.pin = pin

@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if not request.form['nombre'] or not request.form['ciudad'] or not request.form['direccion']:
        flash('Por favor introduzca todos los campos', 'error')
    else:
        estudiante = estudiante(request.form['nombre'],
                                request.form['ciudad'],
                                request.form['direccion'],
                                request.form['pin'])