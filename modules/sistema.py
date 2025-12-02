"""Corrdenação rpincipal do sistema"""
# Estou testando um módulo responsável pelo gerenciammento geral do programa,
# pois a dificuldade em implementar um JSON me fez recorrer a tentativa e erro
     
from cdt_categorias import Categoria
from receita import Receita
from despesa import Despesa
from relatorio import Relatorio
from repositorio import RepositorioJSON

class Sistema:
    def __init__(self, caminho_dados="dados.json"):
        # Vai servir pra rmazenamento interno
        self.categorias: dict[str, Categoria] = {}
        self.lancamentos: list = []

        # PUma persistência
        self.repo = RepositorioJSON(caminho_dados)

        # Tenta carregar dados já existentes
        self.carregar()

    def adicionar_categoria(self, nome: str, limite: float | None = None):
        """Cria uma categoria se não houver"""
        if nome in self.categorias:
            print(f"[AVISO] Categoria '{nome}' já existe.")
            return

        self.categorias[nome] = Categoria(nome, limite)
        print(f"Categoria '{nome}' criada.")

    def adicionar_receita(self, categoria_nome: str, valor: float):
        """Cria uma receita associada a uma categoria"""
        categoria = self.categorias.get(categoria_nome)

        if not categoria:
            print(f"[ERRO] Categoria '{categoria_nome}' não encontrada.")
            return

        nova_receita = Receita(valor, categoria)
        self.lancamentos.append(nova_receita)

        print("[OK] Receita registrada.")

    def adicionar_despesa(self, categoria_nome: str, valor: float):
        """Cria uma despesa associada a uma categoria"""
        categoria = self.categorias.get(categoria_nome)

        if not categoria:
            print(f"[ERRO] Categoria '{categoria_nome}' não encontrada.")
            return

        nova_despesa = Despesa(valor, categoria)
        self.lancamentos.append(nova_despesa)

        print("[OK] Despesa registrada.")

    def gerar_relatorio(self):
        rel = Relatorio(self.lancamentos)
        rel.exibir()

    def carregar(self):
        dados = self.repo.carregar()
        if not dados:
            return

        # carregar Categorias
        for c in dados.get("categorias", []):
            self.categorias[c["nome"]] = Categoria(
                nome=c["nome"],
                limite=c.get("limite")
            )

        # carregar Lançamentos
        for l in dados.get("lancamentos", []):
            categoria = self.categorias.get(l["categoria"])
            if not categoria:
                continue

            if l["tipo"] == "receita":
                obj = Receita(l["valor"], categoria)
            else:
                obj = Despesa(l["valor"], categoria)

            self.lancamentos.append(obj)

    def salvar(self):
        dados = {
            "categorias": [
                {"nome": c.nome, "limite": c.limite}
                for c in self.categorias.values()
            ],
            "lancamentos": [
                {
                    "tipo": lanc.tipo,
                    "valor": lanc.valor,
                    "categoria": lanc.categoria.nome,
                }
                for lanc in self.lancamentos
            ],
        }

        self.repo.salvar(dados)
        print("[OK] Dados salvos com sucesso.")
