
import threading
import time
import random


class Sensores:
    def detectar_ladrido(self, sonido):
        print(f"Sensores: detectando sonido '{sonido}'...")
        if "Guau" in sonido:
            print("Sensores: ladrido reconocido.")
            return True
        print("Sensores: sonido no reconocido.")
        return False

    def es_seguro_cerrar(self):
        print("Sensores: verificando seguridad...")
        if random.random() > 0.2:
            print("Sensores: es seguro cerrar.")
            return True
        print("Sensores: movimiento detectado. No es seguro cerrar.")
        return False


class ActuadorPuerta:
    def __init__(self):
        self.estado = "cerrada"

    def abrir(self):
        if self.estado == "cerrada":
            print("Actuador: abriendo la puerta...")
            self.estado = "abierta"
        else:
            print("Actuador: la puerta ya está abierta.")

    def cerrar(self):
        if self.estado == "abierta":
            print("Actuador: cerrando la puerta...")
            self.estado = "cerrada"
        else:
            print("Actuador: la puerta ya está cerrada.")


class SistemaPuertaPerruna:
    def __init__(self):
        self.sensores = Sensores()
        self.actuador = ActuadorPuerta()

    def procesar_ladrido(self, sonido):
        if self.sensores.detectar_ladrido(sonido):
            self.actuador.abrir()
            self._iniciar_cierre_automatico()

    def _iniciar_cierre_automatico(self):
        def cierre_automatico():
            time.sleep(5)  # Esperar antes de cerrar
            while not self.sensores.es_seguro_cerrar():
                time.sleep(1)  # Revisar cada segundo
            self.actuador.cerrar()

        threading.Thread(target=cierre_automatico).start()
