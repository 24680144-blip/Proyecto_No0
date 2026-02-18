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

Desarrollado con ❤️ usando Python y Flet.
