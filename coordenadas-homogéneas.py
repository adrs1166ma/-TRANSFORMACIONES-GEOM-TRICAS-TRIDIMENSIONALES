import numpy as np


# Función para aplicar una transformación a un punto en coordenadas homogéneas
def apply_transform(matrix, point):
    if point.shape[0] == 3:
        transformed_point = np.dot(matrix, point)
        return transformed_point
    else:
        return None


# Definir una matriz de transformación (por ejemplo, una traslación)
translation_matrix = np.array([
    [1, 0, 2],  # Desplazamiento en el eje x
    [0, 1, 3],  # Desplazamiento en el eje y
    [0, 0, 1]   # Componente de escala
])


# Definir un punto en coordenadas homogéneas (x, y, w)
homogeneous_point = np.array([1, 1, 1])


# Aplicar la transformación al punto
transformed_point = apply_transform(translation_matrix, homogeneous_point)


# Imprimir el resultado
print("Punto original en coordenadas homogéneas:", homogeneous_point)
print("Punto transformado en coordenadas homogéneas:", transformed_point)
Punto original en coordenadas homogéneas: [1 1 1] 
Punto transformado en coordenadas homogéneas: [3 4 1]
