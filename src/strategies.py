from abc import ABC, abstractmethod

class PoliticaDeReserva(ABC):
    @abstractmethod
    def validar_reserva(self, nova_reserva, reservas_existentes):
        pass

class PoliticaSimples(PoliticaDeReserva):
    def validar_reserva(self, nova_reserva, reservas_existentes):
        for reserva in reservas_existentes:
            if reserva.sala.id == nova_reserva.sala.id and reserva.horario == nova_reserva.horario:
                return False, "[Conflito de reserva]: Sala {reserva.sala.id} já reservada para o horário {reserva.horario}."
        return True, "Reserva autorizada."
    

class PoliticaPrimeiroAReservar(PoliticaDeReserva):
    def validar_reserva(self, nova_reserva, reservas_existentes):
        for res in reservas_existentes:
            if nova_reserva.inicio < res.fim and res.inicio < nova_reserva.fim:
                return False, "[Conflito de Reserva]: Conflito de horário detectado."
        return True, "Reserva autorizada."
    
class PoliticaPrioridadeDocente(PoliticaDeReserva):
    def validar_reserva(self, nova_reserva, reservas_existentes):
        for res in reservas_existentes:
            if nova_reserva.inicio < res.fim and res.inicio < nova_reserva.fim:
                if nova_reserva.tipo_usuario == "Docente" and res.tipo_usuario != "Docente":
                    return True, "Reserva autorizada para docente."
                elif nova_reserva.tipo_usuario != "Docente" and res.tipo_usuario == "Docente":
                    return False, "[Conflito de Reserva]: Docente tem prioridade sobre outros usuários."
                else:
                    return False, "[Conflito de Reserva]: Conflito de horário detectado."
        return True, "Reserva autorizada."