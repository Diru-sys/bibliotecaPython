from datetime import date

class Prestamo:
    def __init__(self, idUsuario, isbnLibro, fechaPrestamo=None, fechaDevolucion=None):
        self.idUsuario = idUsuario
        self.isbnLibro = isbnLibro
        self.fechaPrestamo = (fechaPrestamo if fechaPrestamo is not None else date.today())
        self.fechaDevolucion = fechaDevolucion


    @property
    def activo(self):
        if self.fechaDevolucion is None:
            return
        else:
            return False


    def __str__(self):
        estado = "Activo" if self.activo else f"Devuelto en la fecha: {self.fechaDevolucion}"
        return f"ID del usuario del préstamo: {self.idUsuario} - ISBN del libro a prestar: {self.isbnLibro} - Fecha del prestamo: {self.fechaPrestamo} - Fecha de la devolución: {self.fechaDevolucion}"