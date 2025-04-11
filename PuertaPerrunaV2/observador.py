from abc import ABC, abstractmethod
from enum import Enum

class EstadoPuerta(Enum):
    ABIERTA = "abierta"
    CERRADA = "cerrada"
    ERROR = "error"

class Observador(ABC):
    @abstractmethod
    def actualizar(self, puerta_id: str, estado: EstadoPuerta) -> None:
        pass 