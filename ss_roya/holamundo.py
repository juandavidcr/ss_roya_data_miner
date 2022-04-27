from crypt import methods
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola Mundo'

# GET, PUT,PATCH,POST,DELETE
@app.route('/posts/<post_id>',methods=['GET','POST'])
def lala(post_id):
    return 'El id del post es: '+post_id