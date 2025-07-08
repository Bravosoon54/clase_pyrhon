import json
try:
    with open('contactos.json', 'r') as archivo:
        contactos = json.load(archivo)
except FileNotFoundError:
    contactos = {
        "Ana": {"telefono": "3121234567", "correo": "ana@gmail.com "},
        "Pedro": {"telefono": "3109876543", "correo": "pedro@hotmail.com"},
    }
print("Bienvenido a la agenda de contactos")
while True:
    print("\n1. Ver todos los contactos")
    print("2. Buscar contacto")
    print("3. Agregar nuevo contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    
    opcion = input("Ingrese la opción: ")
    
    if opcion == "1":
        if contactos:
            print("\nContactos:")
            for nombre, datos in contactos.items():
                print(f"{nombre}: {datos['telefono']} - {datos['correo']}")
        else:
            print("\nNo hay contactos")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto: ")
        if nombre in contactos:
            print(f"\nContacto encontrado: {nombre}")
            print(f"Telefono: {contactos[nombre]['telefono']}")
            print(f"Correo: {contactos[nombre]['correo']}")
        else:
            print("\nContacto no encontrado")
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        correo = input("Ingrese el correo del contacto: ")
        if nombre in contactos:
            print("\nEl nombre ya existe. Por favor, ingrese otro nombre.")
        else:
            contactos[nombre] = {'nombre': nombre, 'telefono': telefono, 'correo': correo}
            print("\nContacto agregado con éxito")
    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto a eliminar: ").lower()
        if nombre in contactos:
            del contactos[nombre]
            print("\nContacto eliminado con éxito")
        else:
            print("\nNo existe el contacto")
    elif opcion == "5":
        with open('contactos.json', 'w') as archivo:
            json.dump(contactos, archivo)
            break
    else:
        print("\nOpción inválida. Por favor, ingrese una opción válida.")