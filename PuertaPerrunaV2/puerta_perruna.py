from observador import Observable, Observador, EstadoPuerta
from typing import List
import time
import random

class PuertaPerruna(Observable):
    def __init__(self, id: str):
        self.id = id
        self.estado = EstadoPuerta.CERRADA
        self.observadores: List[Observador] = []
        self.intentos_fallidos = 0
        self.max_intentos = 3

    def agregar_observador(self, observador: Observador) -> None:
        if observador not in self.observadores:
            self.observadores.append(observador)

    def eliminar_observador(self, observador: Observador) -> None:
        if observador in self.observadores:
            self.observadores.remove(observador)

    def notificar_observadores(self) -> None:
        for observador in self.observadores:
            observador.actualizar(self.id, self.estado)

    def abrir(self) -> None:
        try:
            # Simulamos un posible error
            if random.random() < 0.2:  # 20% de probabilidad de error
                self.intentos_fallidos += 1
                if self.intentos_fallidos >= self.max_intentos:
                    self.estado = EstadoPuerta.ERROR
                    raise Exception(f"Error al abrir la puerta {self.id}: Demasiados intentos fallidos")
                raise Exception(f"Error al abrir la puerta {self.id}")
            
            self.estado = EstadoPuerta.ABIERTA
            self.intentos_fallidos = 0
            print(f"Puerta {self.id} abierta")
            time.sleep(2)  # La puerta permanece abierta por 2 segundos
            self.cerrar()
        except Exception as e:
            print(str(e))
        finally:
            self.notificar_observadores()

    def cerrar(self) -> None:
        try:
            if random.random() < 0.1:  # 10% de probabilidad de error
                self.estado = EstadoPuerta.ERROR
                raise Exception(f"Error al cerrar la puerta {self.id}")
            
            self.estado = EstadoPuerta.CERRADA
            print(f"Puerta {self.id} cerrada")
        except Exception as e:
            print(str(e))
        finally:
            self.notificar_observadores()

    def reparar(self) -> None:
        if self.estado == EstadoPuerta.ERROR:
            self.estado = EstadoPuerta.CERRADA
            self.intentos_fallidos = 0
            print(f"Puerta {self.id} reparada")
            self.notificar_observadores() 