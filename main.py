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
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
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