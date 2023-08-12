menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
inicio_saques = 0
MAXIMO_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Qual o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("ERROR ! Digite algumas das opções válidas.")

    elif opcao == "2":
        valor = float(input("Digite o valor para saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = inicio_saques >= MAXIMO_SAQUES

        if excedeu_saldo:
            print("Não foi possível realizar a transação! Saldo insuficiente.")

        elif excedeu_limite:
            print("O valor do saque excede o limite. Tente um valor menor!")

        elif excedeu_saques:
            print("Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            inicio_saques += 1

        else:
            print("O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        break

    else:
        print("Opção não encontrada, por favor selecione novamente uma das opções válidas.")
