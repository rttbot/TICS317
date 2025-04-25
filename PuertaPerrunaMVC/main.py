#!/usr/bin/env python3

from modelo import PuertaModel
from vista import PuertaView
from controlador import PuertaController

def main():
    # Crear instancias de MVC
    modelo = PuertaModel()
    vista = PuertaView()
    controlador = PuertaController(modelo, vista)
    
    # Demostración de uso
    print("\n=== Demostración de la Puerta Perruna ===")
    controlador.actualizar_vista()
    
    print("\n1. Intentando abrir la puerta...")
    controlador.abrir_puerta()
    
    print("\n2. Cerrando la puerta...")
    controlador.cerrar_puerta()
    
    print("\n3. Bloqueando la puerta...")
    controlador.bloquear_puerta()
    
    print("\n4. Intentando abrir la puerta bloqueada...")
    controlador.abrir_puerta()
    
    print("\n5. Desbloqueando la puerta...")
    controlador.desbloquear_puerta()
    
    print("\n6. Abriendo la puerta nuevamente...")
    controlador.abrir_puerta()

if __name__ == "__main__":
    main() 