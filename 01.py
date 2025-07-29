class Usuario:
    #atributos de clase (compartido por todas las instancias)
    plataforma = "MiApp 1.0"

    #metodo contructor se ejecuta al instanciar la clase
    #se ejecuta cuando crea un objeto de la clase
    def __init__(self, nombre, email):
        #atributos de instancia
        self.nombre = nombre
        self.email = email
        self.activo = True

    def saludar(self):
        return f"Hola, soy {self.nombre}"
    
    def desactivar(self):
        self.activo = False
        return f"Usuario {self.nombre} desactivado"

#Crear objetos (instancias)
usuario1 = Usuario("Ana García", "ana@gmail.com")
usuario2 = Usuario("Carlos López", "carlos@gmail.com")
usuario3 = Usuario("Juan Bravo", "JBravo@gmail.com")

print(usuario1.saludar()) #Hola, soy Ana García
print(usuario2.plataforma) #MiApp 1.0

respuestaB = usuario3.saludar()
print(respuestaB) 