from factories import FactorySalaIndividual, FactorySalaLaboratorio
from usuario import Usuario
from reservas import Reserva
from reserva_repositorio import ReservaRepositorio
from strategies import PoliticaPrimeiroAReservar, PoliticaPrioridadeDocente
from GerenciadorResevas import GerenciadorDeReservas
from observer import Notificar, RelatoriodiarioService
from decorator import Equipamentos, ServicoLimpeza
def main():
    # uso do singleton
    repo = ReservaRepositorio.get_instance()
    gerenciador = GerenciadorDeReservas(PoliticaPrimeiroAReservar())

    servico_email = Notificar("secretaria")
    servico_relatorio = RelatoriodiarioService()


    #cria salas
    fabrica_sala_individual = FactorySalaIndividual()
    fabrica_lab = FactorySalaLaboratorio()

    sala_estudo_1 = fabrica_sala_individual.criar_sala(id="Sala-01")
    laboratorio = fabrica_lab.criar_sala(id="Lab-01")
    print("sala criada:" + sala_estudo_1.especificacao())
    print("laboratorio criado:", laboratorio.especificacao())

    #cria usuarios
    usuario_aluno = Usuario(tipo = "Estudante", nome ="Joao")
    usuario_docente = Usuario(tipo = "Docente", nome = "Maria")

    #faz reservas

    ##reserva valida
    reserva1 = Reserva(sala_estudo_1, usuario_aluno, inicio = 10, fim = 12)
    reserva1.assinar(servico_email)

    if gerenciador.processar_reserva(reserva1, repo.listar()):
        repo.adicionar(reserva1)

    ##reserva conflitante
    reserva2 = Reserva(sala_estudo_1, usuario_docente, inicio = 11, fim = 13)
    if not gerenciador.processar_reserva(reserva2, repo.listar()):
        print("Tentativa de reserva conflitante de horario para", reserva2.sala.id)

    reserva_equipada = Equipamentos(reserva1)
    reserva_completa = ServicoLimpeza(reserva_equipada)
    print("Descrição da reserva completa:", reserva_completa.descricao())
    
    #troca de politica para prioridade docente
    gerenciador.def_politica(PoliticaPrioridadeDocente())
    if gerenciador.processar_reserva(reserva2, repo.listar()):
        repo.adicionar(reserva2)
        reserva2.assinar(servico_email)
        print("Reserva de docente processada com prioridade, mesmo com conflito de horario.")

    reserva1.cancelar()

    servico_relatorio.atualizar(evento="relatorio_diario")


if __name__ == "__main__":
    main()