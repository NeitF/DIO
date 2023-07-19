from abc import ABC, abstractmethod

class Transacao(ABC):
    @abstractmethod
    def registrar(self, Conta):
        pass
    

class Deposito:
    def __init__(self, valor):
        self._valor = valor
    
    def registrar(self, Conta):
        print(Conta.historico.a())
        
    @property
    def valor(self):
        return self._valor or 0
        

class Saque:
    def __init__(self, valor):
        self._valor = valor
        
    def registrar(self, Conta):
        pass
    
    @property
    def valor(self):
        return self._valor or 0