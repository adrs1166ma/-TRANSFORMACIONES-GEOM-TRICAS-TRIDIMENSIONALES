import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Crear puntos 3D
x = np.array([1, 0, 0])
y = np.array([0, 1, 0])
z = np.array([0, 0, 1])


# Crear una matriz de rotación 3D (rotación en torno al eje Z)
angulo_grados = 45
angulo_radianes = np.radians(angulo_grados)
rotacion_matrix = np.array([[np.cos(angulo_radianes), -np.sin(angulo_radianes), 0],
                            [np.sin(angulo_radianes), np.cos(angulo_radianes), 0],
                            [0, 0, 1]])


# Aplicar la matriz de rotación a los puntos
x_rotado = np.dot(rotacion_matrix, x)
y_rotado = np.dot(rotacion_matrix, y)
z_rotado = np.dot(rotacion_matrix, z)


# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# Dibujar los puntos originales y los puntos rotados
ax.quiver(0, 0, 0, x[0], x[1], x[2], color='b', label='X Original')
ax.quiver(0, 0, 0, y[0], y[1], y[2], color='g', label='Y Original')
ax.quiver(0, 0, 0, z[0], z[1], z[2], color='r', label='Z Original')


ax.quiver(0, 0, 0, x_rotado[0], x_rotado[1], x_rotado[2], color='c', label='X Rotado')
ax.quiver(0, 0, 0, y_rotado[0], y_rotado[1], y_rotado[2], color='m', label='Y Rotado')
ax.quiver(0, 0, 0, z_rotado[0], z_rotado[1], z_rotado[2], color='y', label='Z Rotado')


ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.legend()


plt.show()
