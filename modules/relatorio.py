from collections import defaultdict
from datetime import datetime

class Relatorio:
    """Gera relatórios a partir de uma lista de objetos Lancamento"""
# Isso aqui deu trabalho, lembrar de valorizar 

    def __init__(self, lancamentos):
        self.lancamentos = lancamentos or []

    def total_por_categoria(self):
        resumo = defaultdict(float)
        for l in self.lancamentos:
            nome = l.categoria.nome if l.categoria else 'Sem categoria'
            if getattr(l, 'tipo', '') == 'despesa':
                resumo[nome] += l.valor
            else:
                resumo[nome] -= l.valor
        return dict(resumo)

    def saldo_total(self):
        saldo = 0.0
        for l in self.lancamentos:
            if getattr(l, 'tipo', '') == 'despesa':
                saldo -= l.valor
            else:
                saldo += l.valor
        return saldo
        
    def percentual_por_categoria(self):
        gastos = {}
        total = 0

        for l in self.lancamentos:
            if l.tipo == "despesa" and l.categoria:
                nome = l.categoria.nome
                gastos[nome] = gastos.get(nome, 0) + l.valor
                total += l.valor

        percentuais = {}
        for cat, valor in gastos.items():
            percentuais[cat] = {
                "percentual": (valor / total) * 100 if total > 0 else 0,
                "valor": valor
            }

        return percentuais

    def top_categorias(self, limite=3):
        gastos = {}

        for l in self.lancamentos:
            if l.tipo == "despesa" and l.categoria:
                nome = l.categoria.nome
                gastos[nome] = gastos.get(nome, 0) + l.valor

        ordenado = sorted(gastos.items(), key=lambda x: x[1], reverse=True)
        return ordenado[:limite]

    def media_mensal(self):
        receitas = defaultdict(float)
        despesas = defaultdict(float)

        for l in self.lancamentos:
            mes = l.data_lancamento.strftime("%Y-%m")
            if l.tipo == "receita":
                receitas[mes] += l.valor
            else:
                despesas[mes] += l.valor

        media_receita = sum(receitas.values()) / len(receitas) if receitas else 0
        media_despesa = sum(despesas.values()) / len(despesas) if despesas else 0

        return media_receita, media_despesa

    def imprimir(self):
        # Um print pra ter um feedback por enquanto
        # Marcando para verificar necessidade após aplicação em um front bacana
        print('--- RELATÓRIO SIMPLES ---')
        print('\nTotal por categoria:')
        for cat, total in self.total_por_categoria().items():
            print(f'  {cat}: R$ {total:.2f}')
        print(f'\nSaldo total: R$ {self.saldo_total():.2f}')
