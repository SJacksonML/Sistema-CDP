from modules.lancamentos import Lancamento

class Despesa(Lancamento):
    tipo = 'despesa'

    def executar(self, saldo):
        # tipo receita, soma o valor ao saldo, analisa ele como objeto ou número e se adequa
        try:
            saldo._alterar_saldo(-self.valor)
        except Exception:
            return (saldo or 0) - self.valor

    def __str__(self):
        return f"[DESPESA] {self.descricao or ''}: -R${self.valor:.2f}"
