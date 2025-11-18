class Lancamento:
  """
  Principal responsável pela usabilidade do sistema, a classe reune as ferramentas básicas de Despesa, Receita e gerenciamento de um Saldo da Conta
  """
  def __init__ (self, valor, nome_categoria, data_lancamento, descricao = " ", forma_pagamento):
    """
    Parâmetros básicos para inicializarmos as funções da Classe
    """
    self.valor = valor
    self.nome_categoria - nome_categoria
    self.data_lancamento = data_lancamento
    self.descricao = descricao
    self.forma_pagamento = forma_pagamento
  def pagar(self):
    """
    Função que resume a Despesa, ação de retirar dinheiro do montante do Saldo da conta.
    """
    pass
