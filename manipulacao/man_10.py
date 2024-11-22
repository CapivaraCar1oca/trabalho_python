entrada = input("Digite sua entrada para o diário: ")

try:
    with open("diario.txt", "a") as file:
        file.write(f"{entrada}\n")
    print("Sua entrada foi adicionada ao diário.")
except FileNotFoundError:
    with open("diario.txt", "w") as file:
        file.write(f"{entrada}\n")
    print("O diário foi criado e sua entrada foi adicionada.")
