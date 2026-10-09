from enum import Enum


class TipoCuenta(Enum):
    AHORROS = 1
    CORRIENTE = 2


class CuentaBancaria:
    # No recibe el saldo: toda cuenta nueva empieza en cero
    def __init__(self, nombres_titular: str, apellidos_titular: str,
                 numero_cuenta: int, tipo_cuenta: TipoCuenta,
                 porcentaje_interes_mensual: float):
        self._nombres_titular = nombres_titular
        self._apellidos_titular = apellidos_titular
        self._numero_cuenta = numero_cuenta
        self._tipo_cuenta = tipo_cuenta
        self._saldo = 0.0                                          # Saldo inicial en cero
        self._porcentaje_interes_mensual = porcentaje_interes_mensual  # Interes mensual en %

    # Imprime todos los datos de la cuenta
    def imprimir(self) -> None:
        print("Nombres del titular =", self._nombres_titular)
        print("Apellidos del titular =", self._apellidos_titular)
        print("Numero de cuenta =", self._numero_cuenta)
        print("Tipo de cuenta =", self._tipo_cuenta.name)
        print("Saldo = $", self._saldo)
        print("Porcentaje de interes mensual =", self._porcentaje_interes_mensual, "%")
        print()

    # Muestra el saldo actual
    def consultar_saldo(self) -> None:
        print("El saldo actual es = $", self._saldo)

    # Suma un valor al saldo. Devuelve True si fue valido
    def consignar(self, valor: float) -> bool:
        if valor > 0:
            self._saldo += valor
            print(f"Se consigno ${valor}. Nuevo saldo = ${self._saldo}")
            return True
        print("El valor a consignar debe ser mayor que cero.")
        return False

    # Resta un valor al saldo. No permite retirar mas de lo que hay
    def retirar(self, valor: float) -> bool:
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Se retiro ${valor}. Nuevo saldo = ${self._saldo}")
            return True
        print("Retiro no permitido: el valor debe ser mayor que cero y no superar el saldo.")
        return False

    # Calcula el nuevo saldo aplicando el interes mensual:
    # nuevo saldo = saldo + (saldo * porcentaje / 100)
    def calcular_saldo_con_interes(self) -> float:
        interes = self._saldo * self._porcentaje_interes_mensual / 100
        self._saldo += interes
        print(f"Se aplico un interes de ${interes}. Nuevo saldo = ${self._saldo}")
        return self._saldo


if __name__ == "__main__":
    cuenta = CuentaBancaria("Pedro", "Perez", 123456789, TipoCuenta.AHORROS, 2.0)
    cuenta.imprimir()
    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)                           # Valido: queda 100000
    cuenta.retirar(500000)                           # Invalido: supera el saldo
    cuenta.consultar_saldo()
    cuenta.calcular_saldo_con_interes()              # Aplica el 2% mensual
    cuenta.consultar_saldo()