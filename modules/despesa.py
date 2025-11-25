from .lancamentos import Lancamento

class Despesa(Lancamento):
    """Classe que representa uma saída de dinheiro."""

    def executar(self, saldo):
        saldo._alterar_saldo(-self._valor)

    def __str__(self):
        return f"[DESPESA] {self.descricao}: -R${self.valor:.2f}"
