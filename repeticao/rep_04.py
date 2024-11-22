num = int(input("Digite um número inteiro positivo: "))
if num >= 0:
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
    print(f"O fatorial de {num} é {fatorial}.")
else:
    print("Erro: O número deve ser positivo.")
