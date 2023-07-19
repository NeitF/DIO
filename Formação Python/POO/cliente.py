from abc import ABC, abstractmethod
from transacao import *
from conta import *

class Cliente(ABC):
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []   
    
    def abrir_conta(self, numero, instancia):
        self._contas.append(ContaCorrente(numero, instancia))
    
    def listarContas(self):
        for e, c in enumerate(self._contas):
            print(f" CONTA {(e)} ".center(50, "="), f"\n {c}")
            print(c.saldo)
            
    def realizar_transacao(self, Conta, Transacao):
        if isinstance(Transacao, Saque):
            result, msg = Conta.sacar(Transacao.valor)
        else:
            result, msg = Conta.depositar(Transacao.valor)
            
        if result:
            print(msg)
        else:
            print("ERRO\n", msg)
            
    @property
    def contas(self):
        return self._contas 
    
        
class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
    
    @property
    def nome(self):
        return self._nome or 0
