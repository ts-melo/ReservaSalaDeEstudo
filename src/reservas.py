
class Reserva:
    def __init__(self, sala, usuario, inicio, fim):
        self.sala = sala
        self.usuario = usuario
        self.inicio = inicio
        self.fim = fim
        self.tipo_usuario = usuario.tipo_usuario