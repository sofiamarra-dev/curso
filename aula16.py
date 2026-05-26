# Introducao ao try/except
# try -> tentar executar o codigo
# except -> ocorreu algum erro ao tentar executar

numero_str = input(
    "Vou dobrar o numero que vc digitar:"
    )

try:
    numero_float = float(numero_str)
    print("float:",numero_float)
    print(f"O dobro de {numero_str} e {numero_float * 2:.2f}")
except:
    print("Isso nao e um numero")
    



# if numero_str.isdigit():
#    numero_float= float(numero_str)
#    print(f"o dobro de {numero_str} e {numero_float* 2:.2f}")  
# else:
#    print("isso nao e um numero")