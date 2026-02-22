Flet Calculator App

Referencia y Créditos
Este proyecto fue desarrollado tomando como base y referencia el tutorial oficial de Flet:
[Flet Calculator Tutorial](https://docs.flet.dev/tutorials/calculator/)

1. Definición de Estilos y Componentes
El código utiliza Programación Orientada a Objetos (POO) para definir botones reutilizables con estilos específicos.

Clase Base `CalcButton`: Hereda de `ft.Button`. Utiliza `expand: int = 1` para que cada botón ocupe una fracción igual de espacio dentro de su contenedor horizontal.
Clases Especializadas**:
     `DigitButton`: Botones para números (Gris oscuro).
     `ActionButton`: Botones para operaciones aritméticas (Naranja).
     `ExtraActionButton`: Botones para funciones auxiliares como AC y % (Gris claro).



2. Lógica de la Clase `CalculatorApp`
Esta clase centraliza la interfaz y el estado de la aplicación.

Inicialización (`init`)
Se configuran las propiedades visuales del contenedor principal:
- Dimensiones: Ancho fijo de 350px.
- Diseño: Fondo negro (`ft.Colors.BLACK`) con bordes redondeados.
- Display: Se crea `self.result`, un objeto `ft.Text` que actúa como la pantalla de la calculadora, iniciando en "0".

Estructura de la Interfaz (Layout)
La interfaz se construye mediante una Columna Principal que contiene múltiples Filas:
- Cada fila (`ft.Row`) agrupa botones relacionados.
- El botón "0" en la última fila tiene un `expand=2`, lo que lo hace el doble de ancho que los demás, emulando el diseño clásico de calculadoras.

3. Procesamiento de Eventos: `button_clicked`
Es el método encargado de gestionar qué sucede cuando el usuario presiona un botón:

1.  Captura de datos: `data = e.control.content` extrae el texto del botón presionado.
2.  Lógica de Entrada Numérica: 
    - Si el valor es un dígito o un punto, se concatena al número actual en pantalla.
    - Si `self.new_operand` es verdadero (después de presionar un signo de operación), el nuevo número reemplaza al anterior en lugar de concatenarse.
3.  Lógica de Operación:
    - Al presionar `+`, `-`, `*` o `/`, la calculadora procesa cualquier operación pendiente llamando a `self.calculate()`.
    - Guarda el resultado como el nuevo primer operando (`self.operand1`) y queda a la espera del segundo.
4.  Funciones de Formato:
    - `format_number`: Elimina el `.0` innecesario (ej: convierte `8.0` en `8`).
    - `calculate`: Realiza la operación matemática y maneja la excepción de división por cero devolviendo un mensaje de "Error".



4. Gestión del Estado (`reset`)
El método `reset()` devuelve la calculadora a su estado inicial:
- Define el operador por defecto como `+`.
- Resetea el operando acumulado a `0`.
- Marca `new_operand` como `True` para que la próxima entrada numérica limpie la pantalla.


     Unidad I:

---- 1.1 Interfaz Gráfica de Usuario (GUI) con Flet
La Interfaz Gráfica de Usuario es el conjunto de elementos visuales que permiten la interacción entre el usuario y el sistema. En Flet, esto se construye mediante un árbol de controles (widgets).

Flet es un framework en el cual no necesitamos HTML o CSS complejo. La interfaz se define mediante una función principal (usualmente llamada main) que recibe un objeto page.
En Flet, a diferencia de otros frameworks de escritorio, la interfaz no se "dibuja" píxel por píxel manualmente, sino que se construye mediante una jerarquía de controles que se renderizan usando el motor de Flutter.
     
---- La estructura básica y el Grafo de Controles
Cada aplicación que hicimos (desde la calculadora básica hasta el registro) sigue este flujo:

Importación: import flet as ft.
1. Punto de entrada: Una función main(page: ft.Page).
2. Definición de Controles: Instanciar objetos como ft.TextField() o ft.ElevatedButton().
3. Integración: Añadir los controles a la página con page.add() o page.controls.append().

---- Aqui un ejemplo de como se usa el concepto de organizar elementos: 
<p align="center">
     <img width="800" height="535" alt="image" src="https://github.com/user-attachments/assets/6d14d577-cf45-424b-b9a0-c0c1323a2fea" />
</p>

---- Propiedades fundamentales del contenedor Page
Es importante recordar que page no es solo un lienzo vacío, tiene propiedades que controlan la experiencia del usuario (UX):

- page.theme_mode: Usado en nuestra calculadora para alternar entre ft.ThemeMode.LIGHT y DARK.
- page.vertical_alignment: Lo usamos en el Chat para centrar los elementos o enviarlos al fondo.
- page.padding: Espaciado interno que evita que los botones toquen los bordes de la ventana.

---- Layout Containers: El esqueleto de los proyectos
Usamos tres formas de organizar la interfaz:
<p align="center">
     <img width="727" height="310" alt="image" src="https://github.com/user-attachments/assets/dbfccccc-0584-4833-9934-a8b3820131ea" />
</p>

---- Propiedades Visuales Críticas (Visual Styling)
En el ejercicio del Chat, aprendimos que la estética no es solo lujo, es funcionalidad. Usamos propiedades que definen la jerarquía visual:

expand: Esta propiedad es mágica. Si a la lista de mensajes del Chat le poníamos expand=True, Flet le ordenaba ocupar todo el espacio sobrante, empujando la caja de texto hacia abajo.
spacing y alignment: Controlan el "aire" entre los controles. En la calculadora, un spacing=5 evitaba que los botones parecieran una sola masa gris.

---- 1.2 y 1.3 Eventos y su manejo 
     
En el desarrollo de interfaces con Flet, la interactividad se basa en el modelo de Programación Orientada a Eventos. Esto significa que el flujo del programa no es lineal, sino que espera a que el usuario realice una acción.

1.2 Tipos de Eventos 
En los proyectos de la Calculadora y el Chat, hemos implementado los tipos de eventos más críticos:

- Eventos de Acción (on_click): Es el evento rey. Lo usamos en cada botón de la calculadora. Se dispara cuando el puntero presiona y suelta el control.
- Eventos de Entrada (on_change): Lo vimos en el Registro de Usuario. Cada vez que el usuario escribe una sola letra, el evento se dispara. Es vital para validaciones en tiempo real (ej. poner el borde rojo si el campo está vacío).
- Eventos de Teclado (on_submit): Fundamental en nuestro Chat. Permite que al presionar "Enter", el mensaje se envíe sin tener que buscar el botón con el mouse.
- Eventos de Página (on_route_change): Aunque es más avanzado, lo mencionamos porque permite crear apps con múltiples pantallas.

1.3 Manejo de Eventos 
El "Manejador de Eventos" (Event Handler) es la función que se ejecuta cuando el evento ocurre. En Flet, estas funciones reciben un objeto ControlEvent (comúnmente llamado e).

- Análisis de Caso: El Botón de la Calculadora
En nuestra calculadora, no creamos una función para cada botón, sino que usamos una lógica centralizada.
<p align="center">
     <img width="617" height="277" alt="image" src="https://github.com/user-attachments/assets/2a8682f1-a057-492c-8b22-e071b6a816da" />
</p>

---- Concepto Clave: El objeto e (ControlEvent)
Este objeto es una mina de oro de información:

- e.control: El objeto Python que disparó el evento (el botón, el campo de texto).
- e.data: El valor crudo enviado por el evento (en un TextField, es el texto actual).
- e.page: Una referencia a la página, útil si la función está fuera del main.

---- Lambdas vs Funciones Definidas
-- En la Unidad I, aprendimos dos formas de asignar eventos:

Funciones Nombradas: Ideales para lógica compleja (como el cálculo matemático).
- on_click = calcular
      Se usan cuando la lógica es extensa o requiere múltiples pasos.
           - Ventaja: Son fáciles de leer y depurar.
           - Desventaja: Solo reciben el objeto e por defecto. Si necesitas pasarle un número específico, se complica.

Funciones Lambda: Ideales para pasar argumentos extra o lógica de una sola línea.
- on_click = lambda _: print("Click!")
En la Calculadora, teníamos 10 botones numéricos. Hacer 10 funciones def click_1(), def click_2()... es ineficiente y viola el principio DRY (Don't Repeat Yourself).

   Una "Lambda" es una función de una sola línea sin nombre. En Flet, la usamos como un "puente".
-- El truco del guion bajo: A veces verás lambda _:. El _ es una convención en Python para decir: "Sé que aquí viene un evento e, pero no lo voy a usar, solo quiero ejecutar mi función".
<p align="center">
     <img width="877" height="352" alt="image" src="https://github.com/user-attachments/assets/5f4a3c2e-457c-4b41-a47a-8eb9b8ed8442" />
</p>

En nuestra practica de Chat, no queríamos que el usuario tuviera que soltar el teclado para hacer clic en "Enviar". Queríamos una experiencia fluida. Para lograrlo, profundizamos en la jerarquía de eventos de Flet.

Existen dos formas de capturar el teclado:

- A nivel de Control (on_submit): Específico para el TextField. Se dispara solo cuando el foco está en ese cuadro de texto y se presiona Enter.
- A nivel de Página (page.on_keyboard_event): Captura todas las teclas presionadas en la aplicación, sin importar dónde esté el cursor.

<p align="center">
<img width="691" height="238" alt="image" src="https://github.com/user-attachments/assets/6c4b652a-53f5-42fd-8149-d44ff3dd872b" />
</p>

  Manejo de Componentes Gráficos de Control (1.4)
En Flet, cada componente (Control) es una clase de Python que hereda propiedades de una jerarquía de Flutter. 
---- 1.4.1 Controles de Entrada de Datos (Input Controls)
Son los que permiten al usuario comunicarse con la lógica del programa.

-- ft.TextField: Lo usamos en el Registro y el Chat.
  -- Propiedades clave: password=True (para ocultar caracteres), can_reveal_password (el icono del ojo), y border_color.

-- ft.Checkbox: Utilizado en validaciones de "Acepto términos". Su valor es booleano (True/False).
-- ft.Dropdown: Ideal para selecciones cerradas (como elegir el país en un formulario).

---- 1.4.2 Controles de Acción (Buttons)
Flet ofrece varios sabores de botones, cada uno con una semántica visual distinta:

- ft.ElevatedButton: El botón estándar con sombra. (Usado en el Registro).
- ft.FilledButton: Un botón con color de fondo sólido, ideal para la acción principal (como "Enviar").
- ft.IconButton: Un botón que es solo un icono (ej. el botón de enviar mensaje con forma de avión de papel en el Chat).

---- 1.4.3 Controles de Organización (Layout & Containers)

ft.Container: Es el control más versátil. Permite añadir padding (espacio interno), margin (espacio externo), border (bordes), y gradient (degradados).
ft.Card: Un contenedor con elevación y bordes redondeados predefinidos. Muy útil para mostrar perfiles de usuario.

<p align="center">
<img width="925" height="313" alt="image" src="https://github.com/user-attachments/assets/57e00427-0b05-497a-87b5-b6887542e8e2" />
</p>

---- 1.4.4 Listas Dinámicas (ListView)
En el Chat, enfrentamos un problema: si había muchos mensajes, se salían de la pantalla. La solución fue el componente ft.ListView.

-- auto_scroll=True: Una propiedad fundamental que hace que la lista baje automáticamente cuando llega un mensaje nuevo, mejorando drásticamente la UX (Experiencia de Usuario. UX).




---- Bibliografias

Flet Dev. (2024). Flet: Build Flutter apps in Python. Recuperado de https://flet.dev/docs/
Flet Dev. (2024). Layout Basics: Columns, Rows and Containers. Recuperado de https://flet.dev/docs/controls/layout
Google Developers. (2024). Flutter Documentation: Widget Catalog. Recuperado de https://docs.flutter.dev/development/ui/widgets
Google Material Design. (2024). The Material Design System (M3). Recuperado de https://m3.material.io/
Python Software Foundation. (2024). Lambda Expressions and Functional Programming Tools. Recuperado de https://docs.python.org/3/tutorial/controlflow.html
Real Python. (2024). How to Use Python Lambda Functions. Recuperado de https://realpython.com/python-lambda/

Desarrollado con ❤️ usando Python y Flet.
<p align="center">

</p>

