nome = (input("Qual seu primeiro nome :")).strip()
tamanho_nome = len(nome)

if not nome:
    print("Voce nao digitou um nome")
elif not nome.isalpha():
    print("Digite apenas letras no  nome")
elif tamanho_nome <=4 :
    print("Seu nome e curto")
elif  tamanho_nome <= 6:
    print("Seu nome e normal")
else:
    print("Seu nome e muito grande")
         