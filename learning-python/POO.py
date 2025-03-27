from math import sqrt
from dataclasses import dataclass
# from typing import Optional
numeric = int | float
class Animal:
    def __init__(self, especie: str, edad: int, color: str = "Negro"):
        self.especie = especie
        self.edad = edad
        self.color = color

    def __repr__(self):
        return f"Animal({self.especie}, {self.edad}, {self.color})"

    def speak(self):
        print(f"Soy un {self.especie}, tengo {self.edad} años y soy {self.color} ")

    def __add__(self, other):
        print(f"Estas tratando de sumar {self} y {other}")


class AnimalEntrenado(Animal):
    def __init__(self, nivel_entrenamiento, especie, edad, color):
        super().__init__(especie, edad, color)
        self.nivel_entrenamiento = nivel_entrenamiento

    def hacer_truco(self):
        match self.nivel_entrenamiento:
            case 1:
                print("Dar la pata")
            case 2:
                print("Hacerse el muerto")
            case 3:
                print("Ir a comprar pan")
            case _:
                print("No tengo trucos")


class Mascota(Animal):
    def __init__(self, nombre, especie, edad, color):
        super().__init__(especie, edad, color)
        self.nombre = nombre

    def __repr__(self):
        return f"Mascota({self.nombre},{self.especie}, {self.edad}, {self.color})"

    def presentar(self):
        print(f"Hola, soy {self.nombre}")
        return


class MascotaEntrenada(Mascota, AnimalEntrenado):
    def __init__(self, nombre, nivel_entrenamiento, especie, edad, color):
        Mascota.__init__(self, nombre, especie, edad, color)
        AnimalEntrenado.__init__(self, nivel_entrenamiento, especie, edad, color)

    def __repr__(self):
        return f"MascotaEntrenada({self.nombre}, {self.nivel_entrenamiento}, {self.especie}, {self.edad}, {self.color})"

class Coordenada:
    def __init__(self, x: numeric, y: numeric):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Coordenada({self.x}, {self.y})"

    def __add__(self, other: "Coordenada") -> "Coordenada":
        return Coordenada(self.x + other.x, self.y + other.y)

    def __eq__(self, other: "Coordenada") -> bool: # type: ignore
        return self.x == other.x and self.y == other.y

    def distancia_entre_dos_puntos(self, other: "Coordenada"):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

c1 = Coordenada(1, 2)
c2 = Coordenada(3, 4)

print(c1 + c2)  # Coordenada(4, 6)
print(Coordenada.distancia_entre_dos_puntos(c1, c2))  # 2.8284271247461903
print(c1.distancia_entre_dos_puntos(c2))  # 2.8284271247461903


def sumar_numeros(numeros: list[int | float]) -> float:
    return sum(numeros)

print(sumar_numeros([1, 2.3, 3, 4, 5]))  # 15

def contar_ocurrencias(palabras: list[str]) -> dict[str, int]:
    resultado = {}
    for palabra in palabras:
        resultado[palabra] = resultado.get(palabra, 0) + 1
    return resultado

print(contar_ocurrencias(["A", "B", "C", "D"]))

def buscar_elemento(lista: list[int], elemento: int) -> int | None:
    if elemento in lista:
        return lista.index(elemento)
    return None

print(buscar_elemento([1, 2, 3, 4, 5], 3)) 

@dataclass(eq=True, order=True, frozen=False)
class Punto:
    x: numeric
    y: numeric
    z: numeric = 0

    def __post_init__(self):
        self.z = self.x + self.y

    def distancia_entre_dos_puntos(self, other: "Punto") -> numeric:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def z_value(self) -> numeric:
        return self.z

p1 = Punto(1, 2)
p2 = Punto(3, 4)
print(p1) 
print(p1 == p2)  # False
print(p1.distancia_entre_dos_puntos(p2))  # 2.8284271247461903
print(sorted([p2, p1])) 
#p1.x = 3  # Error por Frozen = True

print(p1.z_value())  # 3