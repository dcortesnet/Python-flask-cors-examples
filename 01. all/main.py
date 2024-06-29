from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)  # Esto permitirá CORS para todas las rutas y orígenes

@app.route('/')
def hello_world():
    return 'Hola, CORS está habilitado!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
