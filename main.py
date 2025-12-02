# Aqui venho com uma outra proposta de interação, mais focada em usabilidade
# A ideia é um pequeno menu, para testar as funcionalidades do sistema
# Como tudo, não sei se voou manter até uma visualização do programa
# Lembrar de rever parâmetros de seleção das opções caso altere o modo de interação com o código

from modules.sistema import Sistema

def main():
    s = Sistema()
    while True:
        print("""\
===== ALVO - um Sistema de Controle de Despesas Pessoais =====
1) Listar categorias
2) Adicionar categoria
3) Listar lançamentos
4) Adicionar despesa
5) Adicionar receita
6) Gerar relatório
7) Salvar e sair
0) Sair sem salvar
""")
        opt = input("Escolha: ").strip()
        if opt == "1":
            s.listar_categorias()
        elif opt == "2":
            nome = input("Nome da categoria: ").strip()
            tipo = input("Tipo (receita/despesa/ambos) [despesa]: ").strip() or 'despesa'
            limite = input("Limite (opcional): ").strip()
            limite = float(limite) if limite else None
            s.adicionar_categoria(nome, tipo, limite)
        elif opt == "3":
            s.listar_lancamentos()
        elif opt == "4":
            s.criar_lancamento('despesa')
        elif opt == "5":
            s.criar_lancamento('receita')
        elif opt == "6":
            s.gerar_relatorio()
        elif opt == "7":
            s.salvar()
            print('Dados salvos. Saindo.')
            break
        elif opt == "0":
            print('Saindo sem salvar.')
            break
        else:
            print('Opção inválida.')

if __name__ == '__main__':
    main()
