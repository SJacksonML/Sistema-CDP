class Categoria:
  """
  Essa classe tem como propósito gerenciar as categorias de Receita e Despesa, criando ou excluindo categorias para essas movimentações.
  """
  def __init__(self, nome, tipo, limite_mensal, descrição = " ")
  """
  Ao inicializar a classe, é interessante que o atributo 'descrição' seja opcional. Portanto, vamos começar abordando ele como um atributo nulo do tipo string sem nada " ".
  """
    self.nome = nome
    self.tipo = tipo
    self.limite_mensal = limite_mensal
    self.descrição = descrição
def cadastar(self, nome_categoria)
"""
A priori, vamos esboçar essa função da forma mais robusta possível, uma função que cadastra novas categorias. Depois vemos como isso se comporta para casos especiais: nome de formato inválido, nome repetido, etc.
"""
  pass
