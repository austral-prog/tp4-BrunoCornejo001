def line():
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    x1 = float(input("Ingrese el coeficiente X1: "))
    x2 = float(input("Ingrese el coeficiente X2: "))

    print("El coeficiente A de su ecuación de la recta es:",A)
    print("El coeficiente B de su ecuación de la recta es:",B)
    print("El coeficiente X1 de su ecuación de la recta es:",x1)
    print("El coeficiente X2 de su ecuación de la recta es:",x2)
    print("")

    print("Para la siguiente ecuación:")
    print( f"\tY = {A}X + {B}")
    print("")

    y1 = A * x1 + B
    y2 = A * x2 + B

    print("Dados los siguientes puntos:")
    print( f"\tP1 ({x1}, {y1})")
    print( f"\tP2 ({x2}, {y2})")
    print("")

    distancia = ((float(x2) - float(x1))**2 + (y2 - y1)**2)**0.5

    print("La distancia entre ellos es:",distancia)
line() 
