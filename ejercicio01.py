# crear un pequeño software con 3 clases: estudiantes, profesores y notas.
# en los 3 deben estar el metodo constructor
# en estudiantes debe haber un metodo para cambiar al estudiante de estado activo e inactivo (true o false)
# en la clase estudiantes debe haber un atributo de asignaturas tipo lista
# en estudiantes debe haber un metodo agregar asignatura del estudiante
# en la clase profesor debe haber un metodo calificar
# en la clase notas debe haber un metodo que reciba la asignatura y la nota y diga si aprobo o no aprobo
# en la clase notas debe haber un metodo para imprimir todas las notas del estudiante de todas las asignaturas que tiene ese estudiante y si aprobo cada una utilizando el metodo anterior
# las notas solo pueden ser de 0 a 5
# donde se imprimen todas las notas debe salir quien califico (nombre del profesor)

from typing import List

class Estudiante:
    def __init__(self, id_estudiante: int, nombre: str, edad: int, estado: bool = True):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.edad = edad
        self.estado = estado
        self.asignaturas = []

    # metodo para cambiar el estado del estudiante
    def cambiar_estado(self):
        self.estado = not self.estado

    def agregar_asignatura(self, asignatura: str):
        if asignatura not in self.asignaturas:
            self.asignaturas.append(asignatura)

    # imprimir datos del estudiante metodo imprimir_estudiante
    def imprimir_estudiante(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Estado: {self.estado}")
        print(f"Asignaturas: {self.asignaturas}")
        

class Profesor:
    def __init__(self, id_profesor: int, nombre: str, edad: int):
        self.id_profesor = id_profesor
        self.nombre = nombre
        self.edad = edad

    def calificar(self, notas, estudiante: 'Estudiante', nota: int, asignatura: str):
        if nota < 0 or nota > 5:
            print("Nota fuera de rango")
            return False
        if asignatura not in estudiante.asignaturas:
            print(f"El estudiante {estudiante.nombre} no está inscrito en la asignatura {asignatura}")
            return False
        notas.agregar_nota(estudiante, self, nota, asignatura)
        return True

class Notas:
    def __init__(self):
        self.notas : List[dict] = []

    def agregar_nota(self, estudiante: Estudiante, profesor: Profesor, nota: int, asignatura: str):
        self.notas.append({
            "estudiante": estudiante.nombre,
            "profesor": profesor.nombre,
            "nota": nota,
            "asignatura": asignatura
        })

    def ver_notas(self, estudiante: Estudiante):
        for nota in self.notas:
            if nota["estudiante"] == estudiante.nombre:
                print(f"El estudiante {nota['estudiante']} obtuvo una nota de {nota['nota']} en la asignatura {nota['asignatura']} de {nota['profesor']}")
                if nota["nota"] >= 3:
                    print(f"El estudiante aprobó la asignatura {nota['asignatura']} con nota {nota['nota']} de {nota['profesor']}")
                else:
                    print(f"El estudiante no aprobó la asignatura {nota['asignatura']} con nota {nota['nota']} de {nota['profesor']}")
            print("--" * 40)






estudiante = Estudiante(1, "Juan", 20)
estudiante.imprimir_estudiante()
print("--" * 40)
estudiante.agregar_asignatura("Matematicas")
estudiante.agregar_asignatura("Fisica")
estudiante.agregar_asignatura("Quimica")

profesor = Profesor(1, "Pedro", 30)
notas = Notas()
profesor.calificar(notas, estudiante, 4, "Matematicas")
profesor.calificar(notas, estudiante, 5, "Fisica")
profesor.calificar(notas, estudiante, 2, "Quimica")
notas.ver_notas(estudiante)



estudiante.cambiar_estado()

print("--" * 40)    

estudiante.imprimir_estudiante()

estudiante.cambiar_estado()
