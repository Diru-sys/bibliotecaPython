#funciones, lógica
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


    def buscarLibro(self, libroNuevo):
        for libro in self.libros:
            if libro.__eq__(libroNuevo):
                return libro
        return None