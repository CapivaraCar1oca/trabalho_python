try:
    with open("alunos.txt", "r") as file:
        alunos = file.readlines()
        for aluno in alunos:
            if aluno.strip().startswith("A"):
                print(aluno.strip())
except FileNotFoundError:
    print("Erro: O arquivo 'alunos.txt' não foi encontrado.")
