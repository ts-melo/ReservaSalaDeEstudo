from abc import ABC, abstractmethod

##classes pra fabrica

class Sala(ABC):
    def __init__(self, id, capacidade):
        self.id = id
        self.capacidade = capacidade
        self.tipo = self.__class__.__name__
    
    @abstractmethod
    def especificacao(self):
        pass

class SalaIndividual(Sala):
    def especificacao(self):
        return f"Sala Individual - ID: {self.id}, Capacidade: {self.capacidade}"

class SalaGrupo(Sala):
    def especificacao(self):
        return f"Sala de Grupo - ID: {self.id}, Capacidade: {self.capacidade}"
    
class SalaLaboratorio(Sala):
    def especificacao(self):
        return f"Sala de Laboratório - ID: {self.id}, Capacidade: {self.capacidade}"