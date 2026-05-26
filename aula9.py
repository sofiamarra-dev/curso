nome = str(input("digite seu nome:"))
encontrar = input("digite o que deseja encontrar:")

if encontrar in nome:
    print(f"{encontrar}esta em {nome}")
else:
    print (f"{encontrar} nao esta em {nome}")
