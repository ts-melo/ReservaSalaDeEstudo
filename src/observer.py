from abc import ABC, abstractmethod
from reserva_repositorio import ReservaRepositorio

class Observador(ABC):
    @abstractmethod
    def atualizar(self, evento: str, dados=None):   # dados = push
        pass
        
class Observavel:
    def __init__(self):
        self._observadores: list[Observador] = []

    def assinar(self, obs: Observador):
        self._observadores.append(obs)

    def cancelar_assinatura(self, obs: Observador):
        self._observadores.remove(obs)

    def notificar(self, evento: str, dados=None):   # push: passa dados direto
        for obs in self._observadores:
            obs.atualizar(evento, dados)

class Reserva(Observavel):
    def __init__(self, sala, usuario, inicio, fim):
        super().__init__()
        self.sala = sala
        self.usuario = usuario
        self.inicio = inicio
        self.fim = fim
        self.status = "confirmada"

    def cancelar(self):
        self.status = "cancelada"
        self.notificar("cancelamento", {"status": self.status, "reserva": self})

    def modificar(self, novo_inicio, novo_fim):
        self.inicio = novo_inicio
        self.fim = novo_fim
        self.notificar("modificacao", {"inicio": novo_inicio, "fim": novo_fim, "reserva": self})

class Notificar(Observador):
    def __init__(self, nome):
        self.nome = nome
    
    def atualizar(self, evento: str, dados: dict | None = None):
        if dados is None:
            return
        
        if evento == "cancelamento":
            print(f"[Notificação] {self.nome}: sua reserva foi {dados['status']}.")
        elif evento == "modificacao":
            print(f"[Notificação] {self.nome}: reserva alterada → {dados['inicio']} até {dados['fim']}.")

class RelatoriodiarioService(Observador):
    def atualizar(self, evento: str, dados=None):
        repo = ReservaRepositorio.get_instance()   
        reservas = repo.listar()
        print(f"[Relatório] Evento '{evento}' detectado. Total de reservas: {len(reservas)}.")