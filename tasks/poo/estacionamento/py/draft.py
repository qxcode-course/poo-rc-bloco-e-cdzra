from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, id: str, tipo: str, horaEntrada: int):
        self.id = id
        self.tipo = tipo
        self.horaEntrada = horaEntrada

    def getEntrada(self) -> int:
        return self.horaEntrada
    def getTipo(self) -> str:
        return self.tipo
    def getId(self) -> str:
        return self.id

    def setEntrada(self, hora: int) -> None:
        self.horaEntrada = hora

    @abstractmethod
    def calcularValor(self, horaSaida: int):
        pass

    def __str__(self):
        id_fmt = self.id.rjust(10, "_")
        tipo_fmt = self.tipo.rjust(10, "_")
        return f"{tipo_fmt} : {id_fmt} : {self.horaEntrada}"


class Bike(Veiculo):
    def __init__(self, id, horaEntrada: int):
        super().__init__(id, "Bike", horaEntrada)

    def calcularValor(self, horaSaida: int = 0) -> float:
        return 3.00


class Moto(Veiculo):
    def __init__(self, id, horaEntrada: int):
        super().__init__(id, "Moto", horaEntrada)

    def calcularValor(self, horaSaida: int) -> float:
        tempo = horaSaida - self.getEntrada()
        return tempo / 20

class Carro(Veiculo):
    def __init__(self, id: str, horaEntrada: int):
        super().__init__(id,"Carro", horaEntrada)

    def calcularValor(self, horaSaida: int) -> float:
        tempo = horaSaida - self.getEntrada()
        valor = tempo / 10
        return max(valor, 5.00)


class Estacionamento:
    def __init__(self, horaAtual: int = 0):
        self.veiculos: list[Veiculo] = []
        self. horaAtual = horaAtual

    def procucarVeiculo(self, id: str):
        for veiculos in self.veiculos:
            if veiculos.id == id:
                return veiculos
        return None


    def estacionarVeiculo(self, veiculo: Veiculo):
        self.veiculos.append(veiculo)

    def pagar(self, id: str) -> None:
        veiculo = self.procucarVeiculo(id)

        if not veiculo:
            print("veiculo não encontrado")
            return
        entrada = veiculo.getEntrada()
        saida = self.horaAtual
        valor = veiculo.calcularValor(saida)
        print(f"{veiculo.getTipo()} chegou {entrada} saiu {saida}. Pagar R$ {valor:.2f}")


    def sair(self, id: str):
        veiculo = self.procucarVeiculo(id)
        if not veiculo:
            print("veiculo não encontrado")
            return
        valor = veiculo.calcularValor(id)
        self.veiculos.remove(veiculo)
        print(f"veiculo: {id} saiu. Valor pago: R$: {valor:.2f}")

    def passarTempo(self, tempo: int) -> None:
        self.horaAtual += tempo

    def __str__(self):
        if not self.veiculos:
            return f"Hora atual: {self.horaAtual}"
        listVeiculos = "\n".join(str(x) for x in self.veiculos)
        return f"{listVeiculos}\nHora atual: {self.horaAtual}"

def main():
    estacionar = Estacionamento()

    while True:

        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(estacionar)
        elif args[0] == "tempo":
            estacionar.passarTempo(int(args[1]))
        elif args[0] == "estacionar":
            if args[1] == "bike":
                estacionar.estacionarVeiculo(Bike(args[2], estacionar.horaAtual))
            if args[1] == "moto":
                estacionar.estacionarVeiculo(Moto(args[2], estacionar.horaAtual))
            if args[1] == "carro":
                estacionar.estacionarVeiculo(Carro(args[2], estacionar.horaAtual))
        elif args[0] == "pagar":
            estacionar.pagar(args[1])
        else:
            print("fail: comando invalido!!!")
main()