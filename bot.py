import os

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Montar la carpeta "CSS" en la ruta "/CSS"
app.mount("/CSS", StaticFiles(directory="CSS"), name="CSS")
# Montar la carpeta "raw" en la ruta "/raw"
app.mount("/raw", StaticFiles(directory="raw"), name="raw")

def menu_desayuno():
    print("Desayunos completos desde $70 pesos.")
    print("Incluye: café y fruta.")
    print("Platillos disponibles:")
    print("1. Huevos al gusto")
    print("2. Omelettes")
    print("3. Chilaquiles")
    print("4. Molletes")

def menu_comida_corrida():
    print("Comida corrida desde $80 pesos.")
    print("Incluye: agua, sopa, guisado con dos guarniciones y postre 😋.")
    print("1. Entradas:")
    print("   a. Sopa de fideo")
    print("   b. Sopa de verdura")
    print("2. Guisados:")
    print("   a. Bistec en salsa verde")
    print("   b. Pollo a la jardinera")
    print("   c. Mixiotes de pollo")
    print("   d. Mole rojo")
    print("   e. Enmoladas (90)")
    print("   f. Enchiladas rojas y verdes (90)")
    print("   g. Chiles rellenos")
    print("   h. Huanzontles en caldillo")
    print("   i. Tortas de papa")
    print("   j. Tortitas de plátano")
    print("3. Guarniciones:")
    print("   a. Arroz")
    print("   b. Frijoles")
    print("   c. Espagueti")
    print("   d. Ensalada")

def menu_a_la_carta():
    print("A la carta: ($120)")
    print("1. Cecina de Yecapixtla")
    print("2. Milanesa de res")
    print("3. Milanesa de pollo")
    print("4. Pechuga asada")
    print("5. Filete de pescado")
    print("(acompañado de arroz o espagueti, ensalada y agua)")

def obtener_precio_menu(opcion_menu, opcion_elegida):
    if opcion_menu == '1':
        precios = {'1': 70, '2': 70, '3': 70, '4': 70}
    elif opcion_menu == '2':
        precios = {'a': 80, 'b': 80, 'c': 80, 'd': 80, 'e': 90, 'f': 90, 'g': 90, 'h': 90, 'i': 90, 'j': 90}
    elif opcion_menu == '3':
        precios = {'1': 120, '2': 120, '3': 120, '4': 120, '5': 120}
    return precios[opcion_elegida]

def obtener_descripcion(opcion_menu, opcion_elegida):
    descripcion = ""
    if opcion_menu == '1':
        entradas = {'1': 'Huevos al gusto', '2': 'Omelettes', '3': 'Chilaquiles', '4': 'Molletes'}
        descripcion = entradas[opcion_elegida]
    elif opcion_menu == '2':
        guisados = {
            'a': 'Bistec en salsa verde', 'b': 'Pollo a la jardinera', 'c': 'Mixiotes de pollo',
            'd': 'Mole rojo', 'e': 'Enmoladas', 'f': 'Enchiladas rojas y verdes',
            'g': 'Chiles rellenos', 'h': 'Huanzontles en caldillo', 'i': 'Tortas de papa',
            'j': 'Tortitas de plátano'
        }
        descripcion = guisados[opcion_elegida]
    elif opcion_menu == '3':
        guarniciones = {
            '1': 'Arroz', '2': 'Frijoles', '3': 'Espagueti', '4': 'Ensalada'
        }
        descripcion = guarniciones[opcion_elegida]
    return descripcion

def obtener_pedido(opcion_menu, opcion_elegida_entrada, opcion_elegida_guisado, opcion_elegida_guarnicion_1, opcion_elegida_guarnicion_2):
    descripcion_entrada = obtener_descripcion(opcion_menu, opcion_elegida_entrada)
    descripcion_guisado = obtener_descripcion(opcion_menu, opcion_elegida_guisado)
    descripcion_guarnicion_1 = obtener_descripcion(opcion_menu, opcion_elegida_guarnicion_1)
    descripcion_guarnicion_2 = obtener_descripcion(opcion_menu, opcion_elegida_guarnicion_2)

    precio_entrada = obtener_precio_menu(opcion_menu, opcion_elegida_entrada)
    precio_guisado = obtener_precio_menu(opcion_menu, opcion_elegida_guisado)
    precio_guarnicion_1 = obtener_precio_menu(opcion_menu, opcion_elegida_guarnicion_1)
    precio_guarnicion_2 = obtener_precio_menu(opcion_menu, opcion_elegida_guarnicion_2)
    
    subtotal = precio_entrada + precio_guisado + precio_guarnicion_1 + precio_guarnicion_2
    pedido = {
        "Entrada": f"{opcion_elegida_entrada}. {descripcion_entrada}",
        "Guisado": f"{opcion_elegida_guisado}. {descripcion_guisado}",
        "Guarnición 1": f"{opcion_elegida_guarnicion_1}. {descripcion_guarnicion_1}",
        "Guarnición 2": f"{opcion_elegida_guarnicion_2}. {descripcion_guarnicion_2}",
        "Subtotal": subtotal
    }
    return pedido

def mostrar_pedido(pedido):
    print("\nTu pedido es:")
    for item, valor in pedido.items():
        print(f"{item}: {valor}")

@app.post("/procesar_pedido", response_class=HTMLResponse)
async def procesar_pedido(request: Request, opcion_menu: str = Form(...), opcion_elegida_entrada: str = Form(...), opcion_elegida_guisado: str = Form(...), opcion_elegida_guarnicion_1: str = Form(...), opcion_elegida_guarnicion_2: str = Form(...)):
    pedidos = []
    # Manejar el formulario y procesar el pedido
    if opcion_menu == "1":
        menu_desayuno()
        cantidad_platos = int(input("Ingresa la cantidad de platos que deseas: "))
        precio_plato = obtener_precio_menu(opcion_menu, opcion_elegida_entrada)
        total = precio_plato * cantidad_platos
        pedidos.append((f"{cantidad_platos} x {opcion_elegida_entrada}. {obtener_descripcion(opcion_menu, opcion_elegida_entrada)}", total))
    elif opcion_menu == "2":
        menu_comida_corrida()
        pedido = obtener_pedido(opcion_menu, opcion_elegida_entrada, opcion_elegida_guisado, opcion_elegida_guarnicion_1, opcion_elegida_guarnicion_2)
        mostrar_pedido(pedido)
        subtotal = pedido["Subtotal"]
        pedidos.append(("Comida corrida", subtotal))
    elif opcion_menu == "3":
        menu_a_la_carta()
        cantidad_platos = int(input("Ingresa la cantidad de platos que deseas: "))
        precio_plato = obtener_precio_menu(opcion_menu, opcion_elegida_entrada)
        total = precio_plato * cantidad_platos
        pedidos.append((f"{cantidad_platos} x {opcion_elegida_entrada}. {obtener_descripcion(opcion_menu, opcion_elegida_entrada)}", total))
    
    # Mostrar resumen total de pedidos
    total_pedido = 0
    for pedido, precio in pedidos:
        total_pedido += precio
    
    # Construir y retornar respuesta HTML
    with open("pedido.html", "r") as f:
        html_content = f.read()
    html_content = html_content.replace("{total_pedido}", str(total_pedido))
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/", response_class=HTMLResponse)
async def read_html():
    # Lee el contenido del archivo HTML
    with open("index.html", "r") as f:
        html_content = f.read()
    # Devuelve el contenido HTML como respuesta
    return html_content

