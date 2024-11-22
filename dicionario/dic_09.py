notas = {}
for _ in range(4):
    disciplina = input("Digite o nome da disciplina: ")
    nota = float(input(f"Digite a nota de {disciplina}: "))
    notas[disciplina] = nota
media = sum(notas.values()) / len(notas)
print(f"A média das notas é: {media:.2f}")
