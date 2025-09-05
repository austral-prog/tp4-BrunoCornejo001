def leap_year():
    anio = int(input("Ingrese un año: "))
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                print(f"El año {anio} es bisiesto")
            else:
                print(f"El año {anio} no es bisiesto")
        else:
            print(f"El año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")
