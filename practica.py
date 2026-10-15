"""Calcula el importe final de un pedido con descuento, IVA y gastos de envío.

Módulo 0485 Programación · UD 2
Autor: Jose María Mas Chicharro y Andrea Mira Hernández
Fecha: 15/10/2026
"""

IVA_GENERAL = 0.21
ENVIO = 4.95
UMBRAL_ENVIO_GRATIS = 50.0


def main():
    """Solicita los datos del pedido y muestra su presupuesto final."""

    # Entradas
    articulo = input("Artículo: ")
    precio = float(input("Precio unitario sin IVA (€): "))
    unidades = int(input("Unidades: "))
    descuento = float(input("Descuento (%): "))

    # Proceso
    base = precio * unidades
    ahorro = base * descuento / 100
    base_descuento = base - ahorro
    iva = base_descuento * IVA_GENERAL

    envio = 0.0 if base_descuento >= UMBRAL_ENVIO_GRATIS else ENVIO

    total = base_descuento + iva + envio

    # Salidas
    print(f"\nPresupuesto de {unidades} x {articulo}")
    print(f" Base imponible:     {base:8.2f} €")
    print(f" Descuento:          {ahorro:8.2f} €")
    print(f" Base con descuento: {base_descuento:8.2f} €")
    print(f" IVA (21 %):         {iva:8.2f} €")
    print(f" Envío:              {envio:8.2f} €")
    print(f" TOTAL:              {total:8.2f} €")


if __name__ == "__main__":
    main()