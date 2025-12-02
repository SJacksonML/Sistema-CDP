from collections import defaultdict

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

    def imprimir(self):
        # Um print pra ter um feedback por enquanto
        # Marcando para verificar necessidade após aplicação em um front bacana
        print('--- RELATÓRIO SIMPLES ---')
        print('\nTotal por categoria:')
        for cat, total in self.total_por_categoria().items():
            print(f'  {cat}: R$ {total:.2f}')
        print(f'\nSaldo total: R$ {self.saldo_total():.2f}')
