nome = input("informe seu nome:").strip().upper()
idade = input("informe sua idade:")

if nome and idade:
    print(f"seu nome e {nome}")
    print(f"seu nom invertido e {nome[::-1]}")
    
    if " " in nome:
      print("seu nome comtem espaços")
    else:
       print("seu nome Não com tem espaços")

    print(f"seu nome comtem {len(nome)} letras")
    print(f"a primeira letra do seu nome e {nome[0]}") 
    print(f"a ultima letra do seu nome e {nome[4]}")
else:
   print("Desculpe, voce deixou campos vazios") 