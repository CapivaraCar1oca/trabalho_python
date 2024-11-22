def contar_vogais(s):
    vogais = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vogais:
            count += 1
    return count

# Solicitar frase ao usuário
frase = input("Digite uma frase: ")
print(f"O número de vogais na frase é: {contar_vogais(frase)}")
