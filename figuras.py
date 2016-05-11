
def cuadrado():
	l1 = int(input("INGRESE LADO 1: "))
	l2 = int(input("INGRESE LADO 2: "))
	l3 = int(input("INGRESE LADO 3: "))
	l4 = int(input("INGRESE LADO 4: "))
	perimetro = l1 + l2 + l3 + l4
	print("EL PERIMETRO ES: "+ str(perimetro))


a = int (input("INGRESE NUMERO DE LADOS DE SU FIGURA: "))
if (a == 1 or a == 2):
	print ("NO existe figura de un lado")
if (a == 4):
    print ("SU FIGURA ES UN CUADRILATERO: \n") 
    cuadrado()

