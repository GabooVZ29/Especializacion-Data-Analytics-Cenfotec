contactos = [] # Lista vacía para guardar los diccionarios

while True:
    # Mostrar el menú y pedir la opción
    print("\n--- MENÚ ---")
    print("1. Ingresar | 2. Mostrar | 3. Salir")
    opcion = input("Seleccione una opción: ") 

    # --- 1. LÓGICA PARA INGRESAR CONTACTO (OPCIÓN 1) ---
    if opcion == '1':
        # 2. Pedir datos
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el telefono: ")
        ciudad = input("Ingrese la ciudad: ")
        
        # 3. Crear el diccionario
        contacto_nuevo = {
            "Nombre": nombre, 
            "Tel": telefono,
            "Ciudad": ciudad
        }
        
        # 4. Agregar a la lista
        contactos.append(contacto_nuevo)
        print("Contacto agregado con éxito.")
        
    # --- 2. LÓGICA PARA MOSTRAR CONTACTOS (OPCIÓN 2) ---
    elif opcion == '2':
        print("\n--- Lista de Contactos Ingresados ---")
        if not contactos:
            print("No hay contactos registrados aún.")
        else:
            # 5. Mostrar todos los contactos
            for contacto in contactos:
                print(f"Contacto: {contacto['Nombre']} | Tel: {contacto['Tel']} | Ciudad: {contacto['Ciudad']}")
        
    # --- 3. LÓGICA PARA SALIR (OPCIÓN 3) ---
    
    elif opcion == '3':
        print("\n¡Hasta luego!")
        break # Detiene el bucle 'while True'
        
    # --- MANEJO DE ERRORES ---
    else:
        print("Opción no válida. Inténtelo de nuevo.")