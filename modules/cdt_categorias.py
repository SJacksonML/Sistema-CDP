class Categoria:
    """Representa uma categoria de Receita ou Despesa."""

    def __init__(self, nome, tipo, limite_mensal, descricao=""):
        self._nome = nome
        self._tipo = tipo.lower() #tipo será receita ou despesa, escrito em minúsculo, estou vendo formas de melhorar isto ainda
        self._limite_mensal = float(limite_mensal)
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

    def __str__(self):
        return f"[{self.tipo.upper()}] {self.nome} (limite: R${self.limite_mensal:.2f})"
