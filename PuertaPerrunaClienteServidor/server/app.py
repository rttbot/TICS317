from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from collections import defaultdict

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Almacenamiento de estados de las puertas
estados_puertas = {}

@app.route('/')
def index():
    return render_template('index.html', estados=estados_puertas)

@app.route('/api/puerta/estado', methods=['POST'])
def actualizar_estado():
    data = request.json
    puerta_id = data.get('id')
    estado = data.get('estado')
    
    if puerta_id and estado:
        estados_puertas[puerta_id] = estado
        # Emitir actualización a todos los clientes web conectados
        socketio.emit('actualizacion_estado', {'puerta_id': puerta_id, 'estado': estado})
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': 'Datos inválidos'}), 400

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5001) 