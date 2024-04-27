# Definir coordenadas cartesianas
x = 3.0
y = 4.0


# Calcular la distancia desde el origen (0, 0)
distancia_origen = (x**2 + y**2)**0.5


# Imprimir las coordenadas y la distancia desde el origen
print(f"Coordenadas: ({x}, {y})")
print(f"Distancia desde el origen: {distancia_origen}")


# Realizar algunas operaciones geométricas
# Por ejemplo, calcular el ángulo respecto al eje x en radianes
import math
angulo_rad = math.atan2(y, x)


# Convertir el ángulo a grados
angulo_grados = math.degrees(angulo_rad)
print(f"Ángulo respecto al eje x (radianes): {angulo_rad}")
print(f"Ángulo respecto al eje x (grados): {angulo_grados}")
