alunos = {}
for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota do aluno {nome}: "))
    alunos[nome] = nota

for nome, nota in alunos.items():
    print(f"Aluno: {nome}, Nota: {nota}")
