while True:
   try:
      num_1 = float(input("informe um valor:")) 
      num_2 = float(input("Informe o segundo valor:"))
   except ValueError:
       print("Um dos valores ou ambos sao invalidos")
       continue

   operador = input("Informe um operador +-/*:")
    
   if operador not in "+-/*":
      print ("operador invalido")
      continue
   
   if operador == "+":
    resultado = num_1 + num_2
   elif operador == "-":
       resultado = num_1 - num_2
   elif operador == "/":
       resultado = num_1 / num_2
   elif operador == "*":
       resultado = num_1 * num_2
   else:
       print("Operador invalido ")
       continue
   print("Calculando ...")
   print (f"Resultado:{num_1}{operador}{num_2}={resultado}")
   
   sair = input("Quer sair ? [s]im").lower().startswith("s")
   
   if sair:
       break
       
       
        