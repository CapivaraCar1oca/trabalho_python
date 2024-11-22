numeros = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

maior = max(numeros)
indice_maior = numeros.index(maior)
numeros[indice_maior] = 0

print(f"Lista atualizada: {numeros}")
