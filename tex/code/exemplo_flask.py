#coding=UTF-8
from __future__ import absolute_import

from flask import Flask, render_template, request, \
    redirect, url_for

from flask_script import Manager, Server
from flask_migrate import MigrateCommand, Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('settings')
app.config.from_pyfile('settings_local.py', silent=True)
app.config.setdefault('SQLALCHEMY_DATABASE_URI',
                      'sqlite:////tmp/compras.db')

db = SQLAlchemy(app)
Migrate(app, db)


class Lista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.relationship('ItemLista')


class ItemLista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lista_id = db.Column(db.Integer, db.ForeignKey('lista.id'))
    nome = db.Column(db.Text)
    lista = db.relationship('Lista')


@app.route('/')
def index():
    return redirect(url_for('.lista'))


@app.route('/lista/')
def lista():
    lista_id = request.args.get('lista_id')
    if not lista_id:
        lista = Lista()
        db.session.add(lista)
        db.session.commit()
        return redirect(url_for('.lista', lista_id=lista.id))
    lista = Lista.query.get(lista_id)
    return render_template('lista.html', lista=lista)


@app.route('/lista/novo_item/', methods=['POST'])
def novo_item():
    form = request.form
    lista_id = form['lista_id']
    nome_item = form['nome_item']
    lista = Lista.query.get(lista_id)
    item_lista = ItemLista(nome=nome_item)
    lista.items.append(item_lista)
    db.session.commit()
    return redirect(url_for('.lista', lista_id=lista.id))

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())

if __name__ == '__main__':
    manager.run()
