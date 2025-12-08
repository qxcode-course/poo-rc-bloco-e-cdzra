from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    @abstractmethod
    def apresentar_nome(self) -> str:
        pass

    @abstractmethod
    def fazer_som(self) -> str:
        pass

    @abstractmethod
    def mover(self) -> str:
        pass

def apresentar(animal: Animal):
    print(animal.apresentar_nome())
    print(animal.fazer_som())
    print(animal.mover())

class Leao(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentar_nome(self):
        return f"Eu sou um(a) <{self.getNome()}>"
    
    def fazer_som(self):
        return "RAWWWWRRR"
    
    def mover(self):
        return "Cuidado nao viu, que esse leao ta com fome"
    
class Coruja(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentar_nome(self):
        return f"Eu sou um(a) <{self.getNome()}>"
    
    def fazer_som(self):
        return "u"
    
    def mover(self):
        return "As asas batem silenciosamente"
    
class Girafa(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentar_nome(self):
        return f"Eu sou um(a) <{self.getNome()}>"
    
    def fazer_som(self):
        return "(barulhos de girafa)"
    
    def mover(self):
        return "(barulhos de corrida de girafa)"
    
animais: list[Animal] = [Leao("Leao"), Coruja("Coruja"), Girafa("Girafa")]

for animal in animais:
    print(animal.apresentar_nome())
    print(animal.fazer_som())
    print(animal.mover())
    print("\n")