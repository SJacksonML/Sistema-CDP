from modules.lancamentos import Lancamento

class Receita(Lancamento):
    tipo = 'receita'

    def executar(self, saldo):
        # soma o valor ao saldo, tentando analisar ele como objeto ou número e se adequando
        try:
            saldo._alterar_saldo(self.valor)
        except Exception:
            return (saldo or 0) + self.valor

    def __str__(self):
        data = self.data_lancamento
        return (
            f"[RECEITA] {self.descricao} "
            f"| +R${self.valor:.2f} "
            f"| Data: {data}"
        )
