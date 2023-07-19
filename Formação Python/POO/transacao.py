from abc import ABC, abstractmethod

class Transacao(ABC):
    @abstractmethod
    def registrar(self, Conta):
        pass
    

class Deposito:
    def __init__(self, valor):
        self._valor = valor
    
    def registrar(self, Conta):
        # dep = f"Depósito: {self._valor}"
        Conta.historico.adicionar_transacao(self)
        
    @property
    def valor(self):
        return self._valor or 0
        

class Saque:
    def __init__(self, valor):
        self._valor = valor
        
    def registrar(self, Conta):
        # saq = f"Saque: {self._valor}"
        Conta.historico.adicionar_transacao(self)
    
    @property
    def valor(self):
        return self._valor or 0