nomes = []
for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

print("Nomes na ordem inversa:")
for nome in reversed(nomes):
    print(nome)
