from observador import Observador
from collections import defaultdict
from typing import Dict

class Dashboard(Observador):
    def __init__(self):
        self.estados: Dict[str] = {}
        self.conteo_estados = defaultdict(int)

    def actualizar(self, puerta_id: str, estado: str) -> None:
        # Actualizamos el nuevo estado
        self.estados[puerta_id] = estado
        self.mostrar_estadisticas()

    def mostrar_estadisticas(self) -> None:
        print("\n=== Dashboard PuertaPerruna ===")
        print("Estado actual de las puertas:")
        for puerta_id, estado in self.estados.items():
            print(f"Puerta {puerta_id}: {estado}")
        print("============================\n")
