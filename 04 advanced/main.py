from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://mi-dominio.com"}}, supports_credentials=True)

@app.route('/api/data')
def data():
    return 'Datos con CORS habilitado!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
