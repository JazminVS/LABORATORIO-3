import math
def cuadrado():
	l1 = int(input("INGRESE LADO 1: "))
	l2 = int(input("INGRESE LADO 2: "))
	l3 = int(input("INGRESE LADO 3: "))
	l4 = int(input("INGRESE LADO 4: "))
	perimetro = l1 + l2 + l3 + l4
	print("EL PERIMETRO ES: "+ str(perimetro))

def triangulo():
	base = int(input("INGRESE LA BASE: "))
	altura = int(input("INGRESE LA ALTURA: "))
	l1 = int(input("INGRESE LADO 1: "))
	l2 = int(input("INGRESE LADO 2: "))
	area = (base*altura)/2
	perimetro = l1 + l2 + base
	print("EL PERIMETRO ES: "+ str(perimetro))
	print ("EL AREA DEL TRIANGULO ES: "+str(area))
	pass

def pentagono():
	lado= int(input("INGRESE EL LADO: "))
	radio= int(input("INGRESE EL RADIO: "))
	apotema=math.sqrt((radio*radio)-(1/2*1/2))
	perimetro=lado*radio
	area=(perimetro*apotema)/2
	print("EL PERIMETRO ES: "+ str(perimetro))
	print ("EL AREA DEL TRIANGULO ES: "+str(area))
	
	
a = int (input("INGRESE NUMERO DE LADOS DE SU FIGURA: "))
if (a == 1 or a == 2):
	print ("NO EXISTE FIGURA")
if (a == 3):
	print ("SU FIGURA ES UN TRIANGULO")
	triangulo()
if (a == 4):
    print ("SU FIGURA ES UN CUADRILATERO: \n") 
    cuadrado()
if (a == 5):
    print ("SU FIGURA ES UN PENTAGONO: \n") 
    pentagono()

