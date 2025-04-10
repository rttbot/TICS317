import threading
import time
from Sensores import Sensores
from ActuadorPuerta import ActuadorPuerta


class SistemaPuertaPerruna:
    def __init__(self):
        self.sensores = Sensores()
        self.actuador = ActuadorPuerta()

    def procesar_ladrido(self, sonido):
        if self.sensores.detectar_ladrido(sonido):
            return self.actuador.abrir_temporalmente(self.sensores)
        return False

    def _iniciar_cierre_automatico(self):
        # Esperar un tiempo inicial antes de verificar el movimiento
        time.sleep(5)
        # Verificar si hay movimiento después de abrir la puerta
        if self.sensores.detectar_movimiento():
            print("Movimiento detectado, extendiendo el tiempo de espera...")
            time.sleep(10)  # Extender el tiempo de espera
        # Verificar si es seguro cerrar
        while not self.sensores.es_seguro_cerrar():
            time.sleep(1)  # Revisar cada segundo
        self.actuador.cerrar()
