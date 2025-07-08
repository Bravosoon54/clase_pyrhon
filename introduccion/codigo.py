print('hola mundo')
print('estoy aprendiendo , PYTHON')
nombre="Juan Roman"
otroNombre="Zharick londono"
estado_civil="novios"
print(nombre ,"y",otroNombre ,"son",estado_civil)
numdecimal=78.90
edad=19
genero="F"
# saber que tipo de dato/variable es

print(type(numdecimal))
print(type(nombre))

# condicionales

if edad>=18:
    if genero=="M":
        print("mayor de edad, hombre")
    else:
        if genero=="F":
            print("mayor de edad , mujer")
else:
    if genero=="M":
        print("menor de edad, hombre")
    else:
        if genero=="F":
            print("menor de edad , mujer")
            


# -----------------------------------------------
#simpre poner en el input espacio
el_Numero=input("escrie un numero del 1 al 10 pero en letras en ingles  ")
match(el_Numero):
    case 'one':
        print('es el uno')
    case 'two':
        print('es el dos')
    case 'three':
        print('es el tres')
    case 'four':
        print('es el cuatro')
    case 'five':
        print('es el cinco') 
    case _:  #el _ es por si no acerta ninguno
        print('no le pegaste a ningunoo')
        
        
print('apoyo a angelina , BESO ,BESO!')

# PARACREAR FUNCION S EUTILIZA DEF

def sumar(n1,n2):
    resultado=n1+n2
    return resultado

print(sumar(1,2))
guardar_resultado=sumar(2,2)
print(guardar_resultado)
# convertir un numero string a entero
dia_semana=int(input("ingrese el numero del dia de la semana "))

def nombreDiaSemana(dia_semana):
    if dia_semana==1:
        print('es lunes')
    elif dia_semana==2:
        print('es martes')   
    elif dia_semana==3:
        print('es miercoles')   
    elif dia_semana==4:
        print('es jueves')
    elif dia_semana==5:
        print('es viernes') 
    elif dia_semana==6:
        print('es sabado')  
    elif dia_semana==7:
        print('es domingo')   
    else:
        print('dia invalido')
    nombreDiaSemana(dia_semana)