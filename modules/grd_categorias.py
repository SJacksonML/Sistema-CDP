from modules.cdt_categorias import Categoria

class GerenciadorCategorias:
    """Gerencia categorias de receita e despesa."""
    #Tive alguns problemas e cadastrar e gerenciar categorias tudo na mesma classe.
    #Optei por tentar fazer isso de outra forma, está em fase de testes.

    def __init__(self):
        self._categorias = []   # lista privada

    def cadastrar(self, nome, tipo, limite_mensal=0, descricao=""):
        nome = nome.strip()

        if self.existe_categoria(nome):
            raise ValueError(f"A categoria '{nome}' já existe!")

        nova_categoria = Categoria(nome, tipo, limite_mensal, descricao)
        self._categorias.append(nova_categoria)
        return nova_categoria

    def existe_categoria(self, nome):
        return any(c.nome.lower() == nome.lower() for c in self._categorias)

    def listar(self):
        return list(self._categorias)
