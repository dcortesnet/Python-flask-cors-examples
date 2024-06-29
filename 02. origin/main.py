from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins='https://mi-dominio.com')  # Esto permitirá CORS solo para 'https://mi-dominio.com'

@app.route('/')
def hello_world():
    return 'Hola, CORS está habilitado para un origen específico!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
