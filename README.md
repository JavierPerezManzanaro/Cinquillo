![Lenguaje Python](https://img.shields.io/badge/Lenguaje-Python-green)
![Versión de Python 3.10](https://img.shields.io/badge/Versión%20de%20Python-3.10-green)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)


# Juego de cartas del Cinquillo
## Descripción
Se reparten todas las cartas y el juego consiste en ir colocando las cartas sobre la mesa hasta quedarse sin ninguna.

La forma de colocar las cartas es la siguiente:
- Empieza el jugador que posea el cinco de oros y lo coloca.
- Después continua el jugador de la derecha y así sucesivamente.
Solo se pueden colocar cincos o todas aquellas cartas que siguen en progresión ascendente o descendente a las que hay en la mesa y sean del mismo palo. Es decir, si por ejemplo solamente está colocado el cinco de oros en la mesa, los jugadores solo podrán colocar el seis o el cuatro de oros o un cinco de otro palo.

Si un jugador no puede colocar ninguna carta, pasa, y el turno le corresponde al siguiente jugador. Un jugador puede pasar su turno, es decir, no depositar una carta, solamente si no tiene lugar para colocarla. Si un jugador puede poner varias cartas deberá elegir la que más le convenga para ganar el juego.

El primer jugador que consigue colocar todas sus cartas sobre la mesa (quedándose por tanto sin ninguna en la mano) es el ganador.
Fuente: https://es.wikipedia.org/wiki/Cinquillo_(juego)

![Mesa de juego](https://asisejuega.com/wp-content/uploads/2022/06/Cinquillo-1.jpg)
Fuente: https://asisejuega.com/juegos-de-cartas/cinquillo/


## Inteligencia artificial
"La inteligencia artificial es, en las ciencias de la computación, la disciplina que intenta replicar y desarrollar la inteligencia y sus procesos implícitos a través de computadoras."
Fuente: https://es.wikipedia.org/wiki/Inteligencia_artificial

En este caso la modalidad es sin aprendizaje.


## ¿Cómo se juega?
Para este juego, como en otros muchos juego clásicos, hay muchas variaciones en el juego. En este caso:
- No hay puntos
- En esta versión solo se puede tirar una carta por turno

Si no sabes jugar puedes consultar estas páginas webs:
- https://www.mundijuegos.com/multijugador/cinquillo/reglas/
- https://asisejuega.com/juegos-de-cartas/cinquillo/
- https://es.wikipedia.org/wiki/Cinquillo_(juego)


## Caraterísticas:
- Esta versión se ha desarrollado para jugar de 2 a 4 jugadores
- No tiene recursos gráficos, esta centrado en la lógica por eso se desarrolla en la terminal, mas adelante se implementara con Tkinter
- Las cartas se reparten en manos aleatoriamente
- Hay un filtro para validar la tirada:
  - No esta permitido tirar una carta que no este en tu mano
  - No puedes dejar ningún hueco sin tirar
  - Admite el uso de las palabras Sota, Caballo y Rey aunque solo se muestra el número en el panel


# Instrucciones de instalación
- Clonar el repositorio en local
- Tener instalado Python 3.10.
- Ejecutar: 'Cinquillo.py'


# Instrucciones de uso
Seguir las instrucciones que se van mostrando en el terminal


# Manifiesto de los archivos del repositorio
- README.md
  El archivo que estas leyendo

-Cinquillo.py
  Juego en Python


# Historial de versiones
## Funciones a implementar
Implementaciones futuras:
- Si escribimos Salir cuando preguntamos por la tirada salimos de la aplicación
- Añadir la ia:
  - Opción de poner el nombre que el usuario desee, por ejemplo: AI iMac, IA Ex Machina, IA Her
  - Sera uno o más jugadores autonomos
  - Abra dos niveles en la IA:
    - Nivel 1: Solo pretende colocar sus cartas
    - Nivel 2: Además de colocar sus cartas intenta impedir que sus openentes las coloquen
  - El proceso sera almacenar, en una variable, la importancia o el peso que se da a la carta según estos criterios:
    - Lo lejos que este del centro
    - Si hay dentras mas cartas en nuestra mano
    - Cuanto más lejos este del 5 peor
    - Cuando más lejos este de la más próxima peor
- Añadir cuatro niveles de ayuda. Nos ayudaremos de la función es_posible_tirar
    - Ayuda: múmero opciones para tirar
    - Mas ayuda: una jugada posible
    - Con IA nivel 1
    - Con AI nivel 2
- Hacer aplicación de escritorio con Tkinter

### 2.0.1
- Cambios menores

### 2
- Se implementa la Inteligencia Artificial básica

### 1.2
- Pasamos el archivo por autopep8
- Cambio en el lugar donde se llama al ganador

### 1
- Versión base


# Licencias y derechos de autor
CC (Creative Commons) de Reconocimiento – NoComercial – SinObraDerivada
![CC (Creative Commons) de Reconocimiento – NoComercial – SinObraDerivada](https://raw.githubusercontent.com/JavierPerezManzanaro/Maquetacion-de-masivos-responsive-html-con-noticias/main/Reconocimiento-no-comercial-sin-obra-derivada.png)


# Información de contacto del autor
Javier Pérez
javierperez@perasalvino.es


# Errores conocidos
-


# Motivación
Es un juego de cartas clásico que todo el mundo conoce. Realizar una aplicación que desarrolle el juego supone un reto. No se pueden tirar cualquier carta, hay que validar la tirada según varios parametros, implementamos la POO (las cartas y los jugadores son objetos), funciones, etc
Mas adelante usar uno o más jugadores como una Inteligencia Artificial supone un reto añadido.
Por último su paso de la version del terminal a una versión de escritorio con Tkinter es otro handicap.

# Créditos y agradecimientos
- A toda la comunidad web que me ha permitido ir ampliando mi formación.
- A mi familia por su infinita paciencia.
