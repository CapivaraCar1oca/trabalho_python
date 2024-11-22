palavra = input("Digite uma palavra: ")
frequencia = {}
for letra in palavra:
    frequencia[letra] = frequencia.get(letra, 0) + 1
print(frequencia)
