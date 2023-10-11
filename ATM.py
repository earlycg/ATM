#- 1 conzultar saldo - 2 depositar saldo - 3 retirar saldo - 4 salir

saldo = 10000

print("\n Welcome to BanColombia \n\n elija el numero acorde a su operación \n\n \t .:Menu:. \n \n 1 = Para conzultar saldo \n 2 = Para depositar dinero \n 3 = Para retirar saldo \n 4 = Para Salir")
print()
operacion = int(input("Digite una opción por su numero correspondiente: "))




if operacion == 1:
    print(f"Su saldo actual es de ${saldo} Cop")
    print()
elif operacion == 2:
    print(f"su saldo actual es de ${saldo} Cop." )
    deposito = float(input("cuanto dinero desea ingrezar?:$ "))
    print(f"Usted deposito ${deposito} Cop.")
    saldo += deposito
    print(f"Su saldo actual es de ${saldo} Cop.")
    print()
elif operacion == 3:
    print(f"su saldo actual es de ${saldo} Cop." )
    retirar = float(input("ingrese la cantidad a retirar:$ "))
    print(retirar)
    if retirar > saldo:
        print("No tienes esa cantidad de dinero \n intente ingrezar un valor correto")
    else:
        print(f"Usted retiro ${retirar} Cop.")
        saldo -= retirar
        print(f"Su saldo actual es de ${saldo} Cop. \n Gracias!")
        print()
elif operacion == 4:
    print("Gracias por usar nuestro Servicio, Regrese pronto")

else:
    print("Error de operacion \n intente de nuevo por favor.")