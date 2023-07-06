menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>
"""

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""

while True:
  opcao = input(menu)
  
  if opcao == "d":
    print('Depósito')
    dep = int(input('Valor: '))

    if dep > 0:
      saldo += dep
      extrato += f"Depósito: R${dep:.2f}\n"
    else:
      print('Apenas valores positivos são permitidos')
    
  elif opcao == "s":
    if numero_saques == LIMITE_SAQUES:
       print('Limite de saques diário atingido')
    else:
      print('Saque')
      saque = int(input('Valor: '))
  
      if saque > limite:
        print('Valor suprior ao limite permitido')
      elif saque > saldo:
        print('Saldo insuficiente')
      elif saque < 0:
        print('Apenas valores positivos são permitidos')
      else:
        saldo -= saque
        extrato += f"Saque: R${saque:.2f}\n"
        numero_saques += 1
      
  elif opcao == "e":
    print('Extrato'.center(20, '='))
    print(extrato + f"\nSaldo: R${saldo:.2f}\n" + '='*20)
    
  elif opcao == "q":
    break
  else:
    print("Operação inválida, por favor selecione novamente a operação desejada")