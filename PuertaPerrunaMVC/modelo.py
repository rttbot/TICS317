#!/usr/bin/env python3

class PuertaModel:
    """
    Modelo de la Puerta Perruna que contiene:
    1. Atributos (datos/estado)
    2. Lógica de negocio (reglas sobre cómo opera la puerta)
    """
    
    # ---- Atributos (Estado) ----
    def __init__(self):
        # Estado interno de la puerta
        self._esta_abierta = False
        self._esta_bloqueada = False
    
    # ---- Consultas de Estado ----
    def esta_abierta(self):
        return self._esta_abierta
    
    def esta_bloqueada(self):
        return self._esta_bloqueada
    
    # ---- Lógica de Negocio ----
    def puede_abrir(self):
        # Regla de negocio: solo se puede abrir si no está bloqueada
        return not self._esta_bloqueada
    
    def abrir(self):
        # Lógica de negocio para abrir la puerta
        if self.puede_abrir():
            self._esta_abierta = True
            return True
        return False
    
    def cerrar(self):
        # Lógica de negocio para cerrar la puerta
        # Siempre se puede cerrar, sin importar si está bloqueada
        self._esta_abierta = False
        return True
    
    def bloquear(self):
        # Lógica de negocio para bloquear la puerta
        self._esta_bloqueada = True
        return True
    
    def desbloquear(self):
        # Lógica de negocio para desbloquear la puerta
        self._esta_bloqueada = False
        return True 