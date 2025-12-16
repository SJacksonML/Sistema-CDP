# ALVO - seu Sistema de Controle de Despesas Pessoais

Projeto de POO - Engenharia de Software.

## Descrição Geral

Este projeto tem como objetivo fornecer ferramentas de fácil uso para rastrear gastos financeiros a fim de promover melhor economia a nível doméstico.

## Objetivo Educacional

Desenvolver habilidades de POO utilizando linguagem Python através de um sistema desafiador e de grande utilidade para qualquer usuário.

## Funcionalidades Principais

- Cadastro de categorias

- Registro de receitas e despesas

- Controle mensal de orçamento

- Relatórios e estatísticas básicas

- Alertas automáticos relativos a gastos e limites

- Arquivo de configurações (settings.json) para alterar parâmetros de limites das variáveis

## Estrutura de Classes

### Classe: Alerta

- Útil para alertar o usuário sobre violações da principais Regras de Negócios: ultrapassar valor de despesa, tentar criar despesa sem categoria, alertar quando o montante de despesas de uma categoria ultrapassa o limite.

### Classe: Categoria

- Aqui há a definição dos parâmetros para criação de novas categorias.
  
### Classe: GerenciadorCategorias

- Contém toda a movimentação das classes após cadastradas, associando cada uma a um tipo de Lancamento, atualizando valores, etc.

### Classe: Lancamento

- Classe Pai que gerencia transações, através de Receita e Despesa
    #### Despesa
    - Classe filho que define o 'tipo' (atributo de Lancamento) e contém as RN associadas às limitações de cadastrar despesas;
    #### Receita
    - Classe filho que, assim como Despesa, define o 'tipo' de Lancamento e mantém em funcionamento as RN relacionadas às receitas.

### Classe: Orcamento

- Controla o cálculo do orçamento do mês atual tendo em vista os gastos e lucros dos meses anteriores.

### Classe: Relatorio

- Gera um relatório simples no terminal ao final das interações com o cadastro de classes, lançamentos e saldo final após movimentaações.

### Classe: RepositorioJSON

- Um repositório simples que salva ou carrega dicts em JSON. Ainda não há Banco de Dados implementado, por enquanto todos os dados ficam armazenados em JSON.

### Classe: Saldo

- Uma importante classe. Aqui é calculado o montante do Saldo atual, que servirá de parâmetro para muitas outras classes. Seus atributos são privados para evitar alterações fora do esperado.

### Classe: Sistema

- Usa o conceito de Classe Orquestra. É a responsável por chamar métodos de classes, garantir persistência e não bugar o JSON.

## UML Textual

### Classe: Alerta

- Atributos

  - tipo: string
  - mensagem: string
  - categoria = None

- Métodos

  - ``to_dict``: transformar valores de atributos em dicionário para formatá-los
  - ``__str__`` : tansformar valores em string (testando uso de métodos especiais)

- Relacionamentos

  - Se relaciona em ``Sistema``, sendo chamado para gerar alertas sobre violação de algumas Regras de Negócio

### Classe: Categoria

- Atributos

  - nome: string
  - tipo: string
  - limite_mensal: float = None
  - descricao: string - ' '

- Métodos

  - ``to_dict``: transforma os valores dos atributos em dicionário
  - ``str__``: chama ``limite_mensal``, ``tipo`` e ``nome`` como string para printar no terminal
  - ``__repr__``: para retornar uma "string técnica" da categoria criada. Isso será usado no JSON
  - ``__eq__``: comparar se os valores de ``nome``, ``tipo`` e ``limiite_mensal`` são idênticos, mas não do ponto de vista de endereço de memória, iguais semanticamente, para verificar se aquela categoria já foi cadastrada antes e poder impedir de se criar duas categorias iguais.

- Relacionamentos

  - ``Categoria`` cria os parâmetros de categorias que serão usadas em ``GerenciadorCategoria``, onde este depende de uma cria categorias e usa categorias  criadas, ou não, para atribuir valores a partir de interações do tipo ``Lancamento`` com receitas e despesas, através do ``Sistema``

### Classe: GerenciadorCategoria

- Atributos

  - 'sem atributos'

- Métodos

  - ``cadastrar``: cadastra novas categorias e verifica se já existem categorias de mesmo nome, se sim, informa que aquela classe já existe, impossibilitando criar duas categorias com o mesmo nome
  - ``existe_categora``: usado anteriormente, aqui é definido o print do que aparece qaundo se tenta criar uma categoria de mesmo nome
  - ``listar``: lista as categorais cadastradasw

- Relacionamentos

  - Se relaciona com ``Categoria`` intrisicamente, à medida que é uma classe sem atributos, apenas definde métodos para outra classe

### Classe: Lancamento

- Atributos

  - valor: float
  - categoria
  - data_lancamento = None
  - descricao: string = None
  - forma_pagamento: string = None

- Métodos

  - ``executar``: puxa saldo
  - ``to_dict``: como dito antes, serve para transformar em dicionário
  - ``__str__``
  - ``__repr__``
  - ``__eq__``

- Relacionamentos

  - Classe pai de ``Receita`` e ``Despesa``

#### Classe: Despesa

- Atributos

  - "herda"

- Métodos

  - ``executar``: altera o valor do saldo para -
  - ``__str__``: lê a alteração como string

- Relacionamentos

  - Se relaciona com sua classe pai e altera o valor de ``Saldo``

#### Classe: Receita

- Atributos

  - "herda"

- Métodos

  - ``executar``: altera o valor do saldo para +
  - ``__str__``: lê a alteração como string

- Relacionamentos

  - Se relaciona com a classe pai e altera o valor de ``Saldo``

### Classe: Relatorio

- Atributos

  - 'sem atributos'

- Métodos

  - ``saldo_total``: getattr, soma/subtrai valor de receita/despesa ao Saldo global
  - ``imprimir``: print de feedback

- Relacionamentos

  - Se relaciona com os valores de ``Saldo`` para posteriormente criar um relatório do JSON

### Classe: RepositorioJSON

- Atributos

  - caminho_arquivo = 'dados.json'

- Métodos

  - ``carregar``: lê valores do relatório
  - ``salvar``: atualiza valores do relatório

- Relacionamentos

  - Se relaciona com ``Relatório`` e com o arquivo JSON que mexe nos dados

### Classe: Saldo

- Atributos

  - 'sem atributos'

- Métodos

  - ``_alterar_saldo``: usa os valores de receita e despesa para alterar o valor numérico do saldo atual disponível
  - ``__str__``: print do saldo atual após movimentação financeira

- Relacionamentos

  - Usa valores de ``Lancamento`` para alterar valor do saldo

### Classe: Sistema

- Atributos

  - caminho_dados = 'dados.json'

- Métodos

  - ``adicionar_categoria``: compara e cria novas categorias, caso não existam ainda
  - ``listar_categorias``: mostra a lista de categorias existentes possíveis para cadastro de lançamento
  - ``cria_lancamento``: usa os valores de despesa e receita
  - ``listar_lancamento``: controle
  - ``gerar_relatorio``: imprime os valores de ``Relatório``
  - ``salvar``: salva os dados
  - ``_alterar_saldo``: modifica o valor de saldo
  - ``carregar``: load dos dados no json
  - ``registrar_alerta``: emite um alerta na tela, caso alguma RN tenha sido violada

- Relacionamentos

  - Define todos os parâmetros do programa como uma Orquestra, dando tudo que for necessário para manipulação na main
