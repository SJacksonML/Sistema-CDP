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
        total_despesas = 0.0
        por_categoria = defaultdict(float)

        for l in self.lancamentos:
            if l.tipo == "despesa":
                total_despesas += l.valor
                por_categoria[l.categoria.nome] += l.valor

        if total_despesas == 0:
            print("Nenhuma despesa registrada.")
            return

        print("\nPercentual de gastos por categoria:")
        for cat, valor in por_categoria.items():
            perc = (valor / total_despesas) * 100
            print(f"- {cat}: {perc:.2f}% (R$ {valor:.2f})")

    def top_categorias(self, n=3):
        gastos = defaultdict(float)

        for l in self.lancamentos:
            if l.tipo == "despesa":
                gastos[l.categoria.nome] += l.valor

        if not gastos:
            print("Nenhuma despesa registrada.")
            return

        ranking = sorted(
            gastos.items(),
            key=lambda item: item[1],
            reverse=True
        )

        print(f"\nTop {n} categorias por gasto:")
        for i, (cat, valor) in enumerate(ranking[:n], start=1):
            print(f"{i}. {cat} — R$ {valor:.2f}")

    def media_mensal(self):
        meses = defaultdict(lambda: {"receita": 0.0, "despesa": 0.0})

        for l in self.lancamentos:
            data = datetime.fromisoformat(l.data_lancamento)
            chave = f"{data.year}-{data.month:02d}"

            meses[chave][l.tipo] += l.valor

        if not meses:
            print("Nenhum lançamento registrado.")
            return

        total_receita = sum(m["receita"] for m in meses.values())
        total_despesa = sum(m["despesa"] for m in meses.values())

        qtd_meses = len(meses)

        print("\nMédia mensal:")
        print(f"- Receita média: R$ {total_receita / qtd_meses:.2f}")
        print(f"- Despesa média: R$ {total_despesa / qtd_meses:.2f}")

    def imprimir(self):
        # Um print pra ter um feedback por enquanto
        # Marcando para verificar necessidade após aplicação em um front bacana
        print('--- RELATÓRIO SIMPLES ---')
        print('\nTotal por categoria:')
        for cat, total in self.total_por_categoria().items():
            print(f'  {cat}: R$ {total:.2f}')
        print(f'\nSaldo total: R$ {self.saldo_total():.2f}')
