numero=42
texto=str(numero) #str ->convierte a string
print('el numero como texto es :',texto)
print(type(texto))

numero_texto="38"
numero=int(numero_texto)
print(numero+10)
print(type(numero))

altura_texto="1.75"
altura=float(altura_texto)
print('tu altura es :' ,altura)
print(type(altura))

mensaje="hola mundo"
print(len(mensaje))   #len es la longitud

lista=[1,2,3,4]
print(len(lista))

# ndexacion
texto="hola"
print(texto[0])
print(texto[3])


# slicing
texto="hola mundo"
print(texto[0:4])   #'hola'
print(texto[5:])    #'mundo'
print(texto[:4])    #'hola
print(texto[-5:])   #'mundo' (desde el final)


texto="python"
print(texto.lower())    # 'python'

texto="hola mundo"
print(texto.upper())    # 'HOLA MUNDO'  (CONVIERTE EN MAYUSCULA)

# Reemplazar texto
frase="me gusta python"
nueva=frase.replace("python", "javascrip")
print(nueva)    # 'me gusta javascript'

# qutar espacios al inicio y a final 
texto="  hola  "
print(texto.strip())    # 'hola'

# sepparar una cadena de una lista 
# convi4erte en una lista , teniendo en cuent la , 
frase="rojo,verde,azul"
colores=frase.split(",")
print(colores)  #['rojo' ,'verde','azul' ]

# unir el elemento de una lista con un separador 
palabras=["hola","mundo"]
frase=" ".join(palabras)
print(frase)    # 'hola mundo'



