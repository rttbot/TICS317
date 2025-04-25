import requests
import time
import random
from Sensores import Sensores
from ActuadorPuerta import ActuadorPuerta

class PuertaPerruna:
    def __init__(self, id: str, server_url: str = "http://localhost:5001"):
        self.id = id
        self.server_url = server_url
        self.estado = "cerrada"
        self.sensores = Sensores()
        self.actuador = ActuadorPuerta()
        self.intentos_fallidos = 0
        self.max_intentos = 3
        # Notificar estado inicial
        self._notificar_servidor()

    def _notificar_servidor(self):
        try:
            response = requests.post(
                f"{self.server_url}/api/puerta/estado",
                json={"id": self.id, "estado": self.estado}
            )
            if response.status_code != 200:
                print(f"Error al notificar al servidor: {response.text}")
        except Exception as e:
            print(f"Error de conexión con el servidor: {e}")

    def procesar_ladrido(self, sonido):
        if self.sensores.detectar_ladrido(sonido):
            nuevo_estado = self.actuador.abrir_temporalmente(self.sensores)
            if nuevo_estado == "abierta":
                self.estado = nuevo_estado
                self._notificar_servidor()
                return True
            return False
        return False

    def abrir(self):
        self.estado = self.actuador.abrir()
        print(f"Puerta {self.id} {self.estado}")
        self._notificar_servidor()
        time.sleep(2)
        return self.cerrar()

    def cerrar(self):
        while not self.sensores.es_seguro_cerrar():
            time.sleep(1)
        self.estado = self.actuador.cerrar()
        print(f"Puerta {self.id} {self.estado}")
        self._notificar_servidor()
        return self.estado 