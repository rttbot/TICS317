from observador import Observador
from observable import Observable
from typing import List
import time 
from Sensores import Sensores
from ActuadorPuerta import ActuadorPuerta


class PuertaPerruna(Observable):
    def __init__(self, id: str):
        self.id = id
    
        self.observadores: List[Observador] = []
        self.sensores = Sensores()
        self.actuador = ActuadorPuerta()
        self.intentos_fallidos = 0
        self.max_intentos = 3
        self.estado = "cerrada"
        

    def procesar_ladrido(self, sonido):
        if self.sensores.detectar_ladrido(sonido):
            if self.actuador.abrir_temporalmente(self.sensores)=="abierta":
                self.notificar_observadores() 
                return True
            else:
                return False
        return False

    def _iniciar_cierre_automatico(self):
        # Esperar un tiempo inicial antes de verificar el movimiento
        time.sleep(5)
        # Verificar si hay movimiento después de abrir la puerta
        if self.sensores.detectar_movimiento():
            # print("Movimiento detectado, extendiendo el tiempo de espera...")
            time.sleep(10)  # Extender el tiempo de espera
        # Verificar si es seguro cerrar
        while not self.sensores.es_seguro_cerrar():
            time.sleep(1)  # Revisar cada segundo
        self.estado=self.actuador.cerrar()
        self.notificar_observadores() 

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
      
            self.estado=self.actuador.abrir()
            print(f"Puerta {self.id} abierta")
            time.sleep(2)  # La puerta permanece abierta por 2 segundos
            self.notificar_observadores()  # Notificar después de abrir
            self.estado=self.cerrar()
            self.notificar_observadores() 
            

    def cerrar(self) -> None:
        self.estado = self.actuador.cerrar()
        print(f"Puerta {self.id} cerrada")
        self.notificar_observadores()  # Notificar después de cerrar
        return self.estado