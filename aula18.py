# flag (Bandeira)- Marcar um local
# None = valor vazio ou  nenhum valor ainda
# is e is not = é ou não é (tipo,valor,identidade)
# id = Identidade


# flag (Bandeira)- Marcar um local
# None = Não valor
# is e is not = é ou não é (tipo,valor,identidade)
# id = Identidade

condição = False
passou_no_if = None
# if condição:
#    print("Faça algo")
#    print("passou no if")
# else:
#    print("Não faça algo")
#    print(" Não passou no if")


if condição:
   passou_no_if = True
   print("faca algo")
else:
   print(" Nao faca algof")


if passou_no_if is None:
   print(" Não passou no if")
if passou_no_if is not None:
   print("passou no if")