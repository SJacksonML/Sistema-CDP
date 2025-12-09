# ALVO - seu Sistema de Controle de Despesas Pessoais

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

### Classe; Sistema

- Usa o conceito de Classe Orquestra. É a responsável por chamar métodos de classes, garantir persistência e não bugar o JSON.

## UML Textual

### Classe: Alerta

- Atributos

  - 

- Métodos

  - 

- Relacionamentos

  - 

### Classe: Categoria

- Atributos

  - 

- Métodos

  - 

- Relacionamentos
  - 

### Classe: GerenciadorCategoria

- Atributos

  - 

- Métodos

  - 

- Relacionamentos

  - 

### Classe: Lancamento

- Atributos

  - 

- Métodos

  - 

- Relacionamentos

  - 

#### Classe: Despesa

- Atributos

  - 

- Métodos

  - 

- Relacionamentos

  - 

#### Classe: Receita

- Atributos

  - 

- Métodos

  - 

- Relacionamentos

  - 

### Classe: Orcamento

- Atributos

  - 

- Métodos

  - 

- Relacionamentos

  - 

### Classe: Relatorio

- Atributos

  - 

- Métodos

  - 

- Relacionamentos

  - 

### Classe: RepositorioJSON

- Atributos

  - 

- Métodos

  - 

- Relacionamentos

  - 

### Classe: Saldo

- Atributos

  - 

- Métodos

  - 

- Relacionamentos

  - 

### Classe: Sistema

- Atributos

  - 

- Métodos

  - 

- Relacionamentos

  - 

## Objetivo Educacional

Desenvolver habilidades de POO utilizando linguagem Python através de um sistema desafiador e de grande utilidade para qualquer usuário.
