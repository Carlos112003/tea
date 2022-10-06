try:
    nm = input("Ingrese el nombre del archivo\n>---")
    file = open(nm, "r", encoding="UTF-8")

    for linea in file:
        print(linea.upper())
except:
    print("Intente nuevamente")