import json
import os
from typing import List, Dict

tasks_file = 'tasks.json'

def load_tasks() -> List[Dict]:
    if os.path.exists(tasks_file):
        with open(tasks_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_tasks(tasks: List[Dict]):
    with open(tasks_file, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def add_task(tasks: List[Dict]):
    desc = input('Descripción de la tarea: ')
    tasks.append({'descripcion': desc})
    save_tasks(tasks)
    print('Tarea agregada.')

def list_tasks(tasks: List[Dict]):
    if not tasks:
        print('No hay tareas.')
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t['descripcion']}")

def main():
    tasks = load_tasks()
    while True:
        print('\n1. Listar tareas')
        print('2. Agregar tarea')
        print('3. Salir')
        op = input('Opción: ')
        if op == '1':
            list_tasks(tasks)
        elif op == '2':
            add_task(tasks)
        elif op == '3':
            break
        else:
            print('Opción inválida.')

if __name__ == '__main__':
    main() 