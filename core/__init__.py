from flask import Flask
from decouple import config
from flask_restx import Api

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
api = Api(
    app,
    version='1.0',
    title='Hi-Rez Studios server status API',
    description='Get server status for Hi-Rez Studios games',
    license='',
    contact='',
    contact_url='',
    contact_email='',
    doc='/',
    prefix='/api/v1'
)

from core import routes