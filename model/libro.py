class Libro:
    def __init__(self, isbn, titulo, autor, genero, año=None, disponible=True):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año = año
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"ISBN: {self.isbn} - Titulo: {self.titulo} - Autor: {self.autor} - Género: {self.genero} - Año: {self.año} - Disponible? -> {estado}"
