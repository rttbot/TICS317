import requests
import threading
import time
import os

SERVER_URL = os.environ.get('SERVER_URL', 'http://server:9000')
NUM_TASKS = int(os.environ.get('NUM_TASKS', 100))

# Este script simula el envío concurrente de tareas al servidor Flask

def enviar_tarea(idx):
    descripcion = f"Tarea enviada por client en hilo {idx}"
    try:
        r = requests.post(f"{SERVER_URL}/tareas", json={"descripcion": descripcion}, timeout=3)
        if r.status_code == 201:
            print(f"[OK] Tarea {idx} enviada correctamente.")
        else:
            print(f"[ERROR] Tarea {idx} falló: {r.text}")
    except Exception as e:
        print(f"[EXCEPTION] Tarea {idx} falló: {e}")

def main():
    threads = []
    for i in range(NUM_TASKS):
        t = threading.Thread(target=enviar_tarea, args=(i+1,))
        t.start()
        threads.append(t)
        time.sleep(0.01)  # Pequeña pausa para simular concurrencia realista
    for t in threads:
        t.join()
    print(f"\nTotal de tareas intentadas: {NUM_TASKS}")

if __name__ == '__main__':
    main() 