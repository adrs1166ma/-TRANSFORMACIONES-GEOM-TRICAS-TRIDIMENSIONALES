1. Importar la biblioteca numpy como np.

2. Definir las coordenadas cartesianas `x_cartesiano` y `y_cartesiano` como 3.0 y 4.0 respectivamente.

3. Crear un array numpy llamado `coordenadas_homogeneas` que representa las coordenadas cartesianas en coordenadas homogéneas (x, y, 1), donde el tercer componente es 1.0.

4. Definir la matriz de transformación de traslación `traslacion_matrix` utilizando np.array. Esta matriz representa una traslación en el plano, donde se desplaza el punto 2 unidades hacia la derecha y 3 unidades hacia arriba.

5. Aplicar la traslación a las coordenadas homogéneas utilizando la multiplicación de matrices con np.dot y almacenar el resultado en `coordenadas_homogeneas_traslacion`.

6. Obtener las coordenadas cartesianas resultantes `x_resultante` y `y_resultante` del array `coordenadas_homogeneas_traslacion`.

7. Imprimir las coordenadas cartesianas originales, las coordenadas homogéneas originales, las coordenadas homogéneas después de la traslación y las coordenadas cartesianas resultantes utilizando la función print con formato de cadena f.
