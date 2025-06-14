from flask import Flask, request, jsonify, abort
import json
import os
import sys
from datetime import datetime
from collections import defaultdict, deque

app = Flask(__name__)
tasks_file = 'tasks.json'

# Estadísticas de errores
error_stats = defaultdict(int)
error_log = deque(maxlen=20)

def load_tasks():
    if os.path.exists(tasks_file):
        with open(tasks_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(tasks_file, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

@app.route('/health')
def health():
    return jsonify({'status': 'ok'})

@app.route('/errors/stats')
def error_stats_view():
    return jsonify({
        'total_errors': sum(error_stats.values()),
        'error_types': dict(error_stats),
        'recent_errors': list(error_log)
    })

@app.errorhandler(400)
def bad_request(e):
    error_stats['400_BAD_REQUEST'] += 1
    error_log.append({'type': '400_BAD_REQUEST', 'msg': str(e), 'timestamp': datetime.now().isoformat()})
    return jsonify({'error': 'Bad request', 'msg': str(e)}), 400

@app.errorhandler(404)
def not_found(e):
    error_stats['404_NOT_FOUND'] += 1
    error_log.append({'type': '404_NOT_FOUND', 'msg': str(e), 'timestamp': datetime.now().isoformat()})
    return jsonify({'error': 'Not found', 'msg': str(e)}), 404

@app.errorhandler(500)
def internal_error(e):
    error_stats['500_INTERNAL_ERROR'] += 1
    error_log.append({'type': '500_INTERNAL_ERROR', 'msg': str(e), 'timestamp': datetime.now().isoformat()})
    return jsonify({'error': 'Internal server error', 'msg': str(e)}), 500

@app.route('/tareas', methods=['GET'])
def get_tareas():
    return jsonify(load_tasks())

@app.route('/tareas', methods=['POST'])
def add_tarea():
    data = request.get_json(force=True, silent=True)
    if not data or 'descripcion' not in data:
        abort(400, description='JSON vacío o sin descripción')
    tasks = load_tasks()
    tasks.append({'descripcion': data['descripcion']})
    save_tasks(tasks)
    return jsonify({'msg': 'Tarea agregada'}), 201

@app.route('/tareas/<int:idx>', methods=['GET'])
def get_tarea(idx):
    tasks = load_tasks()
    if idx < 0 or idx >= len(tasks):
        abort(404, description='Tarea inexistente')
    return jsonify(tasks[idx])

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    app.run(host='0.0.0.0', port=port)
