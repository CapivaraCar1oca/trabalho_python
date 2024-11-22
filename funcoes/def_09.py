def é_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# Solicitar ano ao usuário
ano = int(input("Digite um ano: "))
if é_bissexto(ano):
    print(f"{ano} é bissexto.")
else:
    print(f"{ano} não é bissexto.")
