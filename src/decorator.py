from reservas import Reserva
from abc import ABC, abstractmethod

class ReservaDecorator(ABC):
    def __init__(self, reserva):
        self._reserva = reserva

    def descricao(self):
        return self._reserva.descricao()
    
    def __getattr__(self, nome):
        return getattr(self._reserva, nome)
    
    def cancelar(self):
        self._reserva.cancelar()
        self.notificar_equipe("cancelamento")

    def modificar(self, novo_inicio, novo_fim):
        self._reserva.modificar(novo_inicio, novo_fim)
        self.notificar_equipe("modificacao")

    @abstractmethod
    def notificar_equipe(self, evento: str):
        pass

class Equipamentos(ReservaDecorator):
    def descricao(self):
        return f"{self._reserva.descricao()} + Equipamentos adicionais"
    
    def notificar_equipe(self, evento: str):
        print(f"Equipe de suporte notificada sobre {evento} para a reserva."
              f"na sala {self._reserva.sala.id} "
              f"({self._reserva.inicio} → {self._reserva.fim}).")

class ServicoLimpeza(ReservaDecorator):
    def descricao(self):
        return f"{self._reserva.descricao()} + Serviço de limpeza"
    
    def notificar_equipe(self, evento: str):
        print(f"Equipe de limpeza notificada sobre {evento} para a reserva."
              f"na sala {self._reserva.sala.id} "
              f"({self._reserva.inicio} → {self._reserva.fim}).")




