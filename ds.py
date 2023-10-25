import flet as ft
import aiohttp
import asyncio

pokemon_actual = -1

async def main(page: ft.Page):
    page.title = 'Nintendo DS Lite'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 1000
    page.window_height = 800
    page.window_resizable = False
    page.padding = 0
    page.fonts = {'pkmn': 'https://github.com/hpneo/pokedexjs/blob/master/public/fonts/pokemon/Pokemon.ttf?raw=true'}
    
    async def peticion(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()
    
    async def evento_get_pokemon(e: ft.ContainerTapEvent):
        global pokemon_actual
        if e.control == flecha_superior or e.control==flecha_derecha:
            pokemon_actual += 1
        else:
            pokemon_actual -= 1

        numero = (pokemon_actual%151)+1
        resultado = await peticion(f'https://pokeapi.co/api/v2/pokemon/{numero}')
        
        datos = f'Name: {resultado["name"].capitalize()}\n\nAbilities:'
        for elemento in resultado['abilities']:
            habilidad = elemento['ability']['name']
            datos += f'\n{habilidad.capitalize()}'
        datos += f'\n\nHeight (m): {resultado["height"]/10}'
        datos += f'\nWeight (kg): {resultado["weight"]/10}'
        texto.value = datos
        sprite_url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{numero}.png'
        imagen.src = sprite_url
        await page.update_async()

    async def blink():
        while True:
            await asyncio.sleep(1)
            luz_verde.bgcolor = ft.colors.LIGHT_GREEN
            await page.update_async()
            await asyncio.sleep(0.1)
            luz_verde.bgcolor = ft.colors.GREEN
            await page.update_async()

    luz_verde = ft.Container(width=8, height=25, bgcolor=ft.colors.GREEN, border_radius=20)

    sonido = ft.Container(
                ft.Stack(
                    [
                        ft.Container(width=10, height=10, bgcolor=ft.colors.BLACK, border_radius=50, left=0, top=0), # Arriba - izquierda
                        ft.Container(width=10, height=10, bgcolor=ft.colors.BLACK, border_radius=50, left=20, top=0), # Arriba - centro
                        ft.Container(width=10, height=10, bgcolor=ft.colors.BLACK, border_radius=50, right=0, top=0), # Arriba - derecha
                        ft.Container(width=10, height=10, bgcolor=ft.colors.BLACK, border_radius=50, left=0, bottom=0), # Abajo - izquierda
                        ft.Container(width=10, height=10, bgcolor=ft.colors.BLACK, border_radius=50, left=20, bottom=0), # Abajo - centro
                        ft.Container(width=10, height=10, bgcolor=ft.colors.BLACK, border_radius=50, right=0, bottom=0), # Abajo - derecha   
                    ]), width=50, height=30, bgcolor=ft.colors.GREY
                )
    
    sprite_url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/0.png'

    imagen = ft.Image(src=sprite_url, scale=10, width=20, height=20, top=100, right=137.5)
    
    pantalla_superior = ft.Stack(
        [
            ft.Container(width=300, height=225, bgcolor=ft.colors.BLACK, border_radius=5),
            ft.Container(width=275, height=200, bgcolor=ft.colors.GREEN, left=12.5, top=12.5),
            imagen
        ]
    )

    texto = ft.Text(value='Nintendo DS Lite', color=ft.colors.BLACK, size=15, text_align=ft.TextAlign.LEFT, top=18, left=30,
                    font_family='pkmn')

    pantalla_inferior = ft.Stack(
        [
            ft.Container(width=300, height=225, bgcolor=ft.colors.BLACK, border_radius=5),
            ft.Container(width=275, height=200, bgcolor=ft.colors.GREEN, left=12.5, top=12.5),
            texto
        ]
    )

    items_superior = [
        ft.Container(width=50, height=30),
        ft.Container(sonido, width=50, height=30),
        ft.Container(width=50, height=30),
        ft.Container(pantalla_superior, width=300, height=225),
        ft.Container(width=50, height=30),
        ft.Container(sonido, width=50, height=30),
        ft.Container(width=50, height=30)
    ]

    items_centro = [
        ft.Container(width=296, height=25),
        ft.Container(width=8, height=25, bgcolor=ft.colors.BLACK, border_radius=20),
        ft.Stack(
                    [
                        ft.Container(width=245, height=25, bgcolor=ft.colors.GREY), # Botón Micrófono
                        ft.Container(ft.Text(value='MIC.', color=ft.colors.WHITE, size=15, text_align=ft.TextAlign.LEFT),
                                     width=40, height=25, bgcolor=ft.colors.GREY, left=5, top=0), # Micrófono
                    ]
                ),
        ft.Container(width=8, height=25, bgcolor=ft.colors.GREEN_100, border_radius=20),
        ft.Container(width=5, height=25),
        luz_verde,
    ]

    boton = ft.Container(
                ft.Stack(
                    [
                        ft.Container(ft.Text(value='X', color=ft.colors.WHITE, size=15, text_align=ft.TextAlign.CENTER),
                                     padding=5, width=35, height=35, bgcolor=ft.colors.BLACK, border_radius=50, left=32.5, top=0), # X
                        ft.Container(ft.Text(value='B', color=ft.colors.WHITE, size=15, text_align=ft.TextAlign.CENTER),
                                     padding=5, width=35, height=35, bgcolor=ft.colors.BLACK, border_radius=50, left=32.5, bottom=0), # B
                        ft.Container(ft.Text(value='A', color=ft.colors.WHITE, size=15, text_align=ft.TextAlign.CENTER),
                                     padding=5, width=35, height=35, bgcolor=ft.colors.BLACK, border_radius=50, right=0, top=32.5), # A
                        ft.Container(ft.Text(value='Y', color=ft.colors.WHITE, size=15, text_align=ft.TextAlign.CENTER),
                                     padding=5, width=35, height=35, bgcolor=ft.colors.BLACK, border_radius=50, left=0, top=32.5), # Y
                        
                    ]), width=100, height=100, bgcolor=ft.colors.GREY
                )
    
    start = ft.Container(
                ft.Stack(
                    [
                        ft.Container(width=15, height=15, bgcolor=ft.colors.BLACK, border_radius=50, left=0, top=0), # Botón Start
                        ft.Container(ft.Text(value='START', color=ft.colors.WHITE, size=10, text_align=ft.TextAlign.LEFT),
                                     width=60, height=15, bgcolor=ft.colors.GREY, left=20, top=0), # Start
                        ft.Container(width=15, height=15, bgcolor=ft.colors.BLACK, border_radius=50, left=0, bottom=0), # Botón Select
                        ft.Container(ft.Text(value='SELECT', color=ft.colors.WHITE, size=10, text_align=ft.TextAlign.LEFT),
                                     width=60, height=15, bgcolor=ft.colors.GREY, left=20, bottom=0), # Select
                        
                    ]), width=100, height=40, bgcolor=ft.colors.GREY
                )
    
    flecha_superior = ft.Container(width=35, height=35, bgcolor=ft.colors.BLACK, left=32.5, top=0, on_click=evento_get_pokemon)
    flecha_inferior = ft.Container(width=35, height=35, bgcolor=ft.colors.BLACK, left=32.5, bottom=0, on_click=evento_get_pokemon)
    flecha_derecha = ft.Container(width=35, height=35, bgcolor=ft.colors.BLACK, right=0, top=32.5, on_click=evento_get_pokemon)
    flecha_izquierda = ft.Container(width=35, height=35, bgcolor=ft.colors.BLACK, left=0, top=32.5, on_click=evento_get_pokemon)

    cruceta = ft.Container(
                ft.Stack(
                    [
                        ft.Stack([
                            flecha_superior, # Arriba
                            ft.Container(width=4, height=22.5, bgcolor=ft.colors.WHITE, border_radius=20, left=48, top=5.5)
                        ]),
                                
                        ft.Stack([
                            flecha_inferior, # Abajo
                            ft.Container(width=4, height=22.5, bgcolor=ft.colors.WHITE, border_radius=20, left=48, bottom=5.5)
                        ]),

                        ft.Stack([
                            flecha_derecha, # Derecha
                            ft.Container(width=22.5, height=4, bgcolor=ft.colors.WHITE, border_radius=20, right=5.5, bottom=48)
                        ]),

                        ft.Stack([
                            flecha_izquierda, # Izquierda
                            ft.Container(width=22.5, height=4, bgcolor=ft.colors.WHITE, border_radius=20, left=5.5, bottom=48)
                        ]),

                        ft.Container(width=35, height=35, bgcolor=ft.colors.BLACK, left=32.5, top=32.5), # Centro
                        
                    ]), width=100, height=100, bgcolor=ft.colors.GREY
                )
    
    panel_derecha = ft.Column(
        [
            ft.Container(width=100, height=60),
            ft.Container(boton, width=100, height=100),
            ft.Container(width=100, height=55),
            ft.Container(start, width=100, height=40)
        ],
    spacing=0)

    panel_izquierdo = ft.Column(
        [
            ft.Container(width=100, height=85),
            ft.Container(cruceta, width=100, height=100)
        ],
    spacing=0)

    items_inferior = [
        ft.Container(width=25, height=25),
        ft.Container(panel_izquierdo, width=100, height=300),
        ft.Container(width=25, height=25),
        ft.Container(pantalla_inferior, width=300, height=225),
        ft.Container(width=25, height=25),
        ft.Container(panel_derecha, width=100, height=300)
    ]
    
    superior = ft.Container(content=ft.Row(items_superior, spacing=0), width=600, height=300, margin=ft.margin.only(top=40), bgcolor=ft.colors.GREY,
                            border_radius=20, border=ft.border.all())
    centro = ft.Container(content=ft.Row(items_centro, spacing=0), width=600, height=40, bgcolor=ft.colors.GREY, border_radius=20,
                          border=ft.border.all())
    inferior = ft.Container(content=ft.Row(items_inferior, spacing=0), width=600, height=300, bgcolor=ft.colors.GREY,
                            border_radius=20, border=ft.border.all())

    col = ft.Column(spacing=0, controls=[
        superior,
        centro,
        inferior,
    ])

    contenedor = ft.Container(col, width=1000, height=800, bgcolor=ft.colors.WHITE, alignment=ft.alignment.top_center)

    await page.add_async(contenedor)
    await blink()

if __name__ == '__main__':
    ft.app(target=main)