class Conta:
    
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo
        print("Conta criada")
        
    def setNumero(self, numero):
        self.numero = numero

    def setSaldo(self, saldo):
        self.saldo = saldo
    
    def getNumero(self):
        return self.numero
    
    def getSaldo(self):
        return self.saldo
        
    def imprimeSaldo(self, numero):
        self.numero = numero
        print("Saldo: R$ %2.f" %self.saldo)

    def credito(self, numero, valor):
        self.saldo += valor
        print("Novo Saldo:", self.saldo)
    
    def debito(self, numero, valor):
        numero.saldo -= valor
        print("Novo Saldo:", numero.saldo)
