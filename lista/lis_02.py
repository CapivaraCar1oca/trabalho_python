entrada = input("Digite uma lista de números separados por espaço: ")
numeros = list(map(int, entrada.split()))
print(f"O maior número é: {max(numeros)}")
print(f"O menor número é: {min(numeros)}")
