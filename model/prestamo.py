class Prestamo:
    def __init__(self, idUsuario, isbnLibro, fechaPrestamo, fechaDevolucion):
        self.idUsuario = idUsuario
        self.isbnLibro = isbnLibro
        self.fechaPrestamo = fechaPrestamo
        self.fechaDevolucion = fechaDevolucion

    def __str__(self):
        return f"ID del usuario del préstamo: {self.idUsuario} - ISBN del libro a prestar: {self.isbnLibro} - Fecha del prestamo: {self.fechaPrestamo} - Fecha máxima devolución: {self.fechaDevolucion}"