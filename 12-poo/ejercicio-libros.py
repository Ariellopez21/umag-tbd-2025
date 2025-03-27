class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool) -> None:
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def mostrar_info(self) -> str:
        return f"Libro(titulo={self.titulo}, autor={self.autor}, isbn={self.isbn}, disponible={self.disponible})"

    def prestar(self) -> None:
        self.disponible = False

    def devolver(self) -> None:
        self.disponible = True

class Usuario:
    def __init__(self, nombre: str, id: int, prestamos: list[str]) -> None:
        self.nombre = nombre
        self.id = id
        self.prestamos = prestamos

    def tomar_libro(self, libro: "Libro") -> None:
        if libro.disponible:
            libro.prestar()
            self.prestamos.append(libro.titulo)
        else:
            print(f"El libro {libro.titulo} no está disponible.")

    def devolver_libro(self, libro: "Libro") -> None:
        if libro.titulo in self.prestamos:
            libro.devolver()
            self.prestamos.remove(libro.titulo)
        else:
            print(f"No tienes el libro {libro.titulo} prestado.")

class Biblioteca:
    def __init__(self, nombre: str, libros: list[Libro], usuarios: list[Usuario]) -> None:
        self.nombre = nombre
        self.libros = libros
        self.usuarios = usuarios

print("QUIJOTE:")
quijote = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "978-3-16-148410-0", True)
print(quijote.mostrar_info())

print("USUARIO:")
ariel = Usuario("Ariel", 1, [quijote.titulo])
print("Prestamos:", ariel.prestamos)
ariel.devolver_libro(quijote)
print("Prestamos:", ariel.prestamos)

