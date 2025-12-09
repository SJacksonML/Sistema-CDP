from datetime import datetime

class Alerta:
    """Vai alertar quando uma Regra de Negócio for violada"""

    def __init__(self, tipo: str, mensagem: str, categoria=None):
        self._tipo = tipo
        self._mensagem = mensagem
        self._categoria = categoria
        self._data_hora = datetime.now()

    @property
    def tipo(self):
        return self._tipo

    @property
    def mensagem(self):
        return self._mensagem

    @property
    def categoria(self):
        return self._categoria

    @property
    def data_hora(self):
        return self._data_hora

    def to_dict(self):
        return {
            "tipo": self.tipo,
            "mensagem": self.mensagem,
            "categoria": self.categoria.nome if self.categoria else None,
            "data_hora": self.data_hora.isoformat()
        }

    def __str__(self):
        cat = f" | Categoria: {self.categoria.nome}" if self.categoria else ""
        return f"[ALERTA] {self.tipo} - {self.mensagem}{cat} - {self.data_hora}"
