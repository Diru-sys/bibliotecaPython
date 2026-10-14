class Libro:
    def __init__(self, isbn, titulo, autor, año, genero, disponible):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.genero = genero
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"ISBN: {self.isbn} - Titulo: {self.titulo} - Autor: {self.autor} - Año: {self.año} - Género: {self.genero} - Disponible? -> {estado}"