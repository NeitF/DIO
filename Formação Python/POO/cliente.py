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
        for c, e in enumerate(self._contas):
            print(f"==== CONTA {e} ====","\n", c)
        
        
class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento




    

    


        
    