class Lancamento:
    """Classe base utilizada por Receita e Despesa."""

    def __init__(self, valor, nome_categoria, data_lancamento, descricao, forma_pagamento):
        self._valor = float(valor)
        self.nome_categoria = nome_categoria
        self.data_lancamento = data_lancamento
        self.descricao = descricao
        self.forma_pagamento = forma_pagamento

    @property
    def valor(self):
        return self._valor

    def executar(self, saldo):
        """Deve ser implementado por subclasses."""
        raise NotImplementedError()

    def __str__(self):
        return (
            f"Lançamento[{self.nome_categoria}] "
            f"{self.descricao} | R${self.valor:.2f} | "
            f"Data: {self.data_lancamento} | Pagamento: {self.forma_pagamento}"
        )

    def __repr__(self):
        return (
            f"Lancamento(valor={self._valor}, "
            f"categoria='{self.nome_categoria}', "
            f"descricao='{self.descricao}')"
        )

    def __eq__(self, other):
        return (
            isinstance(other, Lancamento) and
            self._valor == other._valor and
            self.nome_categoria == other.nome_categoria and
            self.descricao == other.descricao and
            self.data_lancamento == other.data_lancamento
        )
