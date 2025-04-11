from observador import Observador, EstadoPuerta
from collections import defaultdict
from typing import Dict

class Dashboard(Observador):
    def __init__(self):
        self.estados: Dict[str, EstadoPuerta] = {}
        self.conteo_estados = defaultdict(int)

    def actualizar(self, puerta_id: str, estado: EstadoPuerta) -> None:
        # Si la puerta ya tenía un estado, lo restamos del conteo
        if puerta_id in self.estados:
            estado_anterior = self.estados[puerta_id]
            self.conteo_estados[estado_anterior] -= 1

        # Actualizamos el nuevo estado
        self.estados[puerta_id] = estado
        self.conteo_estados[estado] += 1
        self.mostrar_estadisticas()

    def mostrar_estadisticas(self) -> None:
        print("\n=== Dashboard PuertaPerruna ===")
        print("Estado actual de las puertas:")
        for estado in EstadoPuerta:
            print(f"- {estado.value}: {self.conteo_estados[estado]}")
        print("\nDetalle por puerta:")
        for puerta_id, estado in self.estados.items():
            print(f"Puerta {puerta_id}: {estado.value}")
        print("============================\n") 