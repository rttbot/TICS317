from puerta_perruna import PuertaPerruna
from dashboard import Dashboard
import time
import random

def simular_sistema():
    # Crear el dashboard
    dashboard = Dashboard()

    # Crear varias puertas
    puertas = [
        PuertaPerruna(f"P{i}") for i in range(1, 4)
    ]

    # Registrar el dashboard como observador de todas las puertas
    for puerta in puertas:
        puerta.agregar_observador(dashboard)

    # Simular operaciones
    for _ in range(10):  # Simular 10 eventos
        puerta = random.choice(puertas)
        print(f"\nIntentando abrir puerta {puerta.id}")
        puerta.abrir()
        
        # Si la puerta está en error, intentar repararla
        if puerta.estado.value == "error":
            time.sleep(1)
            print(f"\nIntentando reparar puerta {puerta.id}")
            puerta.reparar()
        
        time.sleep(2)  # Esperar antes del siguiente evento

if __name__ == "__main__":
    simular_sistema() 