from conta import Conta

resposta = 'S'

contas=[]

while (not resposta == 'N'):
    print("\nMENU\n")
    print("1- Criar conta")
    print("2- Consultar saldo")
    print("3- Crédito")
    print("4- Débito")
    print("5- Transferência")
    
    escolha = int(input("Digite a operação que deseja fazer:"))
    
    if escolha ==1:
        number = int(input("Digite o número da conta:"))
        nova = Conta(number)
        '''contas.append(nova.numero)
        contas.append(nova.saldo)'''
        contas.append(nova)
        
    if escolha ==2:
        number = int(input("Digite o número da conta:"))
        for i in range(len(contas)):
            if number == contas[i].numero:
                print("Saldo:", contas[i].saldo)
        
    if escolha ==3:
        number = int(input("Digite o número da conta:"))
        valor = int(input("Digite o valor do crédito:"))
        for i in range (len(contas)):
            if number == contas[i].numero:
                contas[i].saldo+= valor
                print("Saldo:", contas[i].saldo)
                
    if escolha ==4:
        number = int(input("Digite o número da conta:"))
        valor = int(input("Digite o valor do dédito:"))
        for i in range (len(contas)):
            if number == contas[i].numero:
                if valor>contas[i].saldo or contas[i].saldo<0:
                    print("Saldo insuficiente")    
                    break
                contas[i].saldo -= valor
                print("Saldo:", contas[i].saldo)
    
    if escolha ==5:
        contaOrigem = int(input("Digite o número da conta de origem:"))
        contaDestino = int(input("Digite o número da conta de destino:"))
        valor = int(input("Digite o valor da transferência:"))
        for i in range(len(contas)):
            if contaOrigem == contas[i].numero:
                if valor>contas[i].saldo or contas[i].saldo<0:
                    print("Saldo insuficiente")    
                    break
                contas[i].saldo -= valor
                for j in range(len(contas)):
                    if contaDestino == contas[j].numero:
                        contas[j].saldo += valor
                        print("Transferência Realizada")
        
    resposta = input("Deseja fazer outra operação? S/N:")
    