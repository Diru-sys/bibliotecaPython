from model.libro import Libro
from model.prestamo import Prestamo
from model.usuario import Usuario
from services.biblioteca import Biblioteca

biblioteca = Biblioteca()

def registrarLibro(biblioteca):
    isbn = input("ISBN: ").strip()
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    año = input("Año: ").strip()
    genero = input("Género: ").strip()

    libro = Libro(isbn,titulo,autor,año,genero)
    biblioteca.registrarLibro(libro)
    print(f"Libro registrado correctamente.")


def registrarUsuario(biblioteca):
    id = input("ID: ").strip()
    nombre = input("Nombre: ").strip()
    apellidos = input("Apellidos: ").strip()
    email = input("Email: ").strip()

    usuario = Usuario(id,nombre,apellidos,email)
    biblioteca.registrarUsuario(usuario)
    print(f"Usuario registrado correctamente.")


def buscarLibro(biblioteca):
    tituloBuscado = input("Introduce el titulo del libro: ").strip()
    for libro in biblioteca.libros:
        if tituloBuscado.lower() == libro.titulo.lower():
            print(f"Libro encontrado: ")
            return print(libro)
    return f"No existe un libro con este titulo."


def mostrarLibros(biblioteca):
    print(f" --LISTADO DE LIBROS-- ")
    for libro in biblioteca.libros:
        print(libro)


def realizarPrestamo(biblioteca):
    idUsuario = input("ID del Usuario: ").strip()
    isbnLibro = input("ID del Usuario: ").strip()

    prestamo = Prestamo(idUsuario, isbnLibro)
    biblioteca.realizarPrestamo(prestamo)


def devolverLibro(biblioteca):
    prestamo = buscarPrestamoActivo(idUsuario, isbn)
    if prestamo is None:
        return False
    prestamo.devolver()
    libro = buscarLibroPorIsbn(isbn)
    if libro is not None:
        libro.disponible = True
    return True


def mostrarMenu():
    print("===========================")
    print("   GESTIÓN DE BIBLIOTECA   ")
    print("===========================")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Buscar libro")
    print("4. Listar libros")
    print("5. Realizar préstamo")
    print("6. Devolver libro")
    print("7. Mostrar préstamos activos")
    print("8. Mostrar préstamos de un usuario")
    print("9. Guardar datos")
    print("0. Salir\n")


def main():
    while True:
        mostrarMenu()
        opc = int(input("Opción: "))
        match opc:
            case 1:
                registrarLibro(biblioteca)
            case 2:
                registrarUsuario(biblioteca)
            case 3:
                buscarLibro(biblioteca)
            case 4:
                mostrarLibros(biblioteca)
            case 5:
                realizarPrestamo(biblioteca)
            case 6:
                devolverLibro(biblioteca)
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 0:
                exit
            case _:
                print(f"Opción introducida invalida.")


if __name__ == "__main__":
    main()