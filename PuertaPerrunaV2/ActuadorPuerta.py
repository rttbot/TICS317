import time

class ActuadorPuerta:
    def __init__(self):
        self.estado = "cerrada"

    def abrir(self):
        if self.estado == "cerrada":
            # print("Actuador: abriendo la puerta...")
            self.estado = "abierta"
        else:
            # print("Actuador: la puerta ya está abierta.")
            pass
        return self.estado

    def cerrar(self):
        if self.estado == "abierta":
            # print("Actuador: cerrando la puerta...")
            self.estado = "cerrada"
        else:
            # print("Actuador: la puerta ya está cerrada.")
            pass
        return self.estado

    def abrir_temporalmente(self, sensores):
        if self.estado == "cerrada":
            # print("Actuador: abriendo la puerta temporalmente...")
            self.estado = "abierta"
           
            while True:
                time.sleep(1)  # Esperar 1 segundo
                if not sensores.detectar_movimiento():
                    # print("Actuador: no se detectó movimiento, cerrando la puerta...")
                    self.cerrar()
                    break
                else:
                    # print("Actuador: movimiento detectado, extendiendo el tiempo de espera...")
                    return self.estado
        return self.estado  