inicio = int(input("Digite o início do intervalo (inteiro positivo): "))
fim = int(input("Digite o fim do intervalo (inteiro positivo): "))
if inicio <= fim:
    print("Números pares no intervalo:")
    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            print(i)
else:
    print("Erro: O início do intervalo deve ser menor ou igual ao fim.")
