from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao
        self.validar_valor()

    def resumo(self) -> str:
        return f"pagamento de R$ <{self.valor:2f}>:<{self.descricao}>"
    
    def validar_valor(self):
        if self.valor <= 0:
            raise ValueError("o valor do pagamento deve ser maior que zero.")
        
    @abstractmethod
    def processar(self):
        pass

def processar_pagamento(pagamento: Pagamento):
    pagamento.validar_valor()
    pagamento.resumo()
    pagamento.processar()

class CartaoCredito(Pagamento):
    def __init__(self, valor: float, descricao: str, numero: str, nome_titular: str, limite_disponivel: float):
        super().__init__(valor, descricao)
        self.numero = numero
        self.nome_titular = nome_titular
        self.limite_disponivel = limite_disponivel

    def processar(self):
        if self.valor > self.limite_disponivel:
            print("Pagamento recusado")
        else:
            self.limite_disponivel -= self.valor
            print("Pagamento aprovado!")

class Pix(Pagamento):
    def __init__(self, valor: float, descricao: str, chave: str, banco: str):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco

    def processar(self):
        print(f"valor da transacao aceita {self.banco}:{self.chave}")

class Boleto(Pagamento):
    def __init__(self, valor: float, descricao: str, codigo_barras: str, vencimento: str):
        super().__init__(valor, descricao)
        self.codigo_barras = codigo_barras
        self.vencimento = vencimento


    def processar(self):
        print("Boleto gerado. Aguardando pagamento...")

pagamentos = [Pix(150, "Camisa esportiva", "emailluczzz@gmail.com","Nubs"),
             CartaoCredito(400, "Tênis esportivo", "1234 5678 9123 4567", "Marquin do grau",500),
             Boleto(89.90, "livro de Aventura", "123456789000", "2025-01-10"),
             CartaoCredito(800, "Notebook", "9999 8888 7777 6666", "Cliente Y", 700)]


for pagamento in pagamentos:
    try:
        processar_pagamento(pagamento)
    except Exception as e:
        print("ERRO PAGAMENTO INVALIDO", e)