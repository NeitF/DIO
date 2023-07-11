menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar usuário
[c] Criar conta corrente
[l] Listar contas
[q] Sair

=>
"""

#VARIÁVEIS
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""
dados = []
usuarios = []
contas_corrente = []

#MÉTODOS
def sacar(*, saque, saldo, extrato, limite, numero_saques):
    if saque > limite:
      print('Valor suprior ao limite permitido')
      return saldo, extrato, numero_saques
    elif saque > saldo:
      print('Saldo insuficiente')
      return saldo, extrato, numero_saques
    elif saque < 0:
      print('Apenas valores positivos são permitidos')
      return saldo, extrato, numero_saques
    else:
      saldo -= saque
      extrato += f"Saque: R${saque:.2f}\n"
      numero_saques += 1
      return saldo, extrato, numero_saques
    

def depositar(saldo, valor, extrato):
   if valor > 0:
      saldo += valor
      extrato += f"Depósito: R${valor:.2f}\n"
      return saldo, extrato
   else:
      print('Apenas valores positivos são permitidos')
      return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
   print('Extrato'.center(20, '='))
   print(extrato + f"\nSaldo: R${saldo:.2f}\n" + '='*20)


def criar_usuario(dados, usuarios):
 if not dados[2].isdecimal():
    print('O CPF deve conter apenas números')
    dados.clear()
    return 0
 for u in usuarios:
   if u[2] == dados[2]:
     print('O CPF já foi cadastrado por outro usuário')
     dados.clear()
     return 0
     
 usuarios.append(dados.copy())
 dados.clear()

  
def criar_conta_corrente(cpf, usuarios, contas):
  for u in usuarios:
    if u[2] == cpf:
      nro = len(contas) + 1
      contas.append(["0001", nro, cpf])
      return 1

  print('O CPF informado não foi encontrado')


def listar_contas(usuarios, contas):
  for u in usuarios:
    print(f"======{u[0]}======")
    print(f"Data de nascimento: {u[1]}")
    print(f"CPF: {u[2]}")
    print(f"Endereço:  {u[3]}, {u[4]}, {u[5]}, {u[6]}, {u[7]}")
    for c in contas:
      if c[2] == u[2]:
        print(f"Agência: {c[0]}")
        print(f"Conta: {c[1]}")
    print("="*14)


# INÍCIO
while True:
  opcao = input(menu)
  
  if opcao == "d":
    valor = int(input('Valor de depósito: '))
    saldo, extrato = depositar(saldo, valor, extrato)

  elif opcao == "s":
     if numero_saques == LIMITE_SAQUES:
       print('Limite de saques diário atingido')

     else:
        valor = int(input('Valor de saque: '))
        saldo, extrato, numero_saques = sacar(saque=valor, saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques)

  elif opcao == "e":
    exibir_extrato(saldo, extrato=extrato)

  elif opcao == "u":
    dados.append(input('Nome: '))
    dados.append(input('Data de nascimento: '))
    dados.append(input('CPF: '))
    dados.append(input('Logradouro: '))
    dados.append(input('Número: '))
    dados.append(input('Bairro:  '))
    dados.append(input('Cidade: '))
    dados.append(input('Estado: '))
    criar_usuario(dados, usuarios)

  elif opcao == "c":
    dado = input('CPF do usuário dono da conta: ')
    criar_conta_corrente(dado, usuarios, contas_corrente)

  elif opcao == "l":
    listar_contas(usuarios, contas_corrente)
  
  elif opcao == "q": 
    break
    
  else:
    print("Operação inválida, por favor selecione novamente a operação desejada")
    