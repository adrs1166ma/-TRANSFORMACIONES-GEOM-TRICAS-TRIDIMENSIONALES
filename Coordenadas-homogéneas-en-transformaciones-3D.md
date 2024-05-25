1. Definir un punto 3D en coordenadas cartesianas `punto_cartesiano` como un array numpy con coordenadas (1.0, 2.0, 3.0).

2. Convertir el punto a coordenadas homogéneas agregando un componente 1.0 al final del array utilizando np.append.

3. Definir una matriz de traslación 3D `matriz_traslacion` utilizando np.array. Esta matriz representa una traslación en el espacio tridimensional, desplazando el punto 2 unidades en x, 3 unidades en y y 1 unidad en z.

4. Aplicar la matriz de traslación al punto homogéneo utilizando la multiplicación de matrices con np.dot y almacenar el resultado en `punto_homogeneo_traslacion`.

5. Convertir el resultado de vuelta a coordenadas cartesianas extrayendo los primeros tres elementos del array `punto_homogeneo_traslacion`.

6. Imprimir el punto 3D original en coordenadas cartesianas, el punto 3D en coordenadas homogéneas y el punto 3D después de la traslación utilizando la función print.
