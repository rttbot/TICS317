from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/reservar', methods=['POST'])
def reservar():
    data = request.json
    # Procesar la reserva aquí
    return jsonify({"mensaje": "Reserva exitosa", "datos": data})

if __name__ == '__main__':
   app.run(port=5000)