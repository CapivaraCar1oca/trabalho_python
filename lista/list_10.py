lista1 = []
lista2 = []

print("Digite os números para a primeira lista:")
for i in range(5):
    num = int(input(f"Lista 1 - Número {i+1}: "))
    lista1.append(num)

print("Digite os números para a segunda lista:")
for i in range(5):
    num = int(input(f"Lista 2 - Número {i+1}: "))
    lista2.append(num)

soma_listas = [lista1[i] + lista2[i] for i in range(5)]
print(f"Nova lista com a soma dos elementos correspondentes: {soma_listas}")
