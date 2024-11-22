numeros = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

media = sum(numeros) / len(numeros)
maiores_que_media = [n for n in numeros if n > media]
print(f"A quantidade de números maiores que a média ({media:.2f}) é: {len(maiores_que_media)}")
