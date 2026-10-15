from datetime import date

class Prestamo:
    def __init__(self, usuario, libro, fechaPrestamo=None, fechaDevolucion=None):
        self.usuario = usuario
        self.libro = libro
        self.fechaPrestamo = (fechaPrestamo if fechaPrestamo is not None else date.today())
        self.fechaDevolucion = fechaDevolucion


    @property
    def activo(self):
        if self.fechaDevolucion is None:
            return
        else:
            return False

    def __eq__(self, __value: object) -> bool:
        return self.usuario == __value.usuario and self.libro == __value.libro

    def __str__(self):
        estado = "Activo" if self.activo else f"Devuelto en la fecha: {self.fechaDevolucion}"
        return f"Usuario del prestamo: {self.usuario} - Libro a prestar: {self.libro} - Fecha del prestamo: {self.fechaPrestamo} - Fecha de la devolución: {self.fechaDevolucion}"