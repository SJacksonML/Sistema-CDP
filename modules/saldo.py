class Saldo:
    def __init__(self):
        self.__saldo = 0.0     # atributo privado

    @property
    def saldo(self):
        """Getter do saldo (somente leitura externa)."""
        return self.__saldo

    def _alterar_saldo(self, valor):
        """Usado internamente pelas classes de Receita/Despesa."""
        self.__saldo += valor

    def __str__(self):
        return f"Saldo atual: R${self.__saldo: .2f}"
