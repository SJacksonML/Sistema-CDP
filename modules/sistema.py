from modules.cdt_categorias import Categoria
from modules.receita import Receita
from modules.despesa import Despesa
from modules.relatorio import Relatorio
from modules.repositorio import RepositorioJSON
from modules.alerta import Alerta

class Sistema:
    """Orquestra categorias, lancamentos e persistencia."""
    # Aqui estou implementando uma classe 'Orquestra' para organizar a casa
    # A priori, é pra ficar mais didático, ainda tô testando, lembrar de revisar
    # os parâmetros disso depois

    def __init__(self, caminho_dados='dados.json'):
        self.categorias = {}  
        self.lancamentos = []  
        self.repo = RepositorioJSON(caminho_dados)
        self.carregar()  
        self.alertas = []


    def adicionar_categoria(self, nome: str, tipo: str = 'despesa', limite: float = None):
        if nome in self.categorias:
            print(f"[AVISO] Categoria '{nome}' já existe.")
            return self.categorias[nome]
        cat = Categoria(nome, tipo, limite)
        self.categorias[nome] = cat
        print(f"Categoria '{nome}' criada.")
        return cat

    def listar_categorias(self):
        if not self.categorias:
            print('Nenhuma categoria cadastrada.')
            return
        for c in self.categorias.values():
            print(f"- {c}")

    def criar_lancamento(self, tipo: str = 'despesa'):
        try:
            valor = float(input('Valor: ').strip())
        except ValueError:
            print('Valor inválido.')
            return
        
        self.listar_categorias()
        cat_nome = input('Nome da categoria (ou enter para sem categoria): ').strip()
        categoria = self.categorias.get(cat_nome) if cat_nome else None
        data = input('Data (YYYY-MM-DD) [enter para hoje]: ').strip() or None
        descricao = input('Descrição (opcional): ').strip() or None
        forma = input('Forma de pagamento (opcional): ').strip() or None

        if tipo == 'receita':
            obj = Receita(valor, categoria, data, descricao, forma)
        else:
            obj = Despesa(valor, categoria, data, descricao, forma)

        self.lancamentos.append(obj)

        if isinstance(obj, Despesa) and categoria and categoria.limite_mensal is not None:
            total = 0
            for l in self.lancamentos:
                if l.categoria == categoria and isinstance(l, Despesa):
                    total += l.valor

            if total > categoria.limite_mensal:
                self.registrar_alerta(
                    "LIMITE_ESTOURADO",
                    f"A categoria '{categoria.nome}' excedeu o limite mensal!",
                    categoria
                )

        print('Lançamento adicionado:', obj)

    def listar_lancamentos(self):
        if not self.lancamentos:
            print('Nenhum lançamento.')
            return
        for l in self.lancamentos:
            print(f"- {l}")

    def gerar_relatorio(self):
        r = Relatorio(self.lancamentos)
        r.imprimir()

    def salvar(self):
        self._atualizar_saldo()

        dados = {
            'categorias': [c.to_dict() for c in self.categorias.values()],
            'lancamentos': [l.to_dict() for l in self.lancamentos]
        }

        self.repo.salvar(dados)
        print('[OK] Dados salvos.')

    def _atualizar_saldo(self):
        total = 0
        for l in self.lancamentos:
            if getattr(l, 'tipo', '') == 'despesa':
                total -= l.valor
            else:
                total += l.valor
        self.saldo_atual = total

    def carregar(self):
            dados = self.repo.carregar() or {}

            for cdict in dados.get("categorias", []):
                c = Categoria(
                    cdict.get("nome"),
                    cdict.get("tipo", "despesa"),
                    cdict.get("limite_mensal"),
                    cdict.get("descricao", "")
                )
                self.categorias[c.nome] = c

            for ldict in dados.get("lancamentos", []):
                cat = self.categorias.get(ldict.get("categoria"))

                if ldict.get("tipo") == "receita":
                    obj = Receita(
                        ldict.get("valor", 0),
                        cat,
                        ldict.get("data_lancamento"),
                        ldict.get("descricao"),
                        ldict.get("forma_pagamento")
                    )
                else:
                    obj = Despesa(
                        ldict.get("valor", 0),
                        cat,
                        ldict.get("data_lancamento"),
                        ldict.get("descricao"),
                        ldict.get("forma_pagamento")
                    )

                self.lancamentos.append(obj)

    def registrar_alerta(self, tipo, mensagem, categoria=None):
        alerta = Alerta(tipo, mensagem, categoria)
        self.alertas.append(alerta)
        print(alerta)