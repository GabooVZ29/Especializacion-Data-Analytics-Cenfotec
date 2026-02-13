# =========================================================
# 1. Definición de Funciones de Operación
# =========================================================

def sumar(a, b):
    """Realiza la operación de suma."""
    return a + b

def restar(a, b):
    """Realiza la operación de resta."""
    return a - b

def multiplicar(a, b):
    """Realiza la operación de multiplicación."""
    return a * b

def dividir(a, b):
    """
    Realiza la operación de división.
    Maneja el caso de división por cero.
    """
    if b == 0:
        return "Error: No se puede dividir por cero."
    else:
        return a / b

# =========================================================
# 2. Función Principal del Programa
# =========================================================

def calculadora_simple():
    """
    Función principal que implementa la calculadora
    usando un bucle while y estructuras condicionales.
    """
    print("✨ Iniciando Calculadora Simple de Consola ✨")

    # Bucle 'while True' para mantener el programa en ejecución
    while True:
        # Mostrar el Menú de Opciones
        print("\n--- Menú de Operaciones ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir del programa")
        print("---------------------------")

        # Solicitar la opción
        opcion = input("Seleccione una opción (1-5): ")

        # Estructura Condicional (if/elif/else)
        if opcion == '5':
            # Opción 5: Salir del programa
            print("\n👋 ¡Gracias por usar la calculadora! Programa finalizado.")
            break # Sale del bucle while

        elif opcion in ('1', '2', '3', '4'):
            try:
                # Pedir al usuario los dos números reales (decimales o enteros)
                num1 = float(input("Ingrese el primer número real: "))
                num2 = float(input("Ingrese el segundo número real: "))

                resultado = None 

                # Ejecutar la operación correspondiente
                if opcion == '1':
                    resultado = sumar(num1, num2)
                elif opcion == '2':
                    resultado = restar(num1, num2)
                elif opcion == '3':
                    resultado = multiplicar(num1, num2)
                elif opcion == '4':
                    resultado = dividir(num1, num2)

                # Mostrar el resultado por pantalla
                print(f"\n✅ El resultado es: {resultado}")

            except ValueError:
                # Maneja el caso en que el usuario no ingresa un número válido
                print("\n❌ Error: Entrada no válida. Por favor, ingrese solo números reales.")

        else:
            # Opción inválida
            print("\n⚠️ Opción no válida. Por favor, seleccione un número del 1 al 5.")

# =========================================================
# Punto de Inicio de Ejecución
# =========================================================

if __name__ == "__main__":
    calculadora_simple()