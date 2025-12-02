from datetime import date

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

    @valor.setter
    def valor(self, novo_valor):
        novo = float(novo_valor)
        if novo < 0:
            raise ValueError('Valor não pode ser negativo.')
        self._valor = novo

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, nova_categoria):
        self._categoria = nova_categoria

    @property
    def data_lancamento(self):
        return self._data_lancamento

    @data_lancamento.setter
    def data_lancamento(self, nova_data):
        if hasattr(nova_data, 'isoformat'):
            self._data_lancamento = nova_data.isoformat()
        else:
            self._data_lancamento = str(nova_data)

    @property
    def descricao(self):
        return self._descricao

    @property
    def forma_pagamento(self):
        return self._forma_pagamento

    def executar(self, saldo):
        """Deve ser implementado por subclasses."""
        raise NotImplementedError('Subclasse deve implementar executar(saldo)')

    def to_dict(self):
        return {
            'tipo': getattr(self, 'tipo', None),
            'valor': self.valor,
            'categoria': self.categoria.nome if self.categoria else None,
            'data_lancamento': self.data_lancamento,
            'descricao': self.descricao,
            'forma_pagamento': self.forma_pagamento
        }

    def __str__(self):
        return (
            f"Lançamento[{self.categoria.nome if self.categoria else 'Sem Categoria'}] "
            f"{self.descricao or ''} | R${self.valor:.2f} | Data: {self.data_lancamento} | Pagamento: {self.forma_pagamento or 'N/A'}"
        )

    def __repr__(self):
        return (
            f"Lancamento(valor={self.valor}, categoria='{self.categoria.nome if self.categoria else None}', descricao='{self.descricao}', data='{self.data_lancamento}')"
        )

    def __eq__(self, other):
        return (
            isinstance(other, Lancamento)
            and self.valor == other.valor
            and (self.categoria.nome if self.categoria else None) == (other.categoria.nome if other.categoria else None)
            and self.descricao == other.descricao
            and self.data_lancamento == other.data_lancamento
        )
