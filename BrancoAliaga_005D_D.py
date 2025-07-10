import os

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
            '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
            'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
            'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
            '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
            '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
}

modelo = {
    "HP": ["8475HD", "fgdxFHD"] 
}

acer = 4 + 32 + 7
hp = 10 + 21
asus = 1 + 2
dell = 1

menu = {
    1: "Stock marca",
    2: "Búsqueda por RAM y precio",
    3: "Eliminar producto",
    4: "Salir"
}

marcas = []
ram_min = 4
ram_max = 16
precio = 0

def stock_marca(marcas):
    i = 1
    print(" // MARCAS DISPONIBLES // ")
    for codigo, datos in productos.items():
        if datos[0] not in marcas:
            marcas.append(datos[0])
    for marca in marcas: 
        print(f"{i}. - {marca}")

        i += 1
    
    while True:
        try: 
            seleccion_marca = int(input(" - Seleccione la marca para consultar el stock (1, 2, 3 o 4, 0 para salir): "))
            if seleccion_marca == 1:
                print(f"HP = {hp}")
            elif seleccion_marca == 2:
                print(f"Acer = {acer}")
            elif seleccion_marca == 3:
                print(f"Asus = {asus}")
            elif seleccion_marca == 4:
                print(f"Dell = {dell}")
            elif seleccion_marca == 0:
                break
            else:
                print(" - Esta marca no existe")
        except ValueError:
            print(" - Entrada inválida")

def busqueda_ram_precio(ram_min, ram_max, precio):
    pass

eliminar_modelo = []        

def eliminar_producto(modelo):
    for modelo[0] in productos.items():
        if modelo[0] not in eliminar_modelo:
            eliminar_modelo.append(modelo[0])
    for codigo in eliminar_modelo:
        print(f"{codigo}")

    borrar_codigo = input(" - Insertar código del producto a borrar: ")
    if borrar_codigo in eliminar_modelo:
        del eliminar_modelo[borrar_codigo]
    else:
        print(" - Ese código no existe.")

def mostrar_menu():
    print(" *** MENÚ PRINCIPAL *** ")
    for codigo, datos in menu.items():
        print(f"{codigo}. {datos}")

def verificacion_menu():
    while True:
        try:
            seleccion = int(input(" - Seleccione una opción: "))
            if seleccion in menu:
                return seleccion
            else:
                print(" - Error. Intente otra vez.")
        except ValueError:
            print(" - Entrada inválida.")
    
while True:
    mostrar_menu()
    seleccion = verificacion_menu()

    if seleccion == 1:
        stock_marca(marcas)
    elif seleccion == 2:
        busqueda_ram_precio(ram_min, ram_max, precio)
    elif seleccion == 3:
        eliminar_producto(modelo)
    elif seleccion == 4:
        exit()

