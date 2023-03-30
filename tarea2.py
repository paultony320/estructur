empleados = []

clientes = []

trabajos = []


#desplegamos un menu principal el cual segun la opcion elegida desplegara submenus que me permitiran guardar datos en las listas nombradas

def menu_principal():

    while True:



        print(" MENÚ PRINCIPAL Maridos de alquiler")

        print(  "   1. Empleados "   )

        print("    2. Clientes     ")

        print("     3. Trabajos     ")

        print("     4. Salir        ")

        print(" ---------------------")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":

            menu_empleados()

        elif opcion == "2":

            menu_clientes()

        elif opcion == "3":

            menu_trabajos()

        elif opcion == "4":

            print("Saliendo del programa..")

            break

        else:

            print("Opción inválida.")

            # Función para mostrar el menú de empleados

def menu_empleados():

    while True:

    #este sub menu me permitira guardar los empleados y me permitira ver los guardados y borrarlos

       

        print(" MENÚ DE EMPLEADOS ")

        print( " 1. Ingresar Empleado ")

        print(" 2. Borrar Empleado   ")

        print(" 3. Ver Empleados    ")

        print(" 4. Salir             ")


        opcion = input("Ingrese una Opción: ")

        if opcion == "1":

            ingresar_empleado()

        elif opcion == "2":

            borrar_empleado()

        elif opcion == "3":

            ver_empleados()

        elif opcion == "4":

            break

        else:

            print("Opción Inválida.")

 

# Funciones para el módulo de empleados

def ingresar_empleado():

    nombre = input("Ingrese el nombre del empleado: ")

    especialidad = input("Ingrese la especialidad del empleado: ")

    sexo = input("Ingrese el sexo del empleado: ")

    nuevo_empleado = {"nombre": nombre, "especialidad": especialidad, "sexo": sexo}

    if nuevo_empleado in empleados:

        print("Este empleado ya existe en la lista.")

    else:

        empleados.append(nuevo_empleado)

        print("Empleado Agregado con Éxito.")

 

def borrar_empleado():

    nombre = input("Ingrese el nombre del empleado que desea borrar: ")

    for empleado in empleados:

        if empleado["nombre"] == nombre:

            empleados.remove(empleado)

            print("Empleado Eliminado con Éxito.")

            return

    print("No se Encontró un Empleado con ese Nombre.")

 

def ver_empleados():

    if empleados:

        for empleado in empleados:

                print(f"Nombre: {empleado['nombre']}\nEspecialidad: {empleado['especialidad']}\nSexo: {empleado['sexo']}\n")

    else:

        print("No hay empleados en la lista.")

# Función para mostrar el menú de clientes

def menu_clientes():

    while True:

  #este sub menu me permitira guardar los clientes en una lista ver los guardados y modificarlos

        print("******* MENÚ DE CLIENTES *******")


        print(" 1. Ingresar Cliente  ")

        print(" 2. Modificar Cliente ")

        print(" 3. Ver Clientes      ")

        print(" 4. Salir             ")

       

        opcion = input("Ingrese una opción: ")

        if opcion == "1":

            ingresar_cliente()

        elif opcion == "2":

            modificar_cliente()

        elif opcion == "3":

            ver_clientes()

        elif opcion == "4":

            break

        else:

            print("Opción Inválida.")    

       

   

 

# Funciones para el módulo de clientes

def ingresar_cliente():

    nombre = input("Ingrese el Nombre del Cliente: ")

    apellido = input("Ingrese el Apellido del Cliente: ")

    cedula = input("Ingrese la Cédula del Cliente: ")

    telefono = input("Ingrese el Teléfono del Cliente: ")

    nuevo_cliente = {"nombre": nombre, "cedula": cedula, "telefono": telefono, "apellido": apellido,}

    for i, cliente in enumerate(clientes):

        if cliente["nombre"] > nombre:

            clientes.insert(i, nuevo_cliente)

            print("Cliente Agregado con Éxito.")

            return

    clientes.append(nuevo_cliente)

    print("Cliente Agregado con Éxito.")

 

def modificar_cliente():

    nombre = input("Ingrese el Nombre del Cliente que desea Modificar: ")

    for cliente in clientes:

        if cliente["nombre"] == nombre:

            cliente["cedula"] = input("Ingrese la nueva Cédula del Cliente: ")

            cliente["telefono"] = input("Ingrese el nuevo Teléfono del Cliente: ")

            print("Cliente modificado con éxito.")

            return

    print("No se Encontró un Cliente con ese Nombre.")

 

def ver_clientes():

    if clientes:

        for cliente in clientes:

            print(f"Nombre: {cliente['nombre']}\nCédula: {cliente['cedula']}\nTeléfono: {cliente['telefono']}\n")

    else:

        print("No hay Clientes en la Lista.")

        # Función para mostrar el menú de trabajos

def menu_trabajos():

    while True:

    #este sub menu nos permitira mostrar las opciones de los trabajos nos mostrara los empleados disponibles 

        print("******* MENÚ DE TRABAJOS *******")


        print(" 1. Brindar Servicio        ")

        print(" 2. Ver Servicios Brindados ")

        print(" 3. Empleado Disponible     ")

        print(" 4. Salir                   ")

       

        opcion = input("Ingrese una Opción: ")

        if opcion == "1":

            brindar_servicio()

        elif opcion == "2":

            ver_servicios_brindados()

        elif opcion == "3":

            empleado_disponible()

        elif opcion == "4":

            break

        else:

            print("Opción Inválida.")

 

# Funciones para el módulo de trabajos

def brindar_servicio():

    print("Brindar servicio:")

    cliente_nombre = input("Ingrese el Nombre del Cliente: ")

    servicio = input("Ingrese el Servicio a Brindar: ")

    fecha = input("Ingrese la Fecha del Trabajo (en formato dd/mm/yyyy): ")

    for cliente in clientes:

        if cliente["nombre"] == cliente_nombre:

            for empleado in empleados:

                if empleado["especialidad"] == servicio:

                    print(f"El Empleado {empleado['nombre']} Brindará el servicio al Cliente {cliente['nombre']} el {fecha}  .")

                    trabajos.append({"cliente": cliente, "empleado": empleado, "servicio": servicio, "fecha": fecha})

                    return

            print("No hay Empleados Disponibles para Brindar ese Servicio.")

            return

    print("No se Encontró un Cliente con ese Nombre.")

 

# Función para ver los servicios brindados

def ver_servicios_brindados():

    if trabajos:

        for trabajo in trabajos:

            print(f"Cliente: {trabajo['cliente']}\nServicio: {trabajo['servicio']}\nEmpleado: {trabajo['empleado']}\n")

    else:

        print("No hay Servicios Brindados.")





# Función para verificar si un empleado está disponible

def empleado_disponible():

    especialidad = input("Ingrese la Especialidad del Empleado que Busca: ")

    empleado_disponible = None

    for empleado in empleados:

        if empleado["especialidad"] == especialidad:

            ocupado = False

            for trabajo in trabajos:

                if trabajo["empleado"] == empleado["nombre"]:

                    ocupado = True

                    break

            if not ocupado:

                empleado_disponible = empleado["nombre"]

                break

               

    if empleado_disponible:

        print(f"El empleado {empleado_disponible} está disponible para trabajar en esa especialidad.")

    else:

        print("No se Encontró un Empleado con esa Especialidad o todos los Empleados están Ocupados.")

 

menu_principal()

empleados = []

clientes = []

trabajos = []

while True:

    print("Menú principal:")

 

    print(" Maridos de Alquiler ")

   

    print("1. Empleados")

    print("2. Clientes")

    print("3. Trabajos")

    print("4. Salir")

    opcion = input("Ingrese una Opción: ")

    if opcion == "1":

        menu_empleados()

    elif opcion == "2":

        menu_clientes()

    elif opcion == "3":

        menu_trabajos()

    elif opcion == "4":
       
       break
    else:
        print("opcion invalida")