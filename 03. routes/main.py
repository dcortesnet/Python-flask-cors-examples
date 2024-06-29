from flask import Flask
from flask_cors import cross_origin

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola, esta ruta no tiene CORS habilitado.'

@app.route('/cors')
@cross_origin()  # Esto permitirá CORS solo para esta ruta
def hello_cors():
    return 'Hola, CORS está habilitado para esta ruta!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
