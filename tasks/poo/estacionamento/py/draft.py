from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str):
        self.__id = id
        self.tipo = tipo
        self.horaEntrada = 0

    def setEntrada(self, hora: int):
        self.horaEntrada += hora

    def getEntrada(self):
        return self.horaEntrada

    def getTipo(self):
        return self.tipo
    
    def getId(self):
        return self.__id

    @abstractmethod
    def CalcularValor(self, horaSaida: int) -> float:
        pass

    def __str__(self):
        return f"{self.__id} : {self.tipo}"
    
class Estacionamento:
    def __init__(self):
        self.veiculo: list[Veiculo] = []
        self.hrAtual = 0

    def procurar(self, id: str):
        for i, v in enumerate(self.veiculo):
            if v.getId() == id:
                return i
            return -1
        
    def estacionar(self, veiculo: Veiculo):
        veiculo.setEntrada(self.hrAtual)
        self.veiculo.append(veiculo)

    def pagar(self, id: str):
        pos = self.procurar(id)
        if pos == -1:
            print("fail: veiculo nao encontrado")
            return
        v = self.veiculo[pos]
        valor = v.CalcularValor(self.hrAtual)
        print(f"Valor a pagar: R$ {valor:.2f}")

    def sair(self, id: str):
        pos = self.procurar(id)
        if pos == -1:
            print("fail: veiculo nao encontrado")
            return
        v = self.veiculo[pos]
        valor = v.CalcularValor(self.hrAtual)
        self.veiculo.pop(pos)
        print(f"Veículo saiu. Total pago: R$ {valor:.2f}")

    def passarTempo(self, tempo: int):
        self.hrAtual += tempo

    def __str__(self):
        

class Bike(Veiculo):
    def __init__(self,id: str):
        super().__init__(id, "Bike")

    def CalcularValor(self, horaSaida: int) -> float:
        return 3.0

class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Moto")

    def CalcularValor(self, horaSaida: int) -> float:
        tempo = horaSaida - self.horaEntrada
        if tempo < 0:
            tempo = 0
            return tempo / 20
        
class Carro(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Carro")

    def CalcularValor(self, horaSaida: int) -> float:
        tempo = horaSaida - self.horaEntrada
        if tempo < 0:
            tempo = 0
            valor = tempo / 10
            return max(valor, 5.0)
        
def main():
    estac = Estacionamento()
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(estac)