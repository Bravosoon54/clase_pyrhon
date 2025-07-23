class Luchador:
    def __init__(self, nombre, vida, fuerza, resistencia, agilidad, genero, energia):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.resistencia = resistencia
        self.agilidad = agilidad
        self.genero = genero
        self.energia = energia
        self.usos_esquivar = 0
        self.esquivando = False
        self.turnos_sin_energia = 0

    def calcular_danio(self, potencia_movimiento=0):
        return self.fuerza + self.energia + self.agilidad + potencia_movimiento

    def update_vida(self, danio):
        if self.esquivando:
            danio = danio // 2
            print(self.nombre, "esquivó: daño reducido un 50%")
            self.esquivando = False

        if danio > self.resistencia:
            daño_real = danio - self.resistencia
        else:
            daño_real = 0

        self.vida -= daño_real
        return daño_real

    def recuperar_energia(self):
        self.energia -= 1
        self.energia += 2
        print(self.nombre, "recupera energía. Ahora tiene:", self.energia)

    def punio(self):
        if self.energia <= 0:
            print(self.nombre, "no tiene energía para usar 'puño'.")
            return None
        self.energia -= 1
        return self.calcular_danio(potencia_movimiento=1)

    def patada(self):
        if self.energia <= 0:
            print(self.nombre, "no tiene energía para usar 'patada'.")
            return None
        self.energia -= 1
        return self.calcular_danio(potencia_movimiento=2)

    def codazo(self):
        if self.energia <= 0:
            print(self.nombre, "no tiene energía para usar 'codazo'.")
            return None
        self.energia -= 1
        return self.calcular_danio(potencia_movimiento=3)

    def rodillazo(self):
        if self.energia <= 0:
            print(self.nombre, "no tiene energía para usar 'rodillazo'.")
            return None
        self.energia -= 1
        return self.calcular_danio(potencia_movimiento=4)

    def llave(self):
        if self.energia <= 0:
            print(self.nombre, "no tiene energía para usar 'llave'.")
            return None
        self.energia -= 1
        return self.calcular_danio(potencia_movimiento=6)

    def esquivar(self):
        if self.usos_esquivar >= 3:
            print(self.nombre, "ya no puede usar 'esquivar' más de 3 veces.")
            return False
        if self.energia <= 0:
            print(self.nombre, "no tiene energía para usar 'esquivar'.")
            return False
        self.energia -= 1
        self.usos_esquivar += 1
        self.esquivando = True
        print(self.nombre, "usó 'esquivar'. Usos:", self.usos_esquivar, "/3")
        return True


class Pelea:
    luchadores = []
    turno = 0

    def agregar_luchadores(self, luchador1, luchador2):
        self.luchadores = [luchador1, luchador2]

    def cambio_turno(self):
        self.turno = 1 - self.turno

    def mostrar_estado(self):
        for luchador in self.luchadores:
            print("-----")
            print("Nombre:", luchador.nombre)
            print("Vida:", luchador.vida)
            print("Energía:", luchador.energia)
            print("Esquivar usado:", luchador.usos_esquivar, "/3")

    def verificar_ganador(self):
        if self.luchadores[0].vida <= 0:
            print("\n¡", self.luchadores[1].nombre, "---GANA LA PELEA---")
            return True
        elif self.luchadores[1].vida <= 0:
            print("\n¡", self.luchadores[0].nombre, "---GANA LA PELE---")
            return True
        return False

    def atacar(self, tipo_ataque):
        atacante = self.luchadores[self.turno]
        defensor = self.luchadores[1 - self.turno]

        if atacante.energia <= 0:
            atacante.turnos_sin_energia += 1
            print(atacante.nombre, "no tiene energía suficiente. Pierde el turno.")
            if atacante.turnos_sin_energia >= 2:
                atacante.energia += 1
                atacante.turnos_sin_energia = 0
                print(atacante.nombre, "ha pasado 2 turnos sin energía. Recupera 1 energía gratis.")
            return True

        if atacante.energia > 0:
            atacante.turnos_sin_energia = 0

        if tipo_ataque == "esquivar":
            resultado = atacante.esquivar()
            return False

        if tipo_ataque == "recuperar":
            atacante.recuperar_energia()
            return True

        if tipo_ataque == "punio":
            danio = atacante.punio()
        elif tipo_ataque == "patada":
            danio = atacante.patada()
        elif tipo_ataque == "codazo":
            danio = atacante.codazo()
        elif tipo_ataque == "rodillazo":
            danio = atacante.rodillazo()
        elif tipo_ataque == "llave":
            danio = atacante.llave()
        else:
            print("Movimiento no válido. Intenta de nuevo.")
            return False

        if danio is None:
            return False

        danio_real = defensor.update_vida(danio)
        print(atacante.nombre, "atacó con", tipo_ataque)
        print(defensor.nombre, "recibe", danio_real, "de daño")
        print(defensor.nombre, "queda con", defensor.vida, "de vida.")
        return True


luchador1 = Luchador("Arismedi", 100, 5, 2, 4, "M", 8)
luchador2 = Luchador("Carolina", 100, 6, 3, 5, "F", 7)


pelea = Pelea()
pelea.agregar_luchadores(luchador1, luchador2)


print("¡Comienza la pelea entre", luchador1.nombre, "y", luchador2.nombre, "!\n")
opciones = ["punio", "patada", "codazo", "rodillazo", "llave", "esquivar", "recuperar"]

while True:
    luchador_turno = pelea.luchadores[pelea.turno]
    print("\nTurno de:", luchador_turno.nombre)
    print("Opciones:", opciones)
    ataque = input("¿Qué movimiento quieres usar?: ").lower()

    exito = pelea.atacar(ataque)
    if exito:
        if pelea.verificar_ganador():
            break
        pelea.cambio_turno()
        pelea.mostrar_estado()
