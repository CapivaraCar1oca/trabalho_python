nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

with open("usuario.txt", "a") as file:
    file.write(f"Nome: {nome}, Idade: {idade}\n")
