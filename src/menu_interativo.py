from reserva_repositorio import ReservaRepositorio
from usuario import Usuario
from reservas import Reserva
from strategies import PoliticaPrimeiroAReservar, PoliticaPrioridadeDocente
from GerenciadorResevas import GerenciadorDeReservas
from observer import Notificar, RelatoriodiarioService
from decorator import  Equipamentos, ServicoLimpeza
from factories import FactorySalaIndividual, FactorySalaGrupo, FactorySalaLaboratorio
def menu_principal():

    repo = ReservaRepositorio.get_instance()
    servico_email = Notificar("secretaria")
    servico_relatorio = RelatoriodiarioService()
    gerenciador = GerenciadorDeReservas(PoliticaPrimeiroAReservar())

    while True:
        print("\n SISTEMA DE RESERVA DE SALAS DE ESTUDO")
        print("1 - Criar reserva (Estudante)")
        print("2 - Criar reserva (Docente)")
        print("3 - Listar reservas")
        print("4 - Cancelar reserva")
        print("5 - Sair")

        op = input("Escolha uma opção: ")

        if op == "1" or op == "2":
            
            tipo_usuario = "Estudante" if op == "1" else "Docente"
            nome_usuario = input("Digite o nome do usuário: ")
            usuario = Usuario(tipo=tipo_usuario, nome=nome_usuario)
            print("\n--- Selecione o Tipo de Sala ---")
            print("1. Sala Individual")
            print("2. Sala de Grupo")
            print("3. Laboratório")
            tipo = input("Escolha o tipo de sala: ")
            sala_id = input("Digite o ID da sala: ")
            inicio = int(input("Digite o horário de início (0-23): "))
            fim = int(input("Digite o horário de término (0-23): "))

            if tipo == "1":
                fabrica = FactorySalaIndividual()
            elif tipo == "2":
                fabrica = FactorySalaGrupo()
            else:
                fabrica = FactorySalaLaboratorio()
            
            sala = fabrica.criar_sala(id=sala_id)
            reserva = Reserva(sala, usuario, inicio, fim)
            reserva.assinar(servico_email)

            print("---ESCOLHA DE ADICIONAIS---")
            print("1. Equipamentos Multimídia")
            print("2. Serviço de Limpeza")
            print("3. Ambos")
            print("4. Nenhum")
            opcionais = input("Opção: ")
            
            if opcionais == "1":
                nova_reserva = Equipamentos(nova_reserva)
            elif opcionais == "2":
                nova_reserva = ServicoLimpeza(nova_reserva)
            elif opcionais == "3":
                nova_reserva = Equipamentos(nova_reserva)
                nova_reserva = ServicoLimpeza(nova_reserva)
            
            print("Processando reserva...")
            if tipo_usuario == "Docente":
                gerenciador.def_politica(PoliticaPrioridadeDocente())
            else:
                gerenciador.def_politica(PoliticaPrimeiroAReservar())
            if gerenciador.processar_reserva(reserva, repo.listar()):
                repo.adicionar(reserva)
                print("Reserva criada com sucesso!")
                print("Descrição da reserva:", reserva.descricao())
            else:
                print("Não foi possível criar a reserva devido a conflitos de horário.")
        
        
        elif op == "3":
            servico_relatorio.atualizar(evento="relatorio_diario")
        elif op == "4":
            nome_usuario = input("Digite o nome do usuário da reserva a cancelar: ")
            reservas = repo.listar()
            reserva_encontrada = False
            for r in reservas:
                if r.usuario.nome == nome_usuario and r.status == "confirmada":
                    r.cancelar()
                    encontrada = True
                    print("Reserva cancelada com sucesso!")
                    break
            if not reserva_encontrada:
                print("Reserva não encontrada ou já cancelada.")
        
        elif op == "5":
            print("encerrando o sistema")
            break

if __name__ == "__main__":    menu_principal()


