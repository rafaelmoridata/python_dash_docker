#!/usr/bin/python3

from flask import Flask, render_template
from blueprints.pocker import pocker
from blueprints.jk import jk
from blueprints.gitlab import gitlab


app = Flask(__name__)
app.register_blueprint(pocker)
app.register_blueprint(jk)
app.register_blueprint(gitlab)

@app.route('/')
def home():
    return render_template('index.html')
	#b = 2 + 2
    # teste de conflito


app.run(debug=True)
# fim do meu arquivo
