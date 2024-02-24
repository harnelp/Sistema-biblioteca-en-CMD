class Libro:
    def __init__(self, titulo, autor, cantidad=1):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, titulo, autor, cantidad=1):
        if titulo in self.libros:
            self.libros[titulo].cantidad += cantidad
        else:
            self.libros[titulo] = Libro(titulo, autor, cantidad)
        print(f"Libro agregado: {titulo}, Autor: {autor}, Cantidad: {cantidad}")


    def mostrar_libros(self):
        for libro in self.libros.values():
            print(f"{libro.titulo} por {libro.autor} - Cantidad: {libro.cantidad}")

    def registrar_usuario(self, nombre):
        if nombre not in self.usuarios:
            self.usuarios[nombre] = Usuario(nombre)
            print(f"Usuario registrado: {nombre}")
        else:
            print(f"El usuario {nombre} ya está registrado.")

    def prestar_libro(self, titulo, nombre_usuario):
        if nombre_usuario not in self.usuarios:
            print(f"El usuario {nombre_usuario} no está registrado.")
            return
        if titulo not in self.libros or self.libros[titulo].cantidad < 1:
            print(f"El libro {titulo} no está disponible.")
            return
        self.libros[titulo].cantidad -= 1
        self.usuarios[nombre_usuario].libros_prestados.append(self.libros[titulo])
        print(f"Libro prestado: {titulo} a {nombre_usuario}")

    def devolver_libro(self, titulo, nombre_usuario):
        if nombre_usuario not in self.usuarios:
            print(f"El usuario {nombre_usuario} no está registrado.")
            return
        usuario = self.usuarios[nombre_usuario]
        libro_a_devolver = None
        for libro in usuario.libros_prestados:
            if libro.titulo == titulo:
                libro_a_devolver = libro
                break
        if libro_a_devolver:
            usuario.libros_prestados.remove(libro_a_devolver)
            self.libros[titulo].cantidad += 1
            print(f"Libro devuelto: {titulo} por {nombre_usuario}")
        else:
            print(f"El usuario {nombre_usuario} no tiene prestado el libro {titulo}.")

    def listar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return
        for nombre in self.usuarios:
            print(nombre)

    def listar_libros_usuario(self, nombre_usuario):
        if nombre_usuario not in self.usuarios:
            print(f"El usuario {nombre_usuario} no está registrado.")
            return
        usuario = self.usuarios[nombre_usuario]
        if usuario.libros_prestados:
            print(f"Libros prestados a {nombre_usuario}:")
            for libro in usuario.libros_prestados:
                print(f"- {libro.titulo} por {libro.autor}")
        else:
            print(f"El usuario {nombre_usuario} no tiene libros prestados.")
