def mostrar_menu():
    print("=== Calculadora Básica ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingresa un número válido.")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == "5":
            print("Gracias por usar la calculadora.")
            break

        # Pedimos dos números al usuario
        num1 = pedir_numero("Ingresa el primer número: ")
        num2 = pedir_numero("Ingresa el segundo número: ")

        if opcion == "1":
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif opcion == "2":
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif opcion == "3":
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif opcion == "4":
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
            else:
                print("Error: No se puede dividir por cero.")
        else:
            print("Opción no válida. Intenta otra vez.")

# asdad
        print()
calculadora()