def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Solicitar número ao usuário
numero = int(input("Digite um número para ver a tabuada: "))
tabuada(numero)
