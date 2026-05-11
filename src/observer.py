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
    def atualizar(self, evento: str, dados: dict | None = None): 
        repo = ReservaRepositorio.get_instance()
        reservas = repo.listar()
        confirmadas = [r for r in reservas if r.status == "confirmada"]

        if not confirmadas:
            print("[Relatório Diário] Nenhuma reserva confirmada.")
        else:
            agrupa = {}
            for r in confirmadas:
                agrupa.setdefault(r.sala.id, []).append(r)

            for sala_id, lista in agrupa.items():
                print(f"\nSala: {sala_id}")
                for r in lista:
                    print(f"  • {r.usuario.nome} ({r.tipo_usuario}) | {r.inicio} → {r.fim}")

            print(f"\nTotal de reservas confirmadas: {len(confirmadas)}")

            