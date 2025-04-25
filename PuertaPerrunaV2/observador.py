from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def actualizar(self, puerta_id: str, estado: str) -> None:
        pass 