import flet as ft


def main(page: ft.Page):
    page.title = "Pizza Builder"
    page.window.width = 450
    page.window.height = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    base = ft.Image(src="pizzabase.png", width = 300)
    pepperoni = ft.Image(src="pepperoni.png", width = 300, visible = False)
    ham = ft.Image(src="ham.png", width = 300, visible = False)
    corn = ft.Image(src="corn.png",width = 300, visible = False)
    bacon = ft.Image(src="bacon.png", width = 300, visible = False)

    def enable_disable_pepperoni(e):
        pepperoni.visible = e.control.value
        page.update()

    def enable_disable_ham(e):
        ham.visible = e.control.value
        page.update()

    def enable_disable_corn(e):
        corn.visible = e.control.value
        page.update()

    def enable_disable_bacon(e):
        bacon.visible = e.control.value
        page.update()

    switches = ft.Column([
        ft.Switch(label="Pepperoni", on_change=enable_disable_pepperoni),
        ft.Switch(label="Ham", on_change=enable_disable_ham),
        ft.Switch(label="Corn", on_change=enable_disable_corn),
        ft.Switch(label="Bacon", on_change=enable_disable_bacon),
    ])
    
    pizza_layers = ft.Stack([
        base,
        pepperoni,
        ham,
        corn,
        bacon,
    ])

    page.add(
        ft.Text("Build your pizza", size=27, weight="bold"),
        pizza_layers,
        switches
    )
    
ft.run(main=main,assets_dir="assets")

    


