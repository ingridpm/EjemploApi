from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def pantalla_principal():
    return "Prueba"

@app.route('/hola',methods=['GET'])
def hola_mundo():
    return "hola mundo"

if __name__ == '__main__':
    puerto = 5000
    app.run(host='0.0.0.0', port = puerto)
