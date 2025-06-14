from flask import Flask, request, jsonify
import json
import os
import time
import contextlib

app = Flask(__name__)

@contextlib.contextmanager
def file_lock(lockfile, wait=0.1, retries=100):
    for _ in range(retries):
        try:
            fd = os.open(lockfile, os.O_CREAT | os.O_EXCL | os.O_RDWR)
            os.close(fd)
            break
        except FileExistsError:
            time.sleep(wait)
    else:
        raise TimeoutError(f'No se pudo obtener el lock para {lockfile}')
    try:
        yield
    finally:
        os.remove(lockfile)

tasks_file = 'tasks.json'
lock_file = 'tasks.json.lock'

def load_tasks():
    if os.path.exists(tasks_file):
        with open(tasks_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with file_lock(lock_file):
        with open(tasks_file, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)

@app.route('/tareas', methods=['GET'])
def get_tareas():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route('/tareas', methods=['POST'])
def add_tarea():
    data = request.get_json()
    if not data or 'descripcion' not in data:
        return jsonify({'error': 'Falta la descripción'}), 400
    tasks = load_tasks()
    tasks.append({'descripcion': data['descripcion']})
    save_tasks(tasks)
    return jsonify({'msg': 'Tarea agregada'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000) 