# Lugares vulneráveis à fome no Brasil, no formato ilustrativo.
MapaDaFome = ["São Paulo", "Maceió", "São Gonçalo", "Entre Rios"]


# ONGs já cadastradas no sistema.
listaONGs = ["Amigos do Bem", "05108918000172", "Sao Paulo", "SP", "Mão Amiga",
             "05948372615467", "Entre Rios", "SC", "Nutrir", "06018251000109", "Maceió", "AL"]

print("Bem vindo!!! Escolha uma das opções a seguir:   ")
print("1-  Cadastrar uma ONG.")
print("2-  Consultar quais são as cidades mais vulneráveis a fome.")
print("3-  Consultar quais são as nossas ONGs parceiras.")
opcao = input("Digite aqui:   ")
print()

if opcao == "1":
    print("Cadastre sua ONG em nosso portal!!!   ")

# Cadastrando ONGs.
    nomeONG = input("Digite o nome da ONG:   ")
    print(nomeONG)
    cnpjONG = input("Digite o CNPJ da ONG (sem pontos e barras):   ")
    print(cnpjONG)
# Verificando se o tamanho do CNPJ cadastrado é válido.
    tam = len(cnpjONG)

    while tam != 14:
        print("CNPJ inválido! Tente novamente.")
        cnpjONG = input("Digite o CNPJ da ONG (sem pontos e barras):   ")
        tam = len(cnpjONG)
        print(len(cnpjONG))

    if tam == 14:
        cidadeONG = input("Digite a cidade em que a ONG está localizada:   ")
        print(cidadeONG)
        estadoONG = input("Digite o estado em que a ONG está localizada:   ")
        print(estadoONG)
        resp = input("Aceita receber notificações? S/N   ")

    # Adicionando dados à lista.
        listaONGs.append(str(nomeONG))
        listaONGs.append(str(cnpjONG))
        listaONGs.append(str(cidadeONG))
        listaONGs.append(str(estadoONG))

    for a in MapaDaFome:
        if a == cidadeONG:
            print(
                "A ONG cadastrada está em uma cidade que possui alto índice de insegurança alimentar.")
            print()

    print("Estamos felizes com seu cadastro!!! Em breve enviaremos notificações sobre os lugares vúlneráveis em sua região.")


if opcao == "2":
    print("Cidades em situação de vulnerabilidade alimentar:   ")
    for v in MapaDaFome:
        print(v)

if opcao == "3":
    b = 0
    print("ONGs parceiras:  ")
    for i in range(int(len(listaONGs)/4)):

        print(listaONGs[b])
        b = b + 4
