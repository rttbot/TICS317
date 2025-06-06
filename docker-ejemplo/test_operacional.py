import requests
import subprocess
import time
import os
import json
from threading import Thread

# Este script simula varios usuarios agregando tareas al sistema
def simulate_user(user_id, num_tasks=5):
    for i in range(num_tasks):
        # Simula la entrada del usuario usando subprocess
        proc = subprocess.Popen(['python', 'main.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Secuencia de inputs: agregar tarea y salir
        inputs = '2\nTarea de usuario {} número {}\n3\n'.format(user_id, i+1)
        try:
            out, err = proc.communicate(inputs, timeout=5)
            print(f"[Usuario {user_id}] Tarea {i+1} agregada. Salida:\n{out}")
        except subprocess.TimeoutExpired:
            proc.kill()
            print(f"[Usuario {user_id}] Timeout al agregar tarea {i+1}")
        time.sleep(0.2)

def main():
    num_users = 3
    threads = []
    for user_id in range(1, num_users+1):
        t = Thread(target=simulate_user, args=(user_id,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    # Mostrar el resultado final
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r', encoding='utf-8') as f:
            tasks = json.load(f)
        print(f"\nTotal de tareas registradas: {len(tasks)}")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t['descripcion']}")
    else:
        print("No se encontró el archivo tasks.json")

if __name__ == '__main__':
    main() 