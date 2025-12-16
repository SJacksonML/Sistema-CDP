class Lancamento:
    """Classe Pai que gerencia transações, através de Receita e Despesa"""

    def __init__(self, valor: float, categoria, data_lancamento=None, descricao: str = None, forma_pagamento: str = None):
        self._valor = float(valor)
        self._categoria = categoria
        self._data_lancamento = data_lancamento or date.today().isoformat()
        self._descricao = descricao
        self._forma_pagamento = forma_pagamento

    @property
    def valor(self):
        return self._valor

    @property
    def categoria(self):
        return self._categoria

    @property
    def data_lancamento(self):
        return self._data_lancamento

    @property
    def descricao(self):
        return self._descricao

    @property
    def forma_pagamento(self):
        return self._forma_pagamento

    def __str__(self):
        return f"Lançamento[{self.categoria.nome if self.categoria else 'Sem Categoria'}] " \
               f"{self.descricao or ''} | R${self.valor:.2f} | Data: {self.data_lancamento} | Pagamento: {self.forma_pagamento or 'N/A'}"

    def to_dict(self):
        return {
            'valor': self.valor,
            'categoria': self.categoria.nome if self.categoria else None,
            'data_lancamento': self.data_lancamento,
            'descricao': self.descricao,
            'forma_pagamento': self.forma_pagamento
        }
