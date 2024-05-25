1. Importar las bibliotecas necesarias: numpy para operaciones numéricas, matplotlib.pyplot para graficar y Axes3D de mpl_toolkits.mplot3d para gráficos en 3D.

2. Crear puntos 3D utilizando arrays numpy para las coordenadas x, y, z.

3. Definir un ángulo de rotación en grados y convertirlo a radianes.

4. Crear una matriz de rotación 3D `rotacion_matrix` utilizando np.array. Esta matriz representa una rotación en torno al eje Z con el ángulo especificado.

5. Aplicar la matriz de rotación a los puntos originales (x, y, z) utilizando la multiplicación de matrices con np.dot y almacenar los puntos rotados en (x_rotado, y_rotado, z_rotado).

6. Crear una figura 3D utilizando plt.figure() y un subplot 3D utilizando fig.add_subplot.

7. Dibujar los puntos originales y los puntos rotados en el subplot 3D utilizando la función ax.quiver para representar vectores en 3D.

8. Establecer los límites de los ejes x, y, z utilizando ax.set_xlim, ax.set_ylim y ax.set_zlim.

9. Agregar una leyenda a la gráfica utilizando ax.legend().

10. Mostrar la gráfica utilizando plt.show().
