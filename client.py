import flet as ft



def main(page: ft.Page) :
    page.title = 'Spice Detector'
    image = ft.Image(src=r'vecteezy_half-jalapeno-bright_49015796.png', width=100, height=100)

    img_button = ft.Container(
        content=image,
        on_click= lambda _: print('Hello World!'),
        ink = True,
        border_radius=10
    )

    page.add(
        img_button
    )

if __name__ == '__main__':
    ft.app(target=main, assets_dir="assets")