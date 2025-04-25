#!/usr/bin/env python3

class PuertaView:
    """
    La Vista es responsable de:
    1. Mostrar la información al usuario
    2. Formatear los mensajes de manera amigable
    3. Manejar la presentación del estado del sistema
    
    En esta implementación simple, usamos la consola para mostrar mensajes,
    pero en una aplicación real podría ser una interfaz gráfica, web, etc.
    """
    
    # ---- Constantes para formateo ----
    FORMATO_ESTADO = "La puerta está {estado} y {bloqueo}"
    FORMATO_ERROR = "Error: {mensaje}"
    FORMATO_EXITO = "Éxito: {mensaje}"
    
    # ---- Métodos para mostrar el estado de la puerta ----
    def mostrar_estado(self, esta_abierta, esta_bloqueada):
        """
        Muestra el estado actual de la puerta.
        
        Args:
            esta_abierta (bool): True si la puerta está abierta
            esta_bloqueada (bool): True si la puerta está bloqueada
        """
        # Determina el texto según el estado
        estado = "abierta" if esta_abierta else "cerrada"
        bloqueo = "bloqueada" if esta_bloqueada else "desbloqueada"
        
        # Formatea y muestra el mensaje
        mensaje = self.FORMATO_ESTADO.format(
            estado=estado,
            bloqueo=bloqueo
        )
        print(mensaje)
    
    # ---- Métodos para mostrar mensajes al usuario ----
    def mostrar_error(self, mensaje):
        """
        Muestra un mensaje de error al usuario.
        
        Args:
            mensaje (str): El mensaje de error a mostrar
        """
        print(self.FORMATO_ERROR.format(mensaje=mensaje))
    
    def mostrar_exito(self, mensaje):
        """
        Muestra un mensaje de éxito al usuario.
        
        Args:
            mensaje (str): El mensaje de éxito a mostrar
        """
        print(self.FORMATO_EXITO.format(mensaje=mensaje)) 