from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str, horaEntrada: int):
        self.__id = id
        self.tipo = tipo
        self.horaEntrada = horaEntrada

    def setEntrada(self, hora: int):
        self.horaEntrada += hora

    def getEntrada(self):
        return self.horaEntrada

    def getTipo(self):
        return self.tipo
    
    def getId(self):
        return self.__id

    @abstractmethod
    def CalcularValor(self, horaSaida: int):
        pass

    def __str__(self):
        return f"{self.__id} : {self.tipo}"
    
class Estacionamento:
    def __init__(self):
        self.veiculo: list[Veiculo] = []
        self.hrAtual = 0

class Bike(Veiculo):
    def __init__(self,id: str, tipo: str, horaEntrada: int):
        super().__init__(id, tipo, horaEntrada)

    def CalcularValor(self, horaSaida: int):


class Carro(Veiculo):
    def __init__(self, id: str, tipo: str, horaEntrada: int):
        super().__init__(id, tipo, horaEntrada)

    def CalcularValor(self, horaSaida: int):