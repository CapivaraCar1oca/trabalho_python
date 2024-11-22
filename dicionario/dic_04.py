pessoas = {"Ana": 25, "João": 30, "Maria": 22}
nome = input("Digite o nome que deseja procurar: ")
if nome in pessoas:
    print(f"{nome} está no dicionário.")
else:
    print(f"{nome} não foi encontrado no dicionário.")
