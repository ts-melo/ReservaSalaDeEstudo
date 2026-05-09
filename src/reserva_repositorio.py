import threading

class ReservaRepositorio:  
    _instance = None
    _lock = threading.Lock()
    _reservas: list


    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(ReservaRepositorio, cls).__new__(cls)
                    cls._instance._reservas = []

        return cls._instance
    
    @classmethod
    def get_instance(cls):
        return cls()
    
    def adicionar(self, reserva):
        with self._lock:
            self._reservas.append(reserva)
    
    def remover(self, reserva):
        with self._lock:
            self._reservas.remove(reserva)

    def listar(self):
        return list(self._reservas)
    
    

        