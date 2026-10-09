import math


class Circulo:
    def __init__(self, radio: float):
        self._radio = radio                          # Radio en cm

    def calcular_area(self) -> float:
        return math.pi * self._radio ** 2            # pi * r^2

    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self._radio             # 2 * pi * r


class Rectangulo:
    def __init__(self, base: float, altura: float):
        self._base = base                            # Base en cm
        self._altura = altura                        # Altura en cm

    def calcular_area(self) -> float:
        return self._base * self._altura

    def calcular_perimetro(self) -> float:
        return 2 * self._base + 2 * self._altura


class Cuadrado:
    def __init__(self, lado: float):
        self._lado = lado                            # Lado en cm

    def calcular_area(self) -> float:
        return self._lado * self._lado

    def calcular_perimetro(self) -> float:
        return 4 * self._lado


class TrianguloRectangulo:
    def __init__(self, base: float, altura: float):
        self._base = base                            # Base en cm
        self._altura = altura                        # Altura en cm

    def calcular_area(self) -> float:
        return (self._base * self._altura) / 2

    # Teorema de Pitagoras
    def calcular_hipotenusa(self) -> float:
        return math.sqrt(self._base ** 2 + self._altura ** 2)

    def calcular_perimetro(self) -> float:
        return self._base + self._altura + self.calcular_hipotenusa()

    # Imprime en pantalla si es equilatero, isosceles o escaleno
    def determinar_tipo_triangulo(self) -> None:
        hipotenusa = self.calcular_hipotenusa()
        if self._base == self._altura == hipotenusa:
            print("El triangulo es Equilatero")        # 3 lados iguales
        elif self._base != self._altura and self._base != hipotenusa and self._altura != hipotenusa:
            print("El triangulo es Escaleno")          # 3 lados diferentes
        else:
            print("El triangulo es Isosceles")         # 2 lados iguales


class Rombo:
    def __init__(self, diagonal_mayor: float, diagonal_menor: float):
        self._diagonal_mayor = diagonal_mayor        # Diagonal mayor en cm
        self._diagonal_menor = diagonal_menor        # Diagonal menor en cm

    # Area = (diagonal mayor * diagonal menor) / 2
    def calcular_area(self) -> float:
        return (self._diagonal_mayor * self._diagonal_menor) / 2

    # Las diagonales se cruzan en angulo recto y forman triangulos rectangulos,
    # entonces el lado = raiz((D/2)^2 + (d/2)^2)
    def calcular_lado(self) -> float:
        return math.sqrt((self._diagonal_mayor / 2) ** 2 + (self._diagonal_menor / 2) ** 2)

    # Perimetro = 4 * lado
    def calcular_perimetro(self) -> float:
        return 4 * self.calcular_lado()


class Trapecio:
    def __init__(self, base_mayor: float, base_menor: float, altura: float,
                 lado_izquierdo: float, lado_derecho: float):
        self._base_mayor = base_mayor                # Base mayor en cm
        self._base_menor = base_menor                # Base menor en cm
        self._altura = altura                        # Altura en cm
        self._lado_izquierdo = lado_izquierdo        # Lado no paralelo izquierdo en cm
        self._lado_derecho = lado_derecho            # Lado no paralelo derecho en cm

    # Area = ((base mayor + base menor) * altura) / 2
    def calcular_area(self) -> float:
        return ((self._base_mayor + self._base_menor) * self._altura) / 2

    # Perimetro = suma de los cuatro lados
    def calcular_perimetro(self) -> float:
        return self._base_mayor + self._base_menor + self._lado_izquierdo + self._lado_derecho


# Clase de prueba: solo tiene el main
class PruebaFiguras:
    @staticmethod
    def main() -> None:
        circulo = Circulo(2)
        rectangulo = Rectangulo(1, 2)
        cuadrado = Cuadrado(3)
        triangulo = TrianguloRectangulo(3, 5)
        rombo = Rombo(8, 6)
        trapecio = Trapecio(10, 6, 4, 5, 5)

        print("Area del circulo =", circulo.calcular_area())
        print("Perimetro del circulo =", circulo.calcular_perimetro())
        print()
        print("Area del rectangulo =", rectangulo.calcular_area())
        print("Perimetro del rectangulo =", rectangulo.calcular_perimetro())
        print()
        print("Area del cuadrado =", cuadrado.calcular_area())
        print("Perimetro del cuadrado =", cuadrado.calcular_perimetro())
        print()
        print("Area del triangulo =", triangulo.calcular_area())
        print("Perimetro del triangulo =", triangulo.calcular_perimetro())
        triangulo.determinar_tipo_triangulo()
        print()
        print("Area del rombo =", rombo.calcular_area())
        print("Perimetro del rombo =", rombo.calcular_perimetro())
        print()
        print("Area del trapecio =", trapecio.calcular_area())
        print("Perimetro del trapecio =", trapecio.calcular_perimetro())


if __name__ == "__main__":
    PruebaFiguras.main()