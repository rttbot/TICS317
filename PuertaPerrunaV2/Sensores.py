import random


class Sensores:
    def detectar_ladrido(self, sonido):
        # print(f"Sensores: detectando sonido '{sonido}'...")
        if "Guau" in sonido:
            # print("Sensores: ladrido reconocido.")
            return True
        # print("Sensores: sonido no reconocido.")
        return False

    def es_seguro_cerrar(self):
        # print("Sensores: verificando seguridad...")
        if random.random() > 0.2:
            # print("Sensores: es seguro cerrar.")
            return True
        # print("Sensores: movimiento detectado. No es seguro cerrar.")
        return False

    def detectar_movimiento(self):
        # print("Sensores: verificando movimiento...")
        # Simular detección de movimiento con una probabilidad
        if random.random() > 0.3:
            # print("Sensores: movimiento detectado.")
            return True
        # print("Sensores: no se detectó movimiento.")
        return False 