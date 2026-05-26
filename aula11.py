# interpolacao basica de strings
# s - string
# d e i - int
# f - float
# x e x - Hexadecimal (ABCCDEF012345678)

nome = "Luiz" 
preco = 1000.95897643
variavel = " %s, o preco  e  R$%.2f " %(nome,preco)
print(variavel)
print("O hexadecimal de %d e %04X"%(15, 15))