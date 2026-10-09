"""Ejercicio 2.2 (con ejercicios propuestos) - clase Planeta."""
from enum import Enum


# Tipo enumerado: solo permite estos tres valores
class TipoPlaneta(Enum):
    GASEOSO = 1
    TERRESTRE = 2
    ENANO = 3


class Planeta:
    def __init__(self, nombre: str, cantidad_satelites: int, masa: float, volumen: float,
                 diametro: int, distancia_sol: int, tipo: TipoPlaneta, observable: bool,
                 periodo_orbital: float, periodo_rotacion: float):
        self._nombre = nombre                           # Nombre del planeta
        self._cantidad_satelites = cantidad_satelites   # Cantidad de satelites
        self._masa = masa                               # Masa en kg
        self._volumen = volumen                         # Volumen en km3
        self._diametro = diametro                       # Diametro en km
        self._distancia_sol = distancia_sol             # Distancia al Sol en millones de km
        self._tipo = tipo                               # GASEOSO, TERRESTRE o ENANO
        self._observable = observable                   # Observable a simple vista
        self._periodo_orbital = periodo_orbital         # NUEVO: periodo orbital en años
        self._periodo_rotacion = periodo_rotacion       # NUEVO: periodo de rotacion en dias

    # Imprime todos los atributos del planeta (incluye los nuevos)
    def imprimir(self) -> None:
        print(f"Nombre = {self._nombre}")
        print(f"Cantidad de satelites = {self._cantidad_satelites}")
        print(f"Masa (kg) = {self._masa}")
        print(f"Volumen (km3) = {self._volumen}")
        print(f"Diametro (km) = {self._diametro}")
        print(f"Distancia al Sol (millones de km) = {self._distancia_sol}")
        print(f"Tipo de planeta = {self._tipo.name}")
        print(f"Observable a simple vista = {self._observable}")
        print(f"Periodo orbital (años) = {self._periodo_orbital}")
        print(f"Periodo de rotacion (dias) = {self._periodo_rotacion}")

    # Densidad = masa / volumen
    def calcular_densidad(self) -> float:
        return self._masa / self._volumen

    # Es exterior si esta mas alla del cinturon de asteroides (3.4 UA).
    # 1 UA = 149.597870 millones de km
    def es_planeta_exterior(self) -> bool:
        limite = 3.4 * 149.597870
        return self._distancia_sol > limite


if __name__ == "__main__":
    tierra = Planeta("Tierra", 1, 5.9736e24, 1.08321e12, 12742, 150,
                     TipoPlaneta.TERRESTRE, True, 1.0, 1.0)
    jupiter = Planeta("Jupiter", 79, 1.899e27, 1.4313e15, 139820, 778,
                      TipoPlaneta.GASEOSO, True, 11.86, 0.41)

    tierra.imprimir()
    print("Densidad =", tierra.calcular_densidad())
    print("Es planeta exterior =", tierra.es_planeta_exterior())
    print()
    jupiter.imprimir()
    print("Densidad =", jupiter.calcular_densidad())
    print("Es planeta exterior =", jupiter.es_planeta_exterior())
