
from flask import Blueprint, render_template

docker = Blueprint('docker', __name__, url_prefix='/docker')

@docker.route('')
def home():
    c = {'name':'Paramahansa Yogananda'}
    return render_template('docker.html', container=c)
