from abc import ABC, abstractmethod
from historico import *
from cliente import *


class Conta(ABC):
    def __init__(self, numero, Cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._Cliente = Cliente
        self._Historico = Historico
    
    def sacar(self, valor):
        if valor < 0:
            msg = "Apenas valores positivos são permitidos"
            return False, msg
        elif (self._valor - valor) < 0:
            msg = "Saldo insuficiente"
            return False, msg
        else:
            msg = "Saque realizado com sucesso"
            return True, msg
        
    def depositar(self, valor):
        if  valor < 0:
            msg = "Apenas valores positivas são permitidos"
            return False
        else:
            self._saldo += valor
            msg = "Depositado com sucesso!"
            return True
        
    def __str__(self):
        return f""" Saldo: {self._saldo}
                    """
        
    @property
    def saldo(self):
        return self._saldo or 0
        
    @classmethod
    def nova_conta(cls, numero, Cliente):
        return cls(numero, Cliente)

                
class ContaCorrente(Conta):
    def __init__(self, numero, Cliente):
        super().__init__(numero, Cliente)
        self._limite = 500
        self._limiteSaques = 3
        
    def sacar(self, valor):
        if self._limiteSaques == 0:
            msg = "Limite de saques diário atingido"
            return False, msg
        elif valor > self._limite:
            msg = "Valor informado ultrapassa o limite permitido de R$500"
            return False, msg
        else: 
            return super().sacar(valor)