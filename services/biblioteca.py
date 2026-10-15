#funciones, lógica
from model.libro import Libro

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []


    def registrarLibro(self, libro):
        if self.buscarLibro(libro):
            print(f"Este libro ya está en la lista.")
            return
        self.libros.append(libro)


    def registrarUsuario(self, usuario):
        if self.buscarUsuario(usuario):
            print(f"Este usuario ya está en la lista.")
            return
        self.usuarios.append(usuario)


    def realizarPrestamo(self, prestamo):
        if self.buscarPrestamoActivo(prestamo.usuario, prestamo.libro):
            print(f"El prestamo ya está realizado.")
            return
        self.prestamos.append(prestamo)
        libro = self.buscarLibro(Libro(prestamo.libro, "", "", ""))
        if libro is not None:
            libro.disponible = False


    def buscarUsuario(self, usuarioNuevo):
        for usuario in self.usuarios:
            if usuario.__eq__(usuarioNuevo):
                return usuario
        return None


    def buscarLibro(self, libroNuevo):
        for libro in self.libros:
            if libro.__eq__(libroNuevo):
                return libro
        return None


    def buscarPrestamoActivo(self, idUsuario, isbn):
        for prestamo in self.prestamos:
            if prestamo.usuario == idUsuario and prestamo.libro == isbn and prestamo.activo:
                return prestamo
        return None