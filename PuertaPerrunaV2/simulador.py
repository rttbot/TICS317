from puerta_perruna import PuertaPerruna
from dashboard import Dashboard
import time
import random

def simular_sistema():
    # Crear el dashboard
    dashboard = Dashboard()

    # Crear varias puertas
    puertas = [
        PuertaPerruna(f"P{i}") for i in range(1, 5)  # Cambiado a 4 puertas
    ]

    # Registrar el dashboard como observador de todas las puertas
    for puerta in puertas:
        puerta.agregar_observador(dashboard)
        puerta.notificar_observadores

    # Mostrar estadísticas iniciales del dashboard
    dashboard.mostrar_estadisticas()
    # Simular operaciones
    for _ in range(10):  # Simular 10 perros entrando y saliendo
        puerta = random.choice(puertas)
        # print(f"\nPerro ladra dos veces para salir por la puerta {puerta.id}")
        dashboard.mostrar_estadisticas()
        print(f"Perro X ladra dos veces para salir y espera atentamente a que se abra la puerta {puerta.id} ...")
 
        
        if puerta.procesar_ladrido("Guau Guau"):
            print(f"\nPerro X en puerta {puerta.id} ya está en el patio haciendo sus cosas....")
            time.sleep(10)
            dashboard.mostrar_estadisticas()

            print(f"\nPerro X termina de hacer sus cosas y vuelve a la puerta {puerta.id} .")
            print("Perro X ladra dos veces para entrar...")
            time.sleep(1)
            contador = 0   
            volvio = True
            while not puerta.procesar_ladrido("Guau Guau"):
                dashboard.mostrar_estadisticas()
                time.sleep(1)
                contador += 1
                if contador > 10:
                    print("Parece que Perro X no volverá.")
                volvio = False
                break
            if volvio:
                dashboard.mostrar_estadisticas()
                print("\nPerro X ha vuelto.") 
            else:
                dashboard.mostrar_estadisticas()
                print("La puerta {puerta.id} se abrió, pero parece que Perro X se arrepintió.")

        # Mostrar estadísticas finales del dashboard
        dashboard.mostrar_estadisticas()

if __name__ == "__main__":
    simular_sistema() 