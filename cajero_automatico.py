print("Bienvenido al Cajero Automático:")
saldo_inicial = 100_000

while True:
    print("""1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
4. Salir""")
    opcion = int(input("Ingrese la opción que desea: "))
    if opcion == 1:
        print(f"Su saldo es: ${saldo_inicial}\n")
    elif opcion == 2:
        ingresar_dinero = float(input("Cuanto dinero va a ingresar? "))
        if ingresar_dinero > 0:
            saldo_inicial += ingresar_dinero
            print("Dinero ingresado con exito\n")
        else:
            print("No se pudo ingresar el dinero con exito\n")
    elif opcion == 3:
        retirar_dinero = float(input("Cuanto dinero va a retirar?"))
        if retirar_dinero > saldo_inicial or retirar_dinero <= 0:
            print("No se pudo retirar el dinero con exito\n")
        else:
            saldo_inicial -= retirar_dinero
            print("Dinero retirado con exito\n")
    elif opcion == 4:
        print("Saliendo del cajero automático. ¡Hasta luego!")
        break
    else:
        print("Opcion no válida\n")






