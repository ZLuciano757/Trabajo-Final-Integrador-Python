usuario_correcto = "admin"
contrasena_correcta = "1234"

saldo = 100000
limite_extraccion = 50000
operaciones = []

usuario = input("Ingrese usuario: ")
contrasena = input("Ingrese contraseña: ")

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    opcion = 0

    while opcion != 5:
        print("\n--- CAJERO AUTOMATICO ---")
        print("1. Consultar saldo")
        print("2. Extraer dinero")
        print("3. Depositar dinero")
        print("4. Transferir dinero")
        print("5. Salir")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            print("Saldo actual: $", saldo)
            operaciones.append("Consulta de saldo")

        elif opcion == 2:
            monto = float(input("Ingrese monto a extraer: "))

            if monto <= 0:
                print("El monto debe ser mayor a cero.")
            elif monto > limite_extraccion:
                print("El monto supera el limite de extraccion.")
            elif monto > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= monto
                print("Extraccion exitosa.")
                print("Saldo actual: $", saldo)
                operaciones.append("Extraccion de $" + str(monto))

        elif opcion == 3:
            monto = float(input("Ingrese monto a depositar: "))

            if monto <= 0:
                print("El monto debe ser mayor a cero.")
            else:
                saldo += monto
                print("Deposito exitoso.")
                print("Saldo actual: $", saldo)
                operaciones.append("Deposito de $" + str(monto))

        elif opcion == 4:
            cuenta_destino = input("Ingrese cuenta destino: ")
            monto = float(input("Ingrese monto a transferir: "))

            if monto <= 0:
                print("El monto debe ser mayor a cero.")
            elif monto > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= monto
                print("Transferencia exitosa a la cuenta", cuenta_destino)
                print("Saldo actual: $", saldo)
                operaciones.append("Transferencia de $" + str(monto) + " a cuenta " + cuenta_destino)

        elif opcion == 5:
            print("\nGracias por utilizar el cajero.")
            print("\n--- OPERACIONES REALIZADAS ---")

            if len(operaciones) == 0:
                print("No se realizaron operaciones.")
            else:
                for operacion in operaciones:
                    print("-", operacion)

        else:
            print("Opcion incorrecta.")

else:
    print("Usuario o contraseña incorrectos.")
