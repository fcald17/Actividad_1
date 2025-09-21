# Juego de Pintado en Python
Una simple hoja de dibujo usando la interface visual de Python para hacer líneas y figuras. El código original fue obtenido del sitio Grant Jenks, pero este estaba incompleto, así que en este repositorio, se le hicieron algunos cambios para ampliar su funcionalidad.
## Acerca del Código Base y su Funcionamiento
Su funcionamiento es bastante simple, se selecciona con teclas asignadas, el color y la figura que se desea hacer y el programa la genera en ese rango seleccionado. En su versión original, sólo podía hacer líneas y cuadrados y contaba con cinco colores (negro, blanco, verde, azul y rojo)
## Cambios Realizados al Código Base
Para volver las funcionalidades más amplias del programa, dentro de este repositorio se hicieron catro añadidos al código original.
### Primer Cambio: Agregado de un Sexto Color
Como mecionamos anteriormente, el código sólo cuenta con cinco colores, así que decidimos agregar un sexto, el morado, con su correspondiente tecla asignada para ampliar la variedad
### Segundo Cambio: Agregar la función para crear un rectángulo
Creamos una nueva función para poder generar un rectángulo definiendo sus límites por las coordenadas del punto inicial y el final, el ancho por los componentes x y el alto por los componentes y.
### Tercer Cambio: Agregar la función para crear un triángulo
Creamos una nueva función que tome la distancia entre el punto inicial y el final para el largo de todos los lados del triángulo, resultando en un triángulo equilatero.
### Cuarto Cambio: Agregar la función para crear un círculo
Creamos una nueva función que tome las coordenadas de inicio y fin como referencia para el radio del círculo.
