from conta import Conta

print("Sistema Bancário")

number = int(input("Digite o número da conta:"))

conta1 = Conta(number)
print("Número da conta:", conta1.numero)
print("Saldo:", conta1.saldo)
