# ATIVIDADE
#isdigit verefica se e numero
# entrada = input("Digite um numero inteiro: ")

# if entrada.isdigit():
#    numero = int(entrada)

#    if  numero  % 2 == 0:    # 0u if entrada % 2 != 0:
#       print("seu numero e par") #ou ("seu numero e inpar")
#    else:
#       print("seu numero e inpar")# ou ("seu numero e par")
# # inverte porque quando o resto e 1 , o python entende como true e 
# # 0 = false(else) que e par e 1 inpar
       
# else:
#    print("voce nao digitou um numero inteiro")

try:
    numero = int(input("Informe um numero:"))

    if numero %2 == 0:
        print("Numero par")
    else:
        print("Numero impar")

except ValueError:
    print("Digite apenas numeros inteiros")
