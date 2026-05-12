from observer import Observavel

class Reserva(Observavel):
    def __init__(self, sala, usuario, inicio, fim):
        super().__init__()
        self.sala = sala
        self.usuario = usuario
        self.inicio = inicio
        self.fim = fim
        self.tipo_usuario = usuario.tipo_usuario  
        self.status = "confirmada"             

    def cancelar(self):
        self.status = "cancelada"
        self.notificar("cancelamento", {"status": self.status, "reserva": self})

    def modificar(self, novo_inicio, novo_fim):
        self.inicio = novo_inicio
        self.fim = novo_fim
        self.notificar("modificacao", {"inicio": novo_inicio, "fim": novo_fim, "reserva": self})
    
    def descricao(self):
        return f"Reserva | Sala {self.sala.id} | {self.usuario.nome}"

