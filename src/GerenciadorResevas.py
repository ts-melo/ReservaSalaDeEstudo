from strategies import PoliticaDeReserva
class GerenciadorDeReservas:
    def __init__(self, politica :PoliticaDeReserva):
        self.politica = politica
    
    def def_politica(self, nova_politica: PoliticaDeReserva):
        self.politica = nova_politica
    def processar_reserva(self, nova_reserva, reservas_existentes):
        valido, mensagem = self.politica.validar_reserva(nova_reserva, reservas_existentes)
        if valido:
            print("Reserva processada com sucesso:", mensagem)
            return True
        else:
            print("Reserva negada:", mensagem)
            return False