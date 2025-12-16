from modules.lancamentos import Lancamento

class Despesa(Lancamento):
    tipo = 'despesa'

    # implementando algumas RN:
    def __init__(self, valor, categoria, data_lancamento=None, descricao: str = None, forma_pagamento: str = None):
            if valor <= 0:
                raise ValueError("Despesa não pode ter valor menor ou igual a zero.")
            if categoria is None:
                raise ValueError("Despesa deve possuir uma categoria.")
            if not hasattr(categoria, 'nome'):
                raise TypeError("Categoria inválida: deve ser um objeto com atributo 'nome' (ex.: Categoria).")

            super().__init__(valor, categoria, data_lancamento, descricao, forma_pagamento)

    def executar(self, saldo):
        # tipo receita, soma o valor ao saldo, analisa ele como objeto ou número e se adequa
        try:
            saldo._alterar_saldo(-self.valor)
        except Exception:
            return (saldo or 0) - self.valor

    def __str__(self):
        data = self.data_lancamento
        return (
            f"[DESPESA] {self.descricao} "
            f"| -R${self.valor:.2f} "
            f"| Data: {data}"
        )
