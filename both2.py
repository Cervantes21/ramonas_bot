import os

class Calculator():
    a = 0
    b = 0

    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def sumar(self):
        suma = self.a + self.b
        return suma

    def restar(self):
        resta = self.a - self.b
        return resta

    def multiplicar(self):
        multiplicacion = self.a * self.b
        return multiplicacion

    def dividir(self):
        if self.b != 0:
            division = self.a / self.b
            return division
        else:
            return "No se puede dividir entre 0"

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

if __name__ == '__main__':
    pedidos = []  # Almacena todos los pedidos
    while True:
        print("Opciones:")
        print("1: Desayuno")
        print("2: Comida corrida")
        print("3: Menú a la carta")
        opcion_menu = input("¿Qué deseas ordenar? (1/2/3): ")
        os.system('clear')

        if opcion_menu == "1":
            menu_desayuno()
            opcion_elegida = input("Elige una opción del menú: ")
            cantidad_platos = int(input("Ingresa la cantidad de platos que deseas: "))
            precio_plato = obtener_precio_menu(opcion_menu, opcion_elegida)
            total = precio_plato * cantidad_platos
            print(f"\nTu pedido es: {opcion_elegida}. {obtener_descripcion(opcion_menu, opcion_elegida)} x{cantidad_platos}, Total: ${total}")
            pedidos.append((f"{cantidad_platos} x {opcion_elegida}. {obtener_descripcion(opcion_menu, opcion_elegida)}", total))  # Añadir pedido a la lista

        elif opcion_menu == "2":
            menu_comida_corrida()
            opcion_elegida_entrada = input("Elige una opción de entrada: ")
            opcion_elegida_guisado = input("Elige una opción de guisado: ")
            opcion_elegida_guarnicion_1 = input("Elige una primera opción de guarnición: ")
            opcion_elegida_guarnicion_2 = input("Elige una segunda opción de guarnición: ")

            pedido = obtener_pedido(opcion_menu, opcion_elegida_entrada, opcion_elegida_guisado, opcion_elegida_guarnicion_1, opcion_elegida_guarnicion_2)
            mostrar_pedido(pedido)

            subtotal = pedido["Subtotal"]
            pedidos.append(("Comida corrida", subtotal))  # Añadir pedido a la lista

        elif opcion_menu == "3":
            menu_a_la_carta()
            opcion_elegida = input("Elige una opción del menú: ")
            cantidad_platos = int(input("Ingresa la cantidad de platos que deseas: "))
            precio_plato = obtener_precio_menu(opcion_menu, opcion_elegida)
            total = precio_plato * cantidad_platos
            print(f"\nTu pedido es: {opcion_elegida}. {obtener_descripcion(opcion_menu, opcion_elegida)} x{cantidad_platos}, Total: ${total}")
            pedidos.append((f"{cantidad_platos} x {opcion_elegida}. {obtener_descripcion(opcion_menu, opcion_elegida)}", total))  # Añadir pedido a la lista
        
        else:
            print("Opción no válida.")
            continue

        continuar = input("\n¿Deseas realizar otro pedido? (s/n): ")
        if continuar.lower() != 's':
            break

    # Mostrar resumen total de pedidos
    print("\nPedido total:\n")
    total_pedido = 0
    for pedido, precio in pedidos:
        print(f"{pedido}: ${precio}")
        total_pedido += precio
    print(f"\nTotal: ${total_pedido:.2f}")

    eliminar = input("\n¿Eliminar producto (s/n)? ")
    if eliminar.lower() == 's':
        print("Funcionalidad de eliminar productos aún no implementada.")

    direccion = input("\nPor favor, ingresa la dirección de entrega: ")
    print(f"\n¡Tu pedido será enviado a la dirección: {direccion}!")

