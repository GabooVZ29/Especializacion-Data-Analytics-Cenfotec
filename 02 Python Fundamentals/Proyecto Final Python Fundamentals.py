import csv
import os

# --- 1. MANEJO DE ARCHIVOS CSV ---

def cargar_inventario(nombre_archivo="inventario.csv"):
    """Carga los productos desde el archivo CSV al inicio."""
    inventario = []
    
    # Si el archivo no existe, no hay nada que cargar.
    if not os.path.exists(nombre_archivo):
        return inventario
        
    try:
        with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for fila in reader:
                # Convertir a tipos numéricos, ya que el CSV guarda todo como texto
                try:
                    fila['cantidad'] = int(fila['cantidad'])
                    fila['precio'] = float(fila['precio'])
                    inventario.append(fila)
                except ValueError:
                    print(f"Error de formato en la fila: {fila['nombre']}. Omitiendo.")
                    
    except Exception as e:
        print(f"Error crítico al cargar el archivo: {e}")
        
    return inventario

def guardar_inventario(inventario, nombre_archivo="inventario.csv"):
    """Guarda el inventario actual en el archivo CSV."""
    campos = ["nombre", "cantidad", "precio", "codigo"]
    
    try:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=campos)
            writer.writeheader() # Escribe los encabezados (nombre, cantidad, etc.)
            writer.writerows(inventario) # Escribe todos los productos
        print("\n Inventario guardado exitosamente en inventario.csv.")
    except Exception as e:
        print(f" Error al guardar el archivo: {e}")

# --- 2. OPERACIONES DEL INVENTARIO ---

def registrar_producto(inventario):
    """Permite al usuario ingresar los datos de un nuevo producto (forma libre)."""
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")
    
    nombre = input("Nombre: ")
    codigo = input("Código (debe ser único): ")
    
    # Validar código único
    if any(p['codigo'] == codigo for p in inventario):
        print("Error: Ya existe un producto con ese código.")
        return

    # Validar Cantidad
    while True:
        try:
            cantidad = int(input("Cantidad (stock): "))
            if cantidad < 0: raise ValueError
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero positivo para la cantidad.")

    # Validar Precio
    while True:
        try:
            precio = float(input("Precio: "))
            if precio < 0: raise ValueError
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número positivo para el precio.")
            
    # Crea la estructura de datos y lo añade a la lista
    nuevo_producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio,
        "codigo": codigo
    }
    inventario.append(nuevo_producto)
    print(f" Producto '{nombre}' registrado con éxito.")

def consultar_inventario(inventario):
    """Muestra todos los productos en formato de tabla."""
    if not inventario:
        print("\n⚠️ El inventario está vacío. Use la opción 1 para registrar productos.")
        return
        
    print("\n--- INVENTARIO ACTUAL ---")
    print("-" * 55)
    print(f"{'Código':<10} {'Nombre':<20} {'Cantidad':<10} {'Precio':<10}")
    print("-" * 55)
    
    # Recuenta sobre la lista e imprime cada diccionario de forma ordenada
    for producto in inventario:
        print(f"{producto['codigo']:<10} {producto['nombre']:<20} {producto['cantidad']:<10} ${producto['precio']:<9.2f}")
    print("-" * 55)

def modificar_stock(inventario):
    """Busca un producto por código y actualiza su cantidad."""
    print("\n--- MODIFICAR STOCK ---")
    codigo_buscar = input("Ingrese el CÓDIGO del producto a modificar: ")
    
    # Encuentra el diccionario del producto usando su código
    producto_encontrado = next((p for p in inventario if p['codigo'] == codigo_buscar), None)
    
    if producto_encontrado:
        print(f"Producto: {producto_encontrado['nombre']} | Stock actual: {producto_encontrado['cantidad']}")
        
        while True:
            try:
                nueva_cantidad = int(input("Ingrese la NUEVA cantidad (stock): "))
                if nueva_cantidad < 0: raise ValueError
                break
            except ValueError:
                print("Entrada inválida. Ingrese un número entero positivo.")
                
        # Actualiza el valor en el diccionario de la lista
        producto_encontrado['cantidad'] = nueva_cantidad
        print(f"Stock de '{producto_encontrado['nombre']}' actualizado a {nueva_cantidad}.")
    else:
        print(f"Error: Producto con código '{codigo_buscar}' no encontrado.")

# --- 3. CICLO PRINCIPAL (MAIN) ---

def main():
    # Carga los datos guardados, si existen. Si no, empieza con una lista vacía.
    inventario = cargar_inventario()
    print("====================================")
    print(" SISTEMA DE INVENTARIO (PROYECTO FINAL)")
    print("====================================")
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar Nuevo Producto")
        print("2. Consultar Inventario")
        print("3. Modificar Stock")
        print("4. Guardar y Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            registrar_producto(inventario)
        elif opcion == '2':
            consultar_inventario(inventario)
        elif opcion == '3':
            modificar_stock(inventario)
        elif opcion == '4':
            # La única opción que guarda los cambios antes de terminar
            guardar_inventario(inventario)
            print("¡Aplicación finalizada! 👋")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecutar el programa principal al correr el script
if __name__ == "__main__":
    main()