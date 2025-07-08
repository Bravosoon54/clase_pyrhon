numero = 42
texto =str(numero)
print("El numero como texto es:", texto)
print(type(texto)) #<class 'str'>


numero_texto = "30"
numero = int(numero_texto)
print(numero + 10) #40
print(type(numero)) # <class 'int'>


altura_texto = "1.75"
altura = float(altura_texto)
print("Tu altura es:", altura)
print(type(altura)) # <class 'float'>

mensaje = "Hola mundo"
print(len(mensaje)) # 10 (espacio incluido)

lista = [1, 2, 3, 4]
print(len(lista)) # 4

#indexacion
texto = "Hola"
print(texto[0]) # H
print(texto[3]) # a

#Slicing
texto = "Hola mundo"
print(texto[0:4]) # Hola
print(texto[5:]) # mundo
print(texto[:4]) # Hola
print(texto[-5:]) # mundo (desde el final)

texto = "PYTHON"
print(texto.lower()) # python

texto = "hola mundo"
print(texto.upper()) # HOLA MUNDO

#reemplazar texto
frase ="me gusta python"
nueva = frase.replace("python", "javaScript")
print(nueva) # me gusta javaScript

#quitar espacios al inicio y al final
texto = "   hola   "
print(texto.strip()) # hola

# separar una cadena en una lista
frase = "rojo,verde,azul"
colores = frase.split(",")
print(colores) # ['rojo', 'verde', 'azul']

#unir elelmentos de una lista con un separador 
palabras = ["hola", "mundo"]
frase =" ".join(palabras)
print(frase) # hola mundo