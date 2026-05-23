nombre = "Waflle"
energia = 100
felicidad = 100
print(f"Energia Inicial de: {nombre}, energia: {energia}, felicidad: {felicidad}")
while energia >0: 
    print("¿Que quieres hacer:?")
    print("1.- Alimentar")
    print("2.- Jugar")
    print("3.- Ver estado de salud")
    print("4.- No hacer nada")
    opcion = input("Seleccione:")
    if opcion == "1":
        energia = energia +20
        felicidad = felicidad+1
        print(f"Alimentaste a {nombre}, esta muy feliz de jugar  contigo..")
    elif opcion == "2":
        energia = energia -15
        felicidad = felicidad+20
    elif opcion == "3":
        print("     /\_                   /\_/\  ")
        print("   (    @\__              ( o.o ) ")
        print("   /        o               >*<   ")
        print("  /     (___/                     ")
        print(" /_____/                          ")
        print(f"Energia: {energia}")
        print(f"Felicidad: {felicidad}")
    elif opcion == "4":
        felicidad = felicidad -10
        energia = energia -5
        print(f"{nombre} esta muy aburrido....")
    else:
        print("error de ingreso")
