def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [0]\tSair
    => """
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Deposito concluído com sucesso!")
    else:
        print("\nOperação falhou! Tente novamente.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, inicio_saques, maximo_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = inicio_saques >= maximo_saques

    if excedeu_saldo:
        print("\nError! Saldo insuficiente.")

    elif excedeu_limite:
        print("\nError! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nError! Você excedeu o seu limite de saque. ")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        inicio_saques += 1
        print("\n Saque concluído com sucesso!")

    else:
        print("\nError! Digite um valor válido. ")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não há registros." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nError! Este CPF já está cadastrado, digite um novo CPF!")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nError! Usuário não encontrado.")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    MAXIMO_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    inicio_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Qual o valor a ser depositado: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Digite o valor para saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                inicio_saques=inicio_saques,
                maximo_saques=MAXIMO_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Error! Opção inválida, digite uma das opções válidas.")


main()