"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sympy as sym
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from IPython.display import display, Math

import openaq


#api = None

APP = Flask(__name__)

SQLALCHEMY_TRACK_MODIFICATIONS = False


APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(APP)

class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return    f" at {self.datetime} pm25 level was {self.value}"  #  sym.latex((self.datetime, self.value))

    

def aqbase() :
    api = openaq.OpenAQ()
    status, body = api.measurements(city='Los Angeles', parameter='pm25')
    assert(status == 200), 'OpenAQ get error '
    return [(body['results'][i]['date']['utc'],  body['results'][i]['value']) for i in range(100)]

@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    data = aqbase()
    for o in data:
           DB.session.add(Record(datetime=o[0], value=o[1]))
    DB.session.commit()
    return 'Data refreshed!'





@APP.route('/')
def root():
    """Base view."""
    return str(Record.query.filter(Record.value >= 10).all())