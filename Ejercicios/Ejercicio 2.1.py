class Persona:
    # Constructor: ahora también inicializa el país de nacimiento y el género
    def __init__(self, nombre: str, apellido: str, numero_documento: int,
                 año_nacimiento: int, pais_nacimiento: str, genero: str):
        self._nombre = nombre                        # Nombre de la persona
        self._apellido = apellido                    # Apellido de la persona
        self._numero_documento = numero_documento    # Documento de identidad
        self._año_nacimiento = año_nacimiento        # Año de nacimiento
        self._pais_nacimiento = pais_nacimiento      # país de nacimiento 
        self._genero = genero                        # Ngénero, un solo carácter: 'H' o 'M'

    # Imprime en pantalla los valores de los atributos (incluye los nuevos)
    def imprimir(self) -> None:
        print("Nombre =", self._nombre)
        print("Apellido =", self._apellido)
        print("Número de documento =", self._numero_documento)
        print("Año de nacimiento =", self._año_nacimiento)
        print("País de nacimiento =", self._pais_nacimiento)
        print("Género =", self._genero)
        print()


# Programa principal 
if __name__ == "__main__":
    p1 = Persona("Pedro", "Pérez", 1053121010, 1998, "Colombia", "H")
    p2 = Persona("Luisa", "León", 1053223344, 2001, "Colombia", "M")
    p1.imprimir()
    p2.imprimir()