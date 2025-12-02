class Categoria:
    """Classe de 'cadastro' de categorias novas e definição dos parâmetros de categorias"""

    def __init__(self, nome: str, tipo: str = 'despesa', limite_mensal: float = None, descricao: str = ''):
        self._nome = str(nome)
        self._tipo = str(tipo).lower()
        self._limite_mensal = None if limite_mensal is None else float(limite_mensal)
        self._descricao = descricao

    @property
    def nome(self):
        return self._nome

    @property
    def tipo(self):
        return self._tipo

    @property
    def limite_mensal(self):
        return self._limite_mensal

    @property
    def descricao(self):
        return self._descricao

    def to_dict(self):
        return {
            'nome': self.nome,
            'tipo': self.tipo,
            'limite_mensal': self.limite_mensal,
            'descricao': self.descricao
        }

    def __str__(self):
        lim = f" (limite: R${self.limite_mensal:.2f})" if self.limite_mensal else ''
        return f"Categoria[{self.tipo}] {self.nome}{lim}"

    def __repr__(self):
        return f"Categoria(nome='{self.nome}', tipo='{self.tipo}', limite={self.limite_mensal})"

    def __eq__(self, other):
        return (
            isinstance(other, Categoria)
            and self.nome == other.nome
            and self.tipo == other.tipo
            and self.limite_mensal == other.limite_mensal
        )
