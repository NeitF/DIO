from abc import ABC, abstractmethod

class Transacao(ABC):
    @abstractmethod
    def registrar(Conta):
        pass
    

class Deposito:
    def __init__(self, valor):
        self._valor = valor


class Saque:
    def __init__(self, valor):
        self._valor = valor