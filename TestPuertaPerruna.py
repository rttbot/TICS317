import unittest

# Simulación de las funciones del sistema PuertaPerruna
def reconocer_ladrido(ladrido):
    # Simulación de reconocimiento de ladrido con una precisión del 98%
    return ladrido == "ladrido_perro_registrado"

def abrir_puerta():
    return "puerta_abierta"

def cerrar_puerta():
    return "puerta_cerrada"

def es_seguro_cerrar():
    # Simulación de verificación de seguridad
    return True

def estado_puerta():
    # Simulación del estado de la puerta
    return "cerrada"

# Caso de prueba unitaria para el caso de uso "salir de casa"
class TestPuertaPerruna(unittest.TestCase):
    def test_salir_de_casa(self):
        # Paso 1: El perro ladra dos veces frente a la puerta para poder salir
        ladrido = "ladrido_perro_registrado"
        self.assertTrue(reconocer_ladrido(ladrido))
        
        # Paso 2: El sensor de ladridos reconoce el ladrido del perro y envía la petición a la puerta para que se abra
        self.assertEqual(abrir_puerta(), "puerta_abierta")
        
        # Paso 3: La puerta se abre
        self.assertEqual(estado_puerta(), "cerrada")  # Simulación del estado inicial
        
        # Paso 4: El perro sale (simulación)
        
        # Paso 5: La puerta espera X segundos y se cierra lentamente volviéndose a abrir si detecta que aún hay movimiento y no es seguro cerrarse
        if es_seguro_cerrar():
            self.assertEqual(cerrar_puerta(), "puerta_cerrada")
        else:
            self.assertEqual(abrir_puerta(), "puerta_abierta")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
