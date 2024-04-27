import numpy as np


# Coordenadas cartesianas (x, y)
x_cartesiano = 3.0
y_cartesiano = 4.0


# Coordenadas homogéneas (x, y, 1)
coordenadas_homogeneas = np.array([x_cartesiano, y_cartesiano, 1.0])


# Matriz de transformación de traslación
# Supongamos que queremos trasladar el punto 2 unidades hacia la derecha y 3 unidades hacia arriba
traslacion_matrix = np.array([[1.0, 0.0, 2.0],
                              [0.0, 1.0, 3.0],
                              [0.0, 0.0, 1.0]])


# Aplicar la traslación a las coordenadas homogéneas
coordenadas_homogeneas_traslacion = np.dot(traslacion_matrix, coordenadas_homogeneas)


# Obtener las coordenadas cartesianas resultantes
x_resultante = coordenadas_homogeneas_traslacion[0]
y_resultante = coordenadas_homogeneas_traslacion[1]


print(f"Coordenadas cartesianas originales: ({x_cartesiano}, {y_cartesiano})")
print(f"Coordenadas homogéneas originales: {coordenadas_homogeneas}")
print(f"Coordenadas homogéneas después de la traslación: {coordenadas_homogeneas_traslacion}")
print(f"Coordenadas cartesianas resultantes: ({x_resultante}, {y_resultante})")
