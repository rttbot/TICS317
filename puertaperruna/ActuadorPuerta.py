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