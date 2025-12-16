from modules.sistema import Sistema
    # Menu de interações com o sistema
    # Foi criada uma seed com informações pré-definidas e de uso puramente didático, apenas para demonstrar e testar se os 
    # cálculos de saldo, lançamentos, relatório, estão todos funcionando. Você pode ativar e desativar a seed pelo menu.

def main():
    sistema = Sistema()
    seed_ativada = False   # controle para evitar que a seed seja duplicada

    while True:
        # manter o "SALDO ATUAL" de fato atual, sempre atualizado conforme são feitos novos lançamentos, inclusive quando
        # se utiliza os dados da seed
        saldo_atual = sistema.calcular_saldo_atual()

        print("""
========================================
 SALDO ATUAL: R$ {:.2f}
========================================
""".format(saldo_atual))

        print("""
----------------- MENU -----------------
1) Listar categorias
2) Adicionar categoria
3) Listar lançamentos
4) Adicionar despesa
5) Adicionar receita
6) Gerar relatório
7) Salvar e sair
9) Ativar Seed de Dados
0) Sair sem salvar
----------------------------------------
""")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            sistema.listar_categorias()

        elif opcao == "2":
            nome = input("Nome da categoria: ").strip()
            tipo = input("Tipo (receita/despesa): ").strip().lower()
            limite = input("Limite mensal (ENTER para nenhum): ").strip()
            limite = float(limite) if limite else None
            sistema.adicionar_categoria(nome, tipo, limite)

        elif opcao == "3":
            sistema.listar_lancamentos()

        elif opcao == "4":
            sistema.criar_lancamento("despesa")

        elif opcao == "5":
            sistema.criar_lancamento("receita")

        elif opcao == "6":
            sistema.gerar_relatorio()

        elif opcao == "7":
            sistema.salvar()
            print("\n[OK] Dados salvos. Encerrando sistema.")
            break

        elif opcao == "9":
            if seed_ativada:
                print("\n[AVISO] Seed já foi ativada nesta execução.")
            else:
                confirma = input("Ativar seed de dados? (S/N): ").strip().lower()
                if confirma == "s":
                    sistema.carregar_seed()
                    seed_ativada = True
                    print("[SEED] Dados simulados carregados com sucesso.")
                else:
                    print("[SEED] Operação cancelada.")

        elif opcao == "0":
            print("\nEncerrando sem salvar.")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
