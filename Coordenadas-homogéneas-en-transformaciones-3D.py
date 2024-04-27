import numpy as np


# Punto 3D en coordenadas cartesianas (x, y, z)
punto_cartesiano = np.array([1.0, 2.0, 3.0])


# Convertir el punto a coordenadas homogéneas (x, y, z, 1)
punto_homogeneo = np.append(punto_cartesiano, 1.0)


# Matriz de traslación 3D (trasladar 2 unidades en x, 3 unidades en y y 1 unidad en z)
matriz_traslacion = np.array([[1, 0, 0, 2],
                              [0, 1, 0, 3],
                              [0, 0, 1, 1],
                              [0, 0, 0, 1]])


# Aplicar la matriz de traslación al punto homogéneo
punto_homogeneo_traslacion = np.dot(matriz_traslacion, punto_homogeneo)


# Convertir el resultado de vuelta a coordenadas cartesianas
punto_cartesiano_resultado = punto_homogeneo_traslacion[:3]


print("Punto 3D en coordenadas cartesianas:", punto_cartesiano)
print("Punto 3D en coordenadas homogéneas:", punto_homogeneo)
print("Punto 3D después de la traslación:", punto_cartesiano_resultado)
