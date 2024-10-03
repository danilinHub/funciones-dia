import math

#ejemplo para calcular el area de un triangulo rectangulo

#Variaables de entradas
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

#Proceso
def calculalarAreaTriangulo(a,b):
    area = (a*b)/2
    return area

#Invocamos la funcion
resultado = calculalarAreaTriangulo(base,altura)

print("El area del triangulo es :",resultado)
#salida
print(f"en angulo cuya base {base} ya la altura {altura} es y el resultado es: {resultado}")

#FUNCION CON ARGUMENTOS PREDETERMINADOS
def my_function(country = "colombia"):
    print("I am from "+country)

#Invocar funcion
my_function()
my_function("Sweden")

#ARGUMENTOS ARBITRARIOA puede recibir un nemro indetermnado de argumentos
def mostarEstudiantes(*args):
    print("El estudiante: "+args[2])

#INVOCAR FUNCION
mostarEstudiantes("Email","Tobias","Linus","Bill","Andres")

#ARGUMENTOS PALABRAS CLAVE
def mostrarCarro(carro1, carro2, carro3):
    print("El carro es: " +carro2)

mostrarCarro(carro1= "BMW", carro3= "ferrari", carro2= "Ford")

#ARGUMENTO ARBITRARIO **KWARGS
def mostarCliente(**kwargs):
    print("su apellido es: " + kwargs["apellido"])
mostarCliente(nombre = "Tobias", apellido = "Refsnes")

#passs funciones integradas
def miFuncion():
    pass

#funciones integradas
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

#funciones integradas
num1 = pow(7, 4)
print(num1)

#math
num2 = math.sqrt(34)
print(num2)

#modulo de matematicas
num3 = math.ceil(7.8)
num4 = math.floor(7.8)

print(num3) # returns 8
print(num4) # returns 7



















