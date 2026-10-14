#ISBN
#titulo
#autor
#año
#genero
#disponible
class Libro:
    def __init__(self, isbn, titulo, autor, año, genero, disponible):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.genero = genero
        self.disponible = disponible