# Actividad 8.1
# Ejercicio 8.1: Operaciones con Multiplicaciones en Python

# ----------------------------------------------------
# Celda 1
# ----------------------------------------------------

# Asignar el mismo valor a múltiples variables
# en este caso, como demostración, usamos el valor 1
a = b = c = 2
print(a * b * c)

# Asignar a múltiples variables valores diferentes
x, y, z = 2, 5, 7
print("x=", x)
print("y=", y)
print("z=", z)
print("Multiplicados:", x*y*z)


# ----------------------------------------------------
# Celda 2
# ----------------------------------------------------

"""
Usted necesita calcular artículos en función de paquetes y cajas:
- Tiene 3 paquetes de lápices, cada paquete contiene 10 lápices.
- Tiene 2 cajas de cuadernos, cada caja contiene 5 cuadernos.
"""

# Asigne el número de paquetes y lápices por paquete
num_paquetes = 3
lapices_por_paquete = 10

# Asigne el número de cajas y cuadernos por caja
num_cajas = 2
cuadernos_por_caja = 5

# Calcule el total de lápices usando multiplicación: total de lapices es igual el numero de paquetes por la cantidad de lapices por paquete
total_lapices = num_paquetes * lapices_por_paquete

# Calcule el total de cuadernos usando la lógica de los lápices pero con los datos de los cuadernos
total_cuadernos = num_cajas * cuadernos_por_caja

# Imprima los resultados del total de lapices y el total de cuadernos:
print("total_lapices =", total_lapices)
print()
print("total_cuadernos =", total_cuadernos)
print()

# Calcule e imprima el producto de total_lapices mas el total_cuadernos en una línea:
print("producto =", total_lapices * total_cuadernos)

#Efren Rodriguez Granados 3/10/2026 MV34