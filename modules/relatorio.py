class Relatorio:
    def __init__(self, orcamentos: list):
        self.orcamentos = orcamentos
      # Ainda há dificuldade em evidenciar em que formato seria agradável receber o relatório, partirei do mais básico e sem orientação por hora.


    def total_por_categoria(self):
        resumo = {}
        for l in self.lancamentos:
            resumo.setdefault(l.categoria.nome, 0)
            resumo[l.categoria.nome] += l.valor if l.tipo == "despesa" else -l.valor
        return resumo

    def imprimir(self):
        print("--- RELATÓRIO FINANCEIRO ---")
        for categoria, total in self.total_por_categoria().items():
            print(f"{categoria}: R$ {total:.2f}")

    def despesas_por_categoria(self):
        """
        Gera um relatório de despesas por categoria.
         """
        pass

    def despesas_por_pagamento(self):
        """
        Gera um relatório de despesas por forma de pagamento.
        """
        pass

    def percentual_por_categoria(self):
        """
        Gera um relatório do percentual gasto por categoria.
        """
        pass

    def mes_mais_economico(self):
        """
        Identifica o mês com menor gasto total.
        """
        pass

    def comparativo_3_meses(self):
        """
        Gera um comparativo de gastos dos últimos 3 meses.
        """
        pass
