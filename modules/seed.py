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
        Despesa(424, lazer, "2025-10-03", "Gasto de lazer"),
        Despesa(475, lazer, "2025-10-08", "Gasto de lazer"),
        Despesa(412, lazer, "2025-10-12", "Gasto de lazer"),
    ])

    # mês de novembro
    sistema.lancamentos.extend([
        Receita(5600, salario, "2025-11-05", "Salário base"),
        Despesa(785, casa, "2025-11-05", "Aluguel + contas"),
        Despesa(750, faculdade, "2025-11-05", "Mensalidade"),
        Despesa(414, lazer, "2025-11-02", "Gasto de lazer"),
        Despesa(96, lazer, "2025-11-07", "Gasto de lazer"),
        Despesa(205, lazer, "2025-11-11", "Gasto de lazer"),
    ])

    # atualiza o saldo atual, após lançamentos cadastrados nesta seed
    sistema.atualizar_saldo()
