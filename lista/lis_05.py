entrada = input("Digite uma lista de números inteiros separados por espaço: ")
numeros = list(map(int, entrada.split()))
soma = sum(numeros)
print(f"A soma dos números da lista é: {soma}")
