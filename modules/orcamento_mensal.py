from collections import defaultdict
from datetime import datetime

class OrcamentoMensal:
    """Representa o orçamento de um mês específico (YYYY-MM)"""

    def __init__(self, ano: int, mes: int, saldo_inicial: float = 0.0):
        self.ano = ano
        self.mes = mes
        self.saldo_inicial = float(saldo_inicial)
        self.lancamentos = []

    def adicionar_lancamento(self, lancamento):
        """Adiciona um lançamento se ele pertencer a este mês"""
        data = datetime.fromisoformat(lancamento.data_lancamento)

        if data.year == self.ano and data.month == self.mes:
            self.lancamentos.append(lancamento)

    def total_receitas(self):
        return sum(l.valor for l in self.lancamentos if getattr(l, 'tipo', '') == 'receita')

    def total_despesas(self):
        return sum(l.valor for l in self.lancamentos if getattr(l, 'tipo', '') == 'despesa')

    def saldo_final(self):
        return self.saldo_inicial + self.total_receitas() - self.total_despesas()

    def __str__(self):
        return (
            f"Orçamento {self.mes:02d}/{self.ano} | "
            f"Saldo inicial: R${self.saldo_inicial:.2f} | "
            f"Saldo final: R${self.saldo_final():.2f}"
        )
