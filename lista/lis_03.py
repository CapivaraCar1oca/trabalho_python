numeros = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

pares = [n for n in numeros if n % 2 == 0]
print(f"Números pares da lista: {pares}")
