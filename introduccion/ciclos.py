# el python no exist este ciclo
# for (i=0,i<5,i++):
#     print("numero ," , i)

# ]este si 
for i in range(0,5):
    print("el numero es ," ,i)
    
for i in range(1,5):
    print("el numero es ," ,i)


# le dice que vaya de dos en dos desde el 19 hasta el 30
for i in range(19,30,2):
    print(i)
    
# listas----------------------
# no es un arreglo , se escribe como un arreglo pero es una lista
frutas=['pera' ,'manzana','uva']
for fruta in frutas:
    print(fruta)
# para saber el indice y la fruta   'ennumerate'<-----ayuda a sacar e indice
# f es para poner llaves y poder llamar variables , sin necesitad de estar abriendo y cerrandollaves
# es otra forma de concatenar
for indice,fruta in enumerate(fruta):
    print(f"{indice}-{fruta}"), 
    
    # hacer todo de ciclos do while , while ,agregar y eliminar datos d una lista
    
# while
numero=0
while numero==0 :
    print('angelina')           
    numero=1