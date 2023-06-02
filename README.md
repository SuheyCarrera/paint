# paint
proyecto de programación 
Este código de ejemplo utiliza la biblioteca Pygame para crear una interfaz gráfica en la que puedes dibujar y manipular figuras geométricas. El programa te permite realizar diferentes acciones, como dibujar líneas, cuadrados, rectángulos, círculos y triángulos, así como cambiar los colores de fondo y trazo.

Requisitos
Pygame: Asegúrate de tener instalada la biblioteca Pygame en tu entorno Python antes de ejecutar este código. Puedes instalar Pygame usando el siguiente comando:

Copy code
pip install pygame
Uso
El programa mostrará una ventana de 800x600 píxeles donde podrás interactuar. Puedes ingresar comandos en la línea de comandos que aparece como cmd>. A continuación se muestra una lista de los comandos disponibles:

linea -h: Dibuja una línea horizontal en la posición (100, 200) con el color de trazo actual.

Ejemplo: linea -h
linea -v: Dibuja una línea vertical en la posición (100, 200) con el color de trazo actual.

Ejemplo: linea -v
borrar: Borra el último trazo dibujado en la posición (100, 200) con un rectángulo de tamaño 100x100 del color de fondo.

Ejemplo: borrar
fondo <nombre_color>: Cambia el color de fondo al color especificado.

Ejemplo: fondo rojo
trazo <nombre_color>: Cambia el color de trazo al color especificado.

Ejemplo: trazo azul
pixelsize <tamaño>: Ajusta el grosor del trazo al tamaño especificado.

Ejemplo: pixelsize 3
cuadrado <x> <y> <tamaño>: Dibuja un cuadrado en la posición (x, y) con el tamaño especificado y el color de trazo actual.

Ejemplo: cuadrado 200 200 100
rectangulo <x> <y> <ancho> <alto>: Dibuja un rectángulo en la posición (x, y) con el ancho y alto especificados y el color de trazo actual.

Ejemplo: rectangulo 300 300 200 100
circulo <x> <y> <radio>: Dibuja un círculo en la posición (x, y) con el radio especificado y el color de trazo actual.

Ejemplo: circulo 400 400 50
triangulo_equilatero <x> <y> <longitud_lado>: Dibuja un triángulo equilátero en la posición (x, y) con la longitud de lado especificada y el color de trazo actual.

Ejemplo: triangulo_equilatero 500 500 100
triangulo_escaleno <x> <y> <lado1> <lado2> <lado3>: Dibuja un triángulo escaleno en la posición (x, y) con los lados especificados y el color de trazo actual.

Ejemplo: triangulo_escaleno 600 600 50 80 70
triangulo_isosceles <x> <y> <base> <altura>: Dibuja un triángulo isósceles en la posición (x, y) con la base y altura especificadas y el color de trazo actual.

Ejemplo: triangulo_isosceles 700 700 120 80
figura_mover <dx> <dy>: Mueve la figura en la posición (200, 200) en la dirección (dx, dy).

Ejemplo: figura_mover 50 -20
figura_cambiar_color <nombre_color>: Cambia el color de la figura en la posición (200, 200) al color especificado.

Ejemplo: figura_cambiar_color verde
figura_dibujar: Dibuja la figura en la posición (200, 200) con el color y trazo actuales.

Ejemplo: figura_dibujar
rectangulo_mover <dx> <dy>: Mueve el rectángulo en la posición (400, 300) en la dirección (dx, dy).

Ejemplo: rectangulo_mover -30 40
rectangulo_cambiar_color <nombre_color>: Cambia el color del rectángulo en la posición (400, 300) al color especificado.

Ejemplo: rectangulo_cambiar_color rosa
rectangulo_dibujar: Dibuja el rectángulo en la posición (400, 300) con el color y trazo actuales.

Ejemplo: rectangulo_dibujar
color <nombre_color>: Cambia el color de trazo al color especificado.

Ejemplo: color rojo
help: Muestra una lista de comandos disponibles y ejemplos de uso.

Nota: Los colores disponibles son: rojo, verde, azul, amarillo y rosa.

Ejecución
Asegúrate de tener instalada la biblioteca Pygame.
Ejecuta el archivo de código en un entorno Python.
Se abrirá una ventana de Pygame donde podrás interactuar.
Ingresa comandos en la línea de comandos cmd> según las opciones disponibles.
Observa cómo se dibujan las figuras y se aplican los cambios.
¡Diviértete dibujando y explorando las diferentes funciones de este programa! Si tienes alguna pregunta, consulta o problema, no dudes en preguntar
