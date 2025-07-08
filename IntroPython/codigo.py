#AQUI NO SE USAN LLAVES{}
print("hola mundo")
print("estoy aprendiendo python")

nombre = 'Juan Roman'
otroNombre = 'Zharick Exelente'
numero = 38
numDecimal = 88.90
unBoolean = True

print (nombre)
print(otroNombre)
print(numero)
print(numDecimal)
print(unBoolean)

print(type(numDecimal))
print(type(nombre))
print(type(unBoolean))

edad = 19
genero = 'M' #M MASCULINO , F FEMENINO O OTRO

if edad < 18:
    if genero == 'M':
        print("Hombre menor de edad")
    else:
        if genero == 'F':
            print("Mujer menor de edad")
        else:
            print("Persona menor de edad de otro genero")
else:
    if genero == 'M':
        print("Hombre mayor de edad")
    else:
        if genero == 'F':
            print("Mujer mayor de edad")
        else:
            print("Persona mayor de edad de otro genero")
            
# elnumero = input("Escribe un numero del 1 al 10 pero en letras en ingles: ")
# match (elnumero):
#     case "one":
#         print('es el Uno')
#     case "two":
#         print('es el Dos')
#     case "three":
#         print('es el Tres')
#     case "four":
#         print('es el Cuatro')
#     case "five":
#         print('es el Cinco')
#     case "six":
#         print('es el Seis')
#     case "seven":
#         print('es el Siete')
#     case "eight":
#         print('es el Ocho')
#     case "nine":
#         print('es el Nueve')
#     case "ten":
#         print('es el Diez')
#     case _:
#         print('No es un numero del 1 al 10')
        
def sumar (n1, n2):
    resultado = n1 + n2
    return resultado

print(sumar(5, 5))

elresultado = sumar(23,54)
print(elresultado)

diaSemana = int(input('ingrese el numero del dia de la semana: '))
def nombreDiaSemana(diaSemana):
    if diaSemana == 1:
        print('Lunes')
    elif diaSemana == 2:
        print('Martes')
    elif diaSemana == 3:
        print('Miercoles')
    elif diaSemana == 4:
        print('Jueves')
    elif diaSemana == 5:
        print('Viernes')
    elif diaSemana == 6:
        print('Sabado')
    elif diaSemana == 7:
        print('Domingo')
    else:
        print('No es un dia de la semana')

nombreDiaSemana(diaSemana)

