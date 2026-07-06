usuarios = {
    "admin": {
        "contrasena": "1234",
        "saldo": 100000.0
    },
    "juan": {
        "contrasena": "4321",
        "saldo": 75000.0
    },
    "maria": {
        "contrasena": "1111",
        "saldo": 120000.0
    }
}

limite_extraccion = 50000.0
operaciones = []

cantidad_consultas = 0
cantidad_extracciones = 0
cantidad_depositos = 0
cantidad_transferencias = 0
total_extraido = 0.0
total_depositado = 0.0
total_transferido = 0.0


def mostrar_bienvenida():
    print("====================================")
    print("        CAJERO AUTOMATICO")
    print("====================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))
            return opcion
        except ValueError:
            print("Error: debe ingresar un numero de opcion valido.")


def leer_monto(mensaje):
    while True:
        try:
            monto = float(input(mensaje))

            if monto <= 0:
                print("Error: el monto debe ser mayor a cero.")
            else:
                return monto

        except ValueError:
            print("Error: debe ingresar un monto numerico valido.")


def iniciar_sesion():
    intentos = 3

    while intentos > 0:
        usuario = input("Ingrese usuario: ")
        contrasena = input("Ingrese contrasena: ")

        if usuario in usuarios and usuarios[usuario]["contrasena"] == contrasena:
            print("Acceso correcto. Bienvenido,", usuario)
            return usuario

        intentos -= 1
        print("Usuario o contrasena incorrectos.")
        print("Intentos restantes:", intentos)

    print("Acceso bloqueado por superar la cantidad de intentos.")
    return None


def mostrar_menu():
    print("\n---------- MENU PRINCIPAL ----------")
    print("1. Consultar saldo")
    print("2. Extraer dinero")
    print("3. Depositar dinero")
    print("4. Transferir dinero")
    print("5. Ver operaciones realizadas")
    print("6. Ver estadisticas")
    print("7. Salir")


def registrar_operacion(texto):
    operaciones.append(texto)


def consultar_saldo(usuario):
    global cantidad_consultas

    saldo = usuarios[usuario]["saldo"]
    print("Saldo actual: $", round(saldo, 2))

    cantidad_consultas += 1
    registrar_operacion("Consulta de saldo. Saldo: $" + str(round(saldo, 2)))


def extraer_dinero(usuario):
    global cantidad_extracciones
    global total_extraido

    monto = leer_monto("Ingrese monto a extraer: ")
    saldo = usuarios[usuario]["saldo"]

    if monto > limite_extraccion:
        print("Error: no puede extraer mas de $", round(limite_extraccion, 2), "por operacion.")
    elif monto > saldo:
        print("Error: saldo insuficiente.")
    else:
        usuarios[usuario]["saldo"] -= monto
        cantidad_extracciones += 1
        total_extraido += monto

        print("Extraccion realizada correctamente.")
        print("Saldo actual: $", round(usuarios[usuario]["saldo"], 2))
        registrar_operacion("Extraccion de $" + str(round(monto, 2)))


def depositar_dinero(usuario):
    global cantidad_depositos
    global total_depositado

    monto = leer_monto("Ingrese monto a depositar: ")

    usuarios[usuario]["saldo"] += monto
    cantidad_depositos += 1
    total_depositado += monto

    print("Deposito realizado correctamente.")
    print("Saldo actual: $", round(usuarios[usuario]["saldo"], 2))
    registrar_operacion("Deposito de $" + str(round(monto, 2)))


def transferir_dinero(usuario):
    global cantidad_transferencias
    global total_transferido

    cuenta_destino = input("Ingrese usuario destino: ")

    if cuenta_destino not in usuarios:
        print("Error: la cuenta destino no existe.")
        return

    if cuenta_destino == usuario:
        print("Error: no puede transferirse dinero a la misma cuenta.")
        return

    monto = leer_monto("Ingrese monto a transferir: ")

    if monto > usuarios[usuario]["saldo"]:
        print("Error: saldo insuficiente.")
    else:
        usuarios[usuario]["saldo"] -= monto
        usuarios[cuenta_destino]["saldo"] += monto
        cantidad_transferencias += 1
        total_transferido += monto

        print("Transferencia realizada correctamente a", cuenta_destino)
        print("Saldo actual: $", round(usuarios[usuario]["saldo"], 2))
        registrar_operacion("Transferencia de $" + str(round(monto, 2)) + " a " + cuenta_destino)


def ver_operaciones():
    print("\n------ OPERACIONES REALIZADAS ------")

    if len(operaciones) == 0:
        print("No se realizaron operaciones.")
    else:
        for posicion in range(len(operaciones)):
            print(posicion + 1, "-", operaciones[posicion])


def ver_estadisticas():
    total_operaciones = (
        cantidad_consultas
        + cantidad_extracciones
        + cantidad_depositos
        + cantidad_transferencias
    )

    print("\n----------- ESTADISTICAS -----------")
    print("Total de operaciones:", total_operaciones)
    print("Consultas de saldo:", cantidad_consultas)
    print("Extracciones realizadas:", cantidad_extracciones)
    print("Depositos realizados:", cantidad_depositos)
    print("Transferencias realizadas:", cantidad_transferencias)
    print("Total extraido: $", round(total_extraido, 2))
    print("Total depositado: $", round(total_depositado, 2))
    print("Total transferido: $", round(total_transferido, 2))


def ejecutar_cajero(usuario):
    salir = False

    while not salir:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            consultar_saldo(usuario)
        elif opcion == 2:
            extraer_dinero(usuario)
        elif opcion == 3:
            depositar_dinero(usuario)
        elif opcion == 4:
            transferir_dinero(usuario)
        elif opcion == 5:
            ver_operaciones()
        elif opcion == 6:
            ver_estadisticas()
        elif opcion == 7:
            print("Gracias por utilizar el cajero automatico.")
            salir = True
        else:
            print("Opcion incorrecta. Intente nuevamente.")


def main():
    mostrar_bienvenida()
    usuario = iniciar_sesion()

    if usuario is not None:
        ejecutar_cajero(usuario)


main()
