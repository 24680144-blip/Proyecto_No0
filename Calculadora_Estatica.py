import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Estatica - TAP"
    page.window_width = 350
    page.window_height = 500
    page.window_resizable = False
    page.padding = 20

    numero_actual = ""
    numero_anterior = ""
    operador = ""

    # DISPLAY
    display = ft.Text("0", size=30, weight=ft.FontWeight.BOLD)

    seccion_display = ft.Container(
        content=display,
        bgcolor=ft.Colors.BLACK12,
        height=80,
        alignment=ft.alignment.Alignment(0, 0),
        border=ft.border.all(2, ft.Colors.RED)
    )

    # -------- FUNCION NUMEROS --------
    def numero_click(e):
        nonlocal numero_actual
        numero_actual += e.control.data

        if numero_anterior:
            display.value = numero_anterior + " " + operador + " " + numero_actual
        else:
            display.value = numero_actual

        page.update()

    # -------- FUNCION OPERACIONES --------
    def operacion_click(e):
        nonlocal numero_actual, numero_anterior, operador

        if e.control.data == "=":
            if numero_anterior and numero_actual and operador == "+":
                resultado = float(numero_anterior) + float(numero_actual)
                display.value = str(resultado)

                numero_actual = str(resultado)
                numero_anterior = ""
                operador = ""
            elif numero_anterior and numero_actual and operador == "-":
                resultado = float(numero_anterior) - float(numero_actual)
                display.value = str(resultado)

                numero_actual = str(resultado)
                numero_anterior = ""
                operador = ""
        else:
            numero_anterior = numero_actual
            numero_actual = ""
            operador = e.control.data

            display.value = numero_anterior + " " + operador

        page.update()

    # -------- BOTON NUMERO --------
    def boton_numero(numero):
        return ft.Container(
            content=ft.Text(
                str(numero),
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE
            ),
            alignment=ft.alignment.Alignment(0, 0),
            expand=1,
            height=70,
            bgcolor=ft.Colors.BLUE_600,
            border_radius=10,
            data=str(numero),
            on_click=numero_click
        )

    # -------- BOTON OPERACION --------
    def boton_operacion(simbolo):
        return ft.Container(
            content=ft.Text(
                simbolo,
                size=24,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE
            ),
            alignment=ft.alignment.Alignment(0, 0),
            expand=1,
            height=60,
            bgcolor=ft.Colors.GREEN_600,
            border_radius=10,
            data=simbolo,
            on_click=operacion_click
        )

    # SECCION NUMEROS
    seccion_numeros = ft.Column(
        controls=[
            ft.Row([boton_numero(1), boton_numero(2), boton_numero(3)]),
            ft.Row([boton_numero(4), boton_numero(5), boton_numero(6)]),
            ft.Row([boton_numero(7), boton_numero(8), boton_numero(9)]),
        ],
        spacing=10
    )

    # SECCION OPERACIONES
    seccion_operaciones = ft.Row(
        controls=[
            boton_operacion("+"),
            boton_operacion("-"),
            boton_operacion("="),
        ],
        spacing=10
    )

    page.add(
        ft.Column(
            controls=[
                seccion_display,
                ft.Text("Números:"),
                seccion_numeros,
                ft.Divider(),
                ft.Text("Operaciones:"),
                seccion_operaciones,
            ],
            spacing=15
        )
    )

if __name__ == "__main__":
    ft.app(target=main)