"""Calcula el precio final de una compra aplicando un descuento según su importe.

Módulo 0485 Programación · UD 2
Autor: Jose María Mas Chicharro y Andrea Mira Hernández
Fecha: 15/10/2026
"""

DESCUENTO_NORMAL = 0.10
DESCUENTO_ALTO = 0.15
LIMITE_NORMAL = 100.0
LIMITE_ALTO = 300.0


def main():
    """Solicita el importe de una compra y calcula el descuento correspondiente."""

    # Entrada
    importe = float(input("Introduce el importe de la compra (€): "))

    # Proceso
    if importe >= LIMITE_ALTO:
        descuento = DESCUENTO_ALTO
    elif importe >= LIMITE_NORMAL:
        descuento = DESCUENTO_NORMAL
    else:
        descuento = 0.0

    ahorro = importe * descuento
    precio_final = importe - ahorro

    # Salida
    print(f"\nImporte inicial: {importe:.2f} €")
    print(f"Descuento aplicado: {descuento * 100:.0f} %")
    print(f"Ahorro: {ahorro:.2f} €")
    print(f"Precio final: {precio_final:.2f} €")


if __name__ == "__main__":
    main()