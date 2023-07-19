class Historico:
    def __init__(self):
        self._historicoTransacoes = []
    
    def adicionar_transacao(self, Transacao):
       str = f"{Transacao.__class__.__name__} : R${Transacao.valor}"
       self._historicoTransacoes.append(str)
    
    @property
    def historico_transacoes(self):
        return self._historicoTransacoes