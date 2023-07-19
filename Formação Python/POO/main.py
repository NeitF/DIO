from cliente import *
from transacao import *

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Abrir conta corrente
[l] Listar contas
[q] Sair

=>
"""

num = 1
pessoa = PessoaFisica("Campinas", "555.222.111-00", "Josias", "25/05/1990")

while True:
  opcao = input(menu)
  
  if opcao == "d":
    valor, num_conta = input('Digite o valor de depósito e o número da conta: ').split()
    valor, num_conta = int(valor), int(num_conta)
    conta = pessoa.contas[num_conta]
    pessoa.realizar_transacao(conta, Deposito(valor))
  elif opcao == "s":
    valor, num_conta = input('Digite o valor de saque e o número da conta: ').split()
    valor, num_conta = int(valor), int(num_conta)
    conta = pessoa.contas[num_conta]
    pessoa.realizar_transacao(conta, Saque(valor))
  elif opcao == "e":
    pass
  elif opcao == "c":
    pessoa.abrir_conta(num, pessoa)
    num += 1
  elif opcao == "l":
    pessoa.listarContas()
  elif opcao == "q": 
    break
    
  else:
    print("Operação inválida, por favor selecione novamente a operação desejada")
    