#Sérios problemas com o print de utf-8, isso aqui força a sair com as acentuações que eu quero.
import sys
sys.stdout.reconfigure(encoding='utf-8')

#Abaixo, estou importando para a main todas as classes que usarei para os testes iniciais.
from modules.receita import Receita
from modules.despesa import Despesa
from modules.saldo import Saldo
from modules.grd_categorias import GerenciadorCategorias

# Abaixo, apenas testes realizados diretamente na main para entender o funcionnamento do programa até aqui.
manager = GerenciadorCategorias()
manager.cadastrar("Salário", "receita", 0)
manager.cadastrar("Alimentação", "despesa", 500)
manager.cadastrar("Transporte", "despesa", 300)

for test in manager.listar():
    print(test)

saldo = Saldo()
r1 = Receita(247.16, "Trabalho", "25/11/2025", "Bonificacao do trabalho", "PIX")
d1 = Despesa(1112.20, "Carro", "26/11/2025", "Manutencao do carro", "Credito")
d2 = Despesa(23.50, "Alimentacao", "26/11/2025", "Almoco no centro", "Debito")

print(r1)
r1.executar(saldo)
print(saldo)

print(d1)
d1.executar(saldo)
print(saldo)

print(d2)
d2.executar(saldo)
print(saldo)