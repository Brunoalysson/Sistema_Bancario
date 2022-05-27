class Conta:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo
    
    def setNumero(self, numero):
        self.numero = numero

    def setSaldo(self, saldo):
        self.saldo = saldo
    
    def getNumero(self):
        return self.numero
    
    def getSaldo(self):
        return self.saldo