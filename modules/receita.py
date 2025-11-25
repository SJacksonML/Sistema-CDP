from .lancamentos import Lancamento

class Receita(Lancamento):
    """Classe que representa uma entrada de dinheiro."""

    def executar(self, saldo):
        saldo._alterar_saldo(self._valor)

    def __str__(self):
        return f"[RECEITA] {self.descricao}: +R${self.valor:.2f}"
