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


    def registrarUsuario(self, usuario):
        if self.buscarUsuario(usuario):
            print(f"Este usuario ya está en la lista.")
            return
        self.usuarios.append(usuario)


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