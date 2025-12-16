from modules.cdt_categorias import Categoria
from modules.receita import Receita
from modules.despesa import Despesa
from modules.relatorio import Relatorio
from modules.repositorio import RepositorioJSON
from modules.alerta import Alerta
from modules.orcamento_mensal import OrcamentoMensal
from modules.seed import carregar_seed  # Importando a função de seed
from datetime import datetime


class Sistema:
    """Orquestra categorias, lancamentos e persistencia."""

    def __init__(self, caminho_dados='dados.json'):
        self.categorias = {}  
        self.lancamentos = []  
        self.repo = RepositorioJSON(caminho_dados)
        self.carregar()  
        self.alertas = []

    def adicionar_categoria(self, nome: str, tipo: str = 'despesa', limite: float = None):
        nome_normalizado = nome.strip().lower()

        if nome_normalizado in self.categorias:
            print(f"\n!!![AVISO]!!! Categoria '{nome}' já existe, tente novamente com outro nome ou selecione a categoria já criada\n")
            return self.categorias[nome_normalizado]

        cat = Categoria(nome.strip(), tipo, limite)
        self.categorias[nome_normalizado] = cat
        print(f"\nCategoria '{nome}' criada.")
        return cat

    def listar_categorias(self):
        if not self.categorias:
            print('\nNenhuma categoria foi cadastrada. Adicione novas categorias de receita/depesa e elas aparecerão aqui.')
            return
        for c in self.categorias.values():
            print(f"- {c}")

    def criar_lancamento(self, tipo: str = 'despesa'):
        try:
            valor = float(input("Valor: ").strip())
        except ValueError:
            print("\nValor inválido. Digite um número.")
            return

        categoria = None
        while True:
            self.listar_categorias()
            cat_nome = input(
                "\nNome da categoria "
                "(obrigatória para despesa, ENTER para receita sem categoria): "
            ).strip().lower()

            if not cat_nome:
                if tipo == "despesa":
                    print("\nDespesas DEVEM possuir uma categoria.")
                    continue
                break

            categoria = self.categorias.get(cat_nome)
            if not categoria:
                print("\nCategoria não encontrada.")
                continue

            if categoria.tipo != tipo:
                print(
                    f"Categoria '{categoria.nome}' é do tipo '{categoria.tipo}', "
                    f"não pode ser usada para '{tipo}'."
                )
                continue
            break

        while True:
            data = input(
                "\nData do lançamento (YYYY-MM-DD, ENTER para hoje): "
            ).strip()

            if not data:
                data = None
                break

            try:
                from datetime import date
                date.fromisoformat(data)
                break
            except ValueError:
                print("\nData inválida. Use YYYY-MM-DD.")

        descricao = input("Descrição (opcional): ").strip() or None
        forma = input("Forma de pagamento (opcional): ").strip() or None

        try:
            if tipo == "receita":
                obj = Receita(valor, categoria, data, descricao, forma)
            else:
                obj = Despesa(valor, categoria, data, descricao, forma)
        except Exception as e:
            print(f"Erro ao criar lançamento: {e}")
            return

        self.lancamentos.append(obj)
        self.atualizar_saldo()

        print("\nLançamento adicionado:", obj)

    def listar_lancamentos(self):
        if not self.lancamentos:
            print('Nenhum lançamento.')
            return
        for l in self.lancamentos:
            print(f"- {l}")

    def gerar_relatorio(self):
        r = Relatorio(self.lancamentos)

        print("\n======= RELATÓRIO ANALÍTICO =======\n")

        percentuais = r.percentual_por_categoria()
        print("Percentual de gastos por categoria:")
        for cat, dados in percentuais.items():
            print(f"- {cat}: {dados['percentual']:.2f}% (R$ {dados['valor']:.2f})")

        print("\nTop 3 categorias por gasto:")
        top = r.top_categorias()
        for i, (cat, valor) in enumerate(top, start=1):
            print(f"{i}. {cat} — R$ {valor:.2f}")

        media_receita, media_despesa = r.media_mensal()
        print("\nMédia mensal:")
        print(f"- Receita média: R$ {media_receita:.2f}")
        print(f"- Despesa média: R$ {media_despesa:.2f}")

        print("\n=================================")

    def salvar(self):
        self._atualizar_saldo()

        dados = {
            'categorias': [c.to_dict() for c in self.categorias.values()],
            'lancamentos': [l.to_dict() for l in self.lancamentos]
        }

        self.repo.salvar(dados)
        print('[OK] Dados salvos.')

    def atualizar_saldo(self):
        total = 0.0

        for l in self.lancamentos:
            if l.tipo == "despesa":
                total -= l.valor
            else:
                total += l.valor

        self.saldo_atual = total

    def calcular_saldo_atual(self) -> float:
        saldo = 0.0
        for l in self.lancamentos:
            if l.tipo == "receita":
                saldo += l.valor
            else:
                saldo -= l.valor
        return saldo

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

    def gerar_orcamentos_mensais(self):
        orcamentos = {}
        saldo_anterior = 0.0

        lancs_ordenados = sorted(
            self.lancamentos,
            key=lambda l: l.data_lancamento
        )

        for l in lancs_ordenados:
            data = datetime.fromisoformat(l.data_lancamento)
            chave = (data.year, data.month)

            if chave not in orcamentos:
                orcamentos[chave] = OrcamentoMensal(
                    data.year,
                    data.month,
                    saldo_anterior
                )

            orcamentos[chave].adicionar_lancamento(l)
            saldo_anterior = orcamentos[chave].saldo_final()

        return orcamentos

    def carregar_seed(self):
        from modules.seed import carregar_seed
        carregar_seed(self)
        print("\n[SEED] Dados simulados carregados com sucesso.")

