from abc import ABC, abstractmethod

class Observable(ABC):
    @abstractmethod
    def agregar_observador(self, observador) -> None:
        pass

    @abstractmethod
    def eliminar_observador(self, observador) -> None:
        pass

    @abstractmethod
    def notificar_observadores(self) -> None:
        pass 