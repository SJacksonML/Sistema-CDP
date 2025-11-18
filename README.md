# Sistema de Controle de Despesas Pessoais

Projeto de POO - Engenharia de Software.

## Descrição Geral

Este projeto tem como objetivo fornecer ferramentas de fácil uso para rastrear gastos financeiros a fim de promover melhor economia a nível doméstico.

## Funcionalidades Principais

- Cadastro de categorias

- Registro de receitas e despesas

- Controle mensal de orçamento

- Relatórios e estatísticas básicas

- Alertas automáticos relativos a gastos e limites

- Arquivo de configurações (settings.json) para alterar parâmetros de limites das variáveis

## Estrutura de Classes Planejada

### Classe: Categoria

  Representa tipos de receitas e despesas.

### Classe: Lancamento

  Registra cada operação financeira do usuário.

### Classe: OrcamentoMensal

  Agrupa lançamentos e calcula totais e saldo.

### Classe: Relatorio

  Gera estatísticas, agrupamentos e comparativos.

### Classe: Configuracoes

  Gerencia parâmetros globais do sistema.

## UML Textual (protótipo)

### Classe: Categoria

- Atributos

  - nome: str

  - tipo: str

  - limite_mensal: float | None

  - descricao: str | None

- Métodos

  - editar_nome(novo_nome)

  - editar_limite(novo_limite)

  - validar()

- Relacionamentos

  - 1 Categoria → N Lançamentos

### Classe: Lancamento

- Atributos

  - valor: float

  - categoria: Categoria

  - data: date

  - descricao: str

  - forma_pagamento: str

- Métodos

  - validar()

  - gerar_alertas()

- Relacionamentos

  - Cada Lançamento pertence a um OrcamentoMensal

  - Cada Lançamento usa 1 Categoria

### Classe: OrcamentoMensal

- Atributos

  - ano: int

  - mes: int

  - lancamentos: list[Lancamento]

  - meta_economia: float

- Métodos

  - adicionar_lancamento(lancamento)

  - calcular_total_receitas()

  - calcular_total_despesas()

  - calcular_saldo()

  - verificar_deficit()

- Relacionamentos

  - 1 OrcamentoMensal → N Lançamentos

  - É analisado pela classe Relatorio

### Classe: Relatorio

- Atributos

  - orcamentos: list[OrcamentoMensal]

- Métodos

  - despesas_por_categoria()

  - despesas_por_pagamento()

  - percentual_por_categoria()

  - mes_mais_economico()

  - comparativo_3_meses()

- Relacionamentos

  - Utiliza vários objetos OrcamentoMensal

### Classe: Configuracoes

- Atributos

  - alerta_alto_gasto: float

  - meses_comparativo: int

  - meta_economia_padrao: float

- Métodos

  - carregar()

  - salvar()

- Relacionamentos

  - Parâmetros usados por Lancamento, OrcamentoMensal e Relatorio

## Objetivo Educacional

Desenvolver habilidades de POO utilizando linguagem Python através de um sistema desafiador e de grande utilidade para qualquer usuário.
