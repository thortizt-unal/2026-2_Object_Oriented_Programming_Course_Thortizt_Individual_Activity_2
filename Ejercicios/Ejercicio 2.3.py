from enum import Enum


# ----- Enumerados -----
class Combustible(Enum):
    GASOLINA = 1
    BIOETANOL = 2
    DIESEL = 3
    BIODIESEL = 4
    GAS_NATURAL = 5


class TipoAutomovil(Enum):
    CARRO_CIUDAD = 1
    SUBCOMPACTO = 2
    COMPACTO = 3
    FAMILIAR = 4
    EJECUTIVO = 5
    SUV = 6


class Color(Enum):
    BLANCO = 1
    NEGRO = 2
    ROJO = 3
    NARANJA = 4
    AMARILLO = 5
    VERDE = 6
    AZUL = 7
    VIOLETA = 8


class Automovil:
    VALOR_BASE_MULTA = 100000                        # Valor de la primera multa (pesos)

    def __init__(self, marca: str, modelo: int, motor: float, tipo_combustible: Combustible,
                 tipo_automovil: TipoAutomovil, numero_puertas: int, cantidad_asientos: int,
                 velocidad_maxima: int, color: Color, es_automatico: bool):
        self._marca = marca                          # Fabricante
        self._modelo = modelo                        # Año de fabricación
        self._motor = motor                          # Cilindraje en litros
        self._tipo_combustible = tipo_combustible
        self._tipo_automovil = tipo_automovil
        self._numero_puertas = numero_puertas
        self._cantidad_asientos = cantidad_asientos
        self._velocidad_maxima = velocidad_maxima    # km/h
        self._color = color
        self._velocidad_actual = 0                   # km/h, empieza en cero
        self._es_automatico = es_automatico          # True si es automático
        self._numero_multas = 0                      # cantidad de multas
        self._total_multas = 0.0                     # valor acumulado de multas

    # ----- Métodos get -----
    def get_marca(self) -> str: return self._marca
    def get_modelo(self) -> int: return self._modelo
    def get_motor(self) -> float: return self._motor
    def get_tipo_combustible(self) -> Combustible: return self._tipo_combustible
    def get_tipo_automovil(self) -> TipoAutomovil: return self._tipo_automovil
    def get_numero_puertas(self) -> int: return self._numero_puertas
    def get_cantidad_asientos(self) -> int: return self._cantidad_asientos
    def get_velocidad_maxima(self) -> int: return self._velocidad_maxima
    def get_color(self) -> Color: return self._color
    def get_velocidad_actual(self) -> int: return self._velocidad_actual
    def get_es_automatico(self) -> bool: return self._es_automatico          

    # ----- Métodos set -----
    def set_marca(self, marca: str) -> None: self._marca = marca
    def set_modelo(self, modelo: int) -> None: self._modelo = modelo
    def set_motor(self, motor: float) -> None: self._motor = motor
    def set_tipo_combustible(self, tipo_combustible: Combustible) -> None: self._tipo_combustible = tipo_combustible
    def set_tipo_automovil(self, tipo_automovil: TipoAutomovil) -> None: self._tipo_automovil = tipo_automovil
    def set_numero_puertas(self, numero_puertas: int) -> None: self._numero_puertas = numero_puertas
    def set_cantidad_asientos(self, cantidad_asientos: int) -> None: self._cantidad_asientos = cantidad_asientos
    def set_velocidad_maxima(self, velocidad_maxima: int) -> None: self._velocidad_maxima = velocidad_maxima
    def set_color(self, color: Color) -> None: self._color = color
    def set_velocidad_actual(self, velocidad_actual: int) -> None: self._velocidad_actual = velocidad_actual
    def set_es_automatico(self, es_automatico: bool) -> None: self._es_automatico = es_automatico  # NUEVO

    # ----- Otros métodos -----
    # Aumenta la velocidad. Si se pasa de la máxima, no acelera y genera una multa
    def acelerar(self, incremento: int) -> None:
        if self._velocidad_actual + incremento <= self._velocidad_maxima:
            self._velocidad_actual += incremento
        else:
            print("No se puede superar la velocidad maxima del automovil.")
            # La multa aumenta cada vez: 100000, 200000, 300000...
            self._numero_multas += 1
            valor_multa = self.VALOR_BASE_MULTA * self._numero_multas
            self._total_multas += valor_multa
            print(f"Se genero una multa de ${valor_multa}.")

    # Disminuye la velocidad sin llegar a un valor negativo
    def desacelerar(self, decremento: int) -> None:
        if self._velocidad_actual - decremento >= 0:
            self._velocidad_actual -= decremento
        else:
            print("No se puede decrementar a una velocidad negativa.")

    # Pone la velocidad actual en cero
    def frenar(self) -> None:
        self._velocidad_actual = 0

    # Tiempo en horas = distancia / velocidad actual
    def calcular_tiempo_llegada(self, distancia: float) -> float:
        if self._velocidad_actual == 0:              # Evita dividir entre cero
            print("El automovil esta detenido, no se puede calcular el tiempo.")
            return 0
        return distancia / self._velocidad_actual

    #indica si el vehículo tiene multas
    def tiene_multas(self) -> bool:
        return self._numero_multas > 0

    # devuelve el valor total de las multas
    def calcular_total_multas(self) -> float:
        return self._total_multas

    # Imprime los atributos
    def imprimir(self) -> None:
        print("Marca =", self._marca)
        print("Modelo =", self._modelo)
        print("Motor =", self._motor)
        print("Tipo de Combustible =", self._tipo_combustible.name)
        print("Tipo de automovil =", self._tipo_automovil.name)
        print("Numero de puertas =", self._numero_puertas)
        print("Cantidad de asientos =", self._cantidad_asientos)
        print("Velocidad maxima =", self._velocidad_maxima, "km/h")
        print("Color =", self._color.name)
        print("Velocidad actual =", self._velocidad_actual, "km/h")
        print("Es automatico =", self._es_automatico)


if __name__ == "__main__":
    auto = Automovil("Ford", 2018, 3.0, Combustible.DIESEL, TipoAutomovil.EJECUTIVO,
                     5, 6, 250, Color.NEGRO, True)
    auto.imprimir()
    print()

    auto.set_velocidad_actual(100)
    print("Velocidad actual =", auto.get_velocidad_actual())
    auto.acelerar(20)
    print("Velocidad actual =", auto.get_velocidad_actual())
    auto.desacelerar(50)
    print("Velocidad actual =", auto.get_velocidad_actual())
    auto.frenar()
    print("Velocidad actual =", auto.get_velocidad_actual())

    # Prueba de las multas (ejercicios propuestos)
    auto.acelerar(300)                               # Supera la máxima: se genera la multa
    print("Tiene multas =", auto.tiene_multas())
    print("Total de multas = $", auto.calcular_total_multas())