import requests
import threading
import time
import os

BALANCER_URL = os.environ.get('BALANCER_URL', 'http://load_balancer:8080')
NUM_TASKS = int(os.environ.get('NUM_TASKS', 100))

# Este script simula el envío concurrente de tareas y fuerza algunos errores

def enviar_tarea(idx):
    descripcion = f"Tarea enviada por clientemulator hilo {idx}"
    try:
        r = requests.post(f"{BALANCER_URL}/tareas", json={"descripcion": descripcion}, timeout=3)
        if r.status_code == 201:
            print(f"[OK] Tarea {idx} enviada correctamente.")
        else:
            print(f"[ERROR] Tarea {idx} falló: {r.text}")
    except Exception as e:
        print(f"[EXCEPTION] Tarea {idx} falló: {e}")

def forzar_errores():
    # Error 400: JSON vacío
    try:
        r = requests.post(f"{BALANCER_URL}/tareas", json={}, timeout=3)
        print(f"[FORZADO 400] Respuesta: {r.status_code} {r.text}")
    except Exception as e:
        print(f"[FORZADO 400] Excepción: {e}")
    # Error 404: tarea inexistente
    try:
        r = requests.get(f"{BALANCER_URL}/tareas/99999", timeout=3)
        print(f"[FORZADO 404] Respuesta: {r.status_code} {r.text}")
    except Exception as e:
        print(f"[FORZADO 404] Excepción: {e}")


def main():
    threads = []
    for i in range(NUM_TASKS):
        t = threading.Thread(target=enviar_tarea, args=(i+1,))
        t.start()
        threads.append(t)
        time.sleep(0.01)
    for t in threads:
        t.join()
    print(f"\nTotal de tareas intentadas: {NUM_TASKS}")
    forzar_errores()

if __name__ == '__main__':
    main()
