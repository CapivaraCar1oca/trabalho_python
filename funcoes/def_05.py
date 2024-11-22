def media(lista):
    return sum(lista) / len(lista)

# Solicitar lista de números ao usuário
numeros = list(map(float, input("Digite números separados por espaço: ").split()))
print(f"A média dos números é: {media(numeros)}")
