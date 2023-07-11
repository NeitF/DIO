menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar usuário
[q] Sair

=>
"""

#VARIÁVEIS
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""
usuarios = []

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


def criar_usuario(nome, nasc, cpf, endereco, usuarios):
 pass
 

def criar_conta():
  pass


def listar_contas():
  pass


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
    nome = input('Nome: ')
    nasc = input('Data de nascimento: ')
    cpf = input('CPF: ')
    logradouro = input('Logradouro: ')
    numero = input('Número: ')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    estado = input('Estado')
    
  elif opcao == "q": 
    break
  else:
    print("Operação inválida, por favor selecione novamente a operação desejada")
    