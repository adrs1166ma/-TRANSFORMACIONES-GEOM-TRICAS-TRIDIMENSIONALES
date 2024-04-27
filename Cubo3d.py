import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


# Definir vértices de un cubo en coordenadas 3D
vertices_cubo = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])


# Definir las caras del cubo
caras_cubo = [
    [vertices_cubo[0], vertices_cubo[1], vertices_cubo[2], vertices_cubo[3]],
    [vertices_cubo[4], vertices_cubo[5], vertices_cubo[6], vertices_cubo[7]],
    [vertices_cubo[0], vertices_cubo[1], vertices_cubo[5], vertices_cubo[4]],
    [vertices_cubo[2], vertices_cubo[3], vertices_cubo[7], vertices_cubo[6]],
    [vertices_cubo[1], vertices_cubo[2], vertices_cubo[6], vertices_cubo[5]],
    [vertices_cubo[4], vertices_cubo[7], vertices_cubo[3], vertices_cubo[0]]
]


# Factor de escala en cada dimensión (x, y, z)
factor_escala = np.array([2, 1.5, 0.5])


# Aplicar el escalado en 3D al cubo
vertices_cubo_escalado = vertices_cubo * factor_escala


# Visualización del cubo original y escalado
fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
ax.add_collection3d(Poly3DCollection(caras_cubo, alpha=0.25, linewidths=1, edgecolor='r'))
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title('Cubo Original')


ax = fig.add_subplot(122, projection='3d')
ax.add_collection3d(Poly3DCollection(caras_cubo, alpha=0.25, linewidths=1, edgecolor='g'))
ax.set_xlim([0, 4])
ax.set_ylim([0, 4])
ax.set_zlim([0, 4])
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title('Cubo Escalado')


plt.show()
