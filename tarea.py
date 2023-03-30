# Función que muestra el menú principal
def menu_principal():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Empleados")
    print("2. Clientes")
    print("3. Trabajos")
    print("4. Salir")
    opcion = input("Ingrese una opción: ")
    return opcion

# Programa principal
opcion = ""
while opcion != "4":
    opcion = menu_principal()
    if opcion == "1":
        print("Opción 1: Empleados")
        # Función que muestra el submenú de empleados
def menu_empleados():
    empleados = []
    while True:
        print("=== MENÚ DE EMPLEADOS ===")
        print("1. Ingresar empleado")
        print("2. Borrar empleado")
        print("3. Mostrar empleados")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            # Opción para ingresar un nuevo empleado
            nombre = input("Ingrese el nombre del empleado: ")
            ocupacion = input("Ingrese la ocupación del empleado: ")
            sexo = input("Ingrese el sexo del empleado: ")
            empleado = {"nombre": nombre, "ocupacion": ocupacion, "sexo": sexo}
            empleados.append(empleado)
            print("Empleado ingresado correctamente.")
        elif opcion == "2":
            # Opción para borrar un empleado
            if len(empleados) == 0:
                print("No hay empleados para borrar.")
            else:
                nombre = input("Ingrese el nombre del empleado a borrar: ")
                encontrado = False
                for empleado in empleados:
                    if empleado["nombre"] == nombre:
                        empleados.remove(empleado)
                        encontrado = True
                        print("Empleado borrado correctamente.")
                        break
                if not encontrado:
                    print("No se encontró el empleado.")
        elif opcion == "3":
            # Opción para mostrar los empleados guardados
            if len(empleados) == 0:
                print("No hay empleados para mostrar.")
            else:
                for empleado in empleados:
                    print(f"Nombre: {empleado['nombre']}")
                    print(f"Ocupación: {empleado['ocupacion']}")
                    print(f"Sexo: {empleado['sexo']}")
                    print("----------------------")
        elif opcion == "4":
            # Opción para salir del submenú de empleados
            print("Saliendo del menú de empleados...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

          elif opcion == "2":
        print("Opción 2: Clientes")
        # Función que muestra el submenú de clientes
def sub_menu_clientes(clientes):
    opcion = ""
    while opcion != "4":
        print("=== MENÚ DE CLIENTES ===")
        print("1. Ingresar cliente")
        print("2. Modificar cliente")
        print("3. Ver clientes")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            cedula = input("Ingrese la cédula del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            clientes.append({"nombre": nombre, "cedula": cedula, "telefono": telefono})
            print("Cliente ingresado correctamente.")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del cliente a modificar: ")
            encontrado = False
            for cliente in clientes:
                if cliente["nombre"] == nombre:
                    cedula = input("Ingrese la nueva cédula del cliente: ")
                    telefono = input("Ingrese el nuevo teléfono del cliente: ")
                    cliente["cedula"] = cedula
                    cliente["telefono"] = telefono
                    encontrado = True
                    print("Cliente modificado correctamente.")
                    break
            if not encontrado:
                print("Cliente no encontrado.")
        elif opcion == "3":
# Función que muestra el submenú de servicios
def sub_menu_servicios(servicios, empleados):
    opcion = ""
    while opcion != "4":
        print("=== MENÚ DE SERVICIOS ===")
        print("1. Brindar servicio")
        print("2. Ver servicios brindados")
        print("3. Empleados disponibles")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            fecha = input("Ingrese la fecha del servicio (DD/MM/AAAA): ")
            cliente = input("Ingrese el nombre del cliente: ")
            servicio = input("Ingrese el tipo de servicio brindado: ")
            print("Empleados disponibles:")
            for empleado in empleados:
                if empleado["disponible"]:
                    print(empleado["nombre"])
            empleado = input("Ingrese el nombre del empleado que brindará el servicio: ")
            encontrado = False
            for e in empleados:
                if e["nombre"] == empleado:
                    e["disponible"] = False
                    encontrado = True
                    break
            if encontrado:
                servicios.append({"fecha": fecha, "cliente": cliente, "servicio": servicio, "empleado": empleado})
                print("Servicio brindado correctamente.")
            else:
                print("Empleado no encontrado.")
        elif opcion == "2":
            if len(servicios) == 0:
                print("No hay servicios registrados.")
            else:
                print("Lista de servicios brindados:")
                for servicio in servicios:
                    print(f"Fecha: {servicio['fecha']}, Cliente: {servicio['cliente']}, Servicio: {servicio['servicio']}, Empleado: {servicio['empleado']}")
        elif opcion == "3":
            disponibles = [empleado["nombre"] for empleado in empleados if empleado["disponible"]]
            if len(disponibles) == 0:
                print("No hay empleados disponibles.")
            else:
                print("Empleados disponibles:")
                for empleado in disponibles:
                    print(empleado)
        elif opcion == "4":
            print("Volviendo al menú principal...")
        else:
            print("Opción inválida. Intente de nuevo.")

# Programa principal
empleados = []


    elif opcion == "4":
        print("Saliendo...")
    break
    else:
        print("Opción inválida. Intente de nuevo.")
