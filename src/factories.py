from models import SalaIndvidual, SalaGrupo, SalaLaboratorio
from abc import ABC, abstractmethod

class SalaFactory:
    @abstractmethod
    def criar_sala(self, id):
        pass

class FactorySalaIndividual(SalaFactory):
    def criar_sala(self, id):
        return SalaIndvidual(id, capacidade=1)
    
class FactorySalaGrupo(SalaFactory):
    def criar_sala(self, id):
        return SalaGrupo(id, capacidade=6)
    
class FactorySalaLaboratorio(SalaFactory):
    def criar_sala(self, id):
        return SalaLaboratorio(id, capacidade=20)