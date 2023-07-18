from cliente import *

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Abrir conta corrente
[l] Listar contas
[q] Sair

=>
"""
num = 0
pessoa = PessoaFisica("Campinas", "555.222.111-00", "Lucas", "25/05/1990")

while True:
  opcao = input(menu)
  
  if opcao == "d":
    valor = int(input('Valor de depósito: '))
    
  elif opcao == "s":
    pass
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