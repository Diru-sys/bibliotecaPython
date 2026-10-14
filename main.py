from model.libro import Libro
from model.prestamo import Prestamo
from model.usuario import Usuario

def main():
    libro1 = Libro(978, 'Aprende D&D', 'Carlos', 'Fantasía')
    print(libro1)

    usuario1 = Usuario(1, 'Carlos', 'Sánchez Damas', 'dirusetterelos@gmail.com')
    print(usuario1)

    prestamo1 = Prestamo(1, 978)
    print(prestamo1)


if __name__ == "__main__":
    main()