#!/usr/bin/env python3

class PuertaController:
    """
    El Controlador tiene 3 responsabilidades principales:
    1. Recibir acciones del usuario (desde la vista)
    2. Coordinar con el modelo para ejecutar esas acciones
    3. Actualizar la vista con los resultados
    """
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    # ---- Manejo de Acciones del Usuario ----
    def abrir_puerta(self):
        # 1. Intenta realizar la acción en el modelo
        exito = self.model.abrir()
        
        # 2. Según el resultado, muestra mensaje apropiado
        if exito:
            self.view.mostrar_exito("Puerta abierta correctamente")
        else:
            self.view.mostrar_error("No se puede abrir una puerta bloqueada")
        
        # 3. Actualiza la vista con el nuevo estado
        self.actualizar_vista()
    
    def cerrar_puerta(self):
        # 1. Ejecuta la acción en el modelo
        self.model.cerrar()
        
        # 2. Notifica el resultado
        self.view.mostrar_exito("Puerta cerrada correctamente")
        
        # 3. Actualiza la vista
        self.actualizar_vista()
    
    
    
    # ---- Actualización de la Vista ----
    def actualizar_vista(self):
        # Obtiene el estado actual del modelo
        esta_abierta = self.model.esta_abierta()
        esta_bloqueada = self.model.esta_bloqueada()
        
        # Actualiza la vista con el estado actual
        self.view.mostrar_estado(esta_abierta, esta_bloqueada) 
    


    def bloquear_puerta(self):
        # 1. Ejecuta la acción en el modelo
        self.model.bloquear()
        
        # 2. Notifica el resultado
        self.view.mostrar_exito("Puerta bloqueada correctamente")
        
        # 3. Actualiza la vista
        self.actualizar_vista()
    
    def desbloquear_puerta(self):
        # 1. Ejecuta la acción en el modelo
        self.model.desbloquear()
        
        # 2. Notifica el resultado
        self.view.mostrar_exito("Puerta desbloqueada correctamente")
        
        # 3. Actualiza la vista
        self.actualizar_vista()