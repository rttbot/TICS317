from puerta_perruna import PuertaPerruna
import time
import random

def simular_sistema():
    # Crear varias puertas
    puertas = [
        PuertaPerruna(f"P{i}") for i in range(1, 4)
    ]

    # Simular operaciones
    for _ in range(10):  # Simular 10 perros entrando y saliendo
        puerta = random.choice(puertas)
        print(f"\nPerro X ladra dos veces para salir por la puerta {puerta.id}")
        
        if puerta.procesar_ladrido("Guau Guau"):
            print(f"\nPerro X en puerta {puerta.id} ya está en el patio haciendo sus cosas....")
            time.sleep(5)
            
            print(f"\nPerro X termina de hacer sus cosas y vuelve a la puerta {puerta.id}.")
            print("Perro X ladra dos veces para entrar...")
            time.sleep(1)
            
            if puerta.procesar_ladrido("Guau Guau"):
                print("\nPerro X ha vuelto.")
            else:
                print(f"La puerta {puerta.id} se abrió, pero parece que Perro X se arrepintió.")
        
        time.sleep(2)  # Esperar antes del siguiente evento

if __name__ == "__main__":
    simular_sistema() 