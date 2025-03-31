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
    def __init__(self, nombre: str, id: int, prestamos: list["Libro"]) -> None:
        self.nombre = nombre
        self.id = id
        self.prestamos = prestamos

    def tomar_libro(self, libro: "Libro") -> None:
        if libro.disponible:
            libro.prestar()
            self.prestamos.append(libro)
        else:
            print(f"El libro {libro.titulo} no está disponible.")

    def devolver_libro(self, libro: "Libro") -> None:
        if libro.titulo in self.prestamos:
            libro.devolver()
            self.prestamos.remove(libro)
        else:
            print(f"No tienes el libro {libro.titulo} prestado.")

class Biblioteca:
    def __init__(self, nombre: str, libros: list["Libro"], usuarios: list["Usuario"]) -> None:
        self.nombre = nombre
        self.libros = libros
        self.usuarios = usuarios

    def agregar_libro(self, libro: "Libro") -> None:
        self.libros.append(libro)

    def registrar_usuario(self, usuario: "Usuario") -> None:
        self.usuarios.append(usuario)

    def mostrar_libros_disponibles(self) -> None:
        for libro in self.libros:
            if libro.disponible:
                print(libro.mostrar_info())
            else:
                print(libro.titulo, " -> no disponible")

    def mostrar_usuarios(self) -> None:
        if self.usuarios:
            for usuario in self.usuarios:
                print(usuario.nombre)

    def buscar_libro_por_titulo(self, titulo : str) -> bool:
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                return True
        print(titulo, " -> no disponible")
        return False

quijote = Libro("Don Quijote de la Mancha", "Mike de Cervantes", "123-4", True)
pythonLearning = Libro(titulo="Learning Python3, 6ta edición", autor="Diego Alvarez S.", isbn="002231-3", disponible=True)
ariel = Usuario("Ariel", 1, [])
mike = Usuario(nombre="Mike L. Loaiza", id=2, prestamos=[])
biblioteca_umag = Biblioteca("Biblioteca de la Umag", [quijote], [ariel])

print("Biblioteca UMAG, libros disponibles:")
biblioteca_umag.mostrar_libros_disponibles()

print("Biblioteca UMAG, usuarios:")
biblioteca_umag.mostrar_usuarios()

biblioteca_umag.agregar_libro(pythonLearning)
biblioteca_umag.registrar_usuario(mike)

print()
print("BUSCAR LIBRO", quijote.titulo ,":")
print(biblioteca_umag.buscar_libro_por_titulo(quijote.titulo))

print()

print("REFRESH: Biblioteca UMAG, libros disponibles:")
biblioteca_umag.mostrar_libros_disponibles()

print("REFRESH: Biblioteca UMAG, usuarios:")
biblioteca_umag.mostrar_usuarios()

ariel.tomar_libro(quijote)
mike.tomar_libro(pythonLearning)

print()

print("REFRESH 2: Biblioteca UMAG, libros disponibles:")
biblioteca_umag.mostrar_libros_disponibles()

print()

print("BUSCAR LIBRO 2 ", pythonLearning.titulo ,":")
print(biblioteca_umag.buscar_libro_por_titulo(pythonLearning.titulo))