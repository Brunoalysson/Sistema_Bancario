from conta import Conta

print("Sistema Bancário")

number = int(input("Digite o número da conta:"))

conta1 = Conta(number)
print("Número da conta:", conta1.numero)
print("Saldo:", conta1.saldo)

credito = int(input("Digite o valor do crédito:"))
credits = conta1.credito(conta1 ,credito)

debito = int(input("Digite o valor do débito:"))
debits = conta1.debito(conta1, debito)
