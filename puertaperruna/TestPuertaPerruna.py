import unittest
import time
from sistema_puerta_perruna import SistemaPuertaPerruna


# Caso de prueba unitaria para el caso de uso "salir de casa"
class TestPuertaPerruna(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaPuertaPerruna()

    def test_salir_de_casa(self):
        # Paso 1: El perro ladra dos veces frente a la puerta para poder salir
        self.sistema.procesar_ladrido("Guau Guau")
        
        # Paso 2: Verificar que la puerta se abre
        self.assertEqual(self.sistema.actuador.estado, "abierta")
        
        # Paso 3: Simular que el perro sale y la puerta se cierra
        time.sleep(6)  # Esperar más de 5 segundos para el cierre automático
        self.assertEqual(self.sistema.actuador.estado, "cerrada")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
