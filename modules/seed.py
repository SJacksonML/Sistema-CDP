from modules.receita import Receita
from modules.despesa import Despesa


def carregar_seed(sistema):
    """Popula o sistema com dados simulados (didáticos).Deve ser chamada UMA ÚNICA VEZ por execução."""

    salario = sistema.adicionar_categoria(
        "salário", "receita", None
    )

    casa = sistema.adicionar_categoria(
        "casa", "despesa", None
    )

    faculdade = sistema.adicionar_categoria(
        "faculdade", "despesa", None
    )

    lazer = sistema.adicionar_categoria(
        "lazer", "despesa", 1000
    )

    # mês de outubro
    sistema.lancamentos.extend([
        Receita(5600, salario, "2025-10-05", "Salário base"),
        Despesa(785, casa, "2025-10-05", "Aluguel + contas"),
        Despesa(750, faculdade, "2025-10-05", "Mensalidade"),
        Despesa(424, lazer, "2025-10-03", "Read Dead Redemption, Delux"),
        Despesa(254, lazer, "2025-10-08", "Gastos no restaurante com namorada"),
        Despesa(132, lazer, "2025-10-12", "Bebidas para o final de semana"),
        Despesa(16, lazer, "2025-10-12", "Salgadinhos"),
    ])

    # mês de novembro
    sistema.lancamentos.extend([
        Receita(5600, salario, "2025-11-05", "Salário base"),
        Despesa(785, casa, "2025-11-05", "Aluguel + contas"),
        Despesa(750, faculdade, "2025-11-05", "Mensalidade"),
        Despesa(499, lazer, "2025-11-02", "Suplemento de RPG: apoio coletivo"),
        Despesa(96, lazer, "2025-11-07", "Sushi com a gata"),
        Despesa(24, lazer, "2025-11-11", "Vontade de comer bolo"),
    ])

    # atualiza o saldo atual, após lançamentos cadastrados nesta seed
    sistema.atualizar_saldo()
