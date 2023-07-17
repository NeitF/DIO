from abc import ABC, abstractmethod

class Conta:
    def __init__(self, numero, Cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = Cliente
        self._historico = Historico()
        
    @property
    def saldo(self):
        return self._saldo or 0
    
    
    @classmethod
    def nova_conta(cls, Cliente, numero):
        return cls(numero, Cliente)
    
    
    def sacar(self, valor):
        if valor < self._saldo:
            self._saldo -= valor
            return valor
    
    
    def depositar(self, valor):
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}:{valor}' for chave, valor in self.__dict__.items()])}"
    
class Historico:
    def __init__(self):
        self._historico = []
    
    def adicionar_transacao(self, transacao):
        pass
    

class Transacao(ABC):
    @abstractmethod
    def registrar(self, Conta):
        pass
    

class Deposito(Transacao):
    def __init__(self, Conta, valor):
        super().__init__(Conta)
        self._valor = valor
        
    
    def registrar(self, Conta):
        pass
        
    
        
class Saque(Transacao):
    def __init__(self, Conta, valor):
        super().__init__(Conta)
        self._valor = valor    
        
    
    def registrar(self, Conta):
        pass


class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, Cliente):
        super.__init__(saldo, numero, agencia, Cliente)
        self._limite = 500
        self._limita_saques = 3
        
        
class Cliente(ABC):
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
        
    
    def adicionar_conta(self, saldo, numero, agencia):
        self._contas.append(ContaCorrente(saldo, numero, agencia, self))
    
        
# COMEÇAR O PROGRAMA PELA INSTANCIAÇÃO DA PESSOA FÍSICA
class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

