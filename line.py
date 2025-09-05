def line():
    A = float(input("Ingerese el coeficiente A:"))
    B = float(input("Ingerese el coeficiente B:"))
    X1 = float(input("Ingrese el coeficiente x1:"))
    X2 = float(input("Ingrese el coeficiente x2:"))

    print("El coeficiente A de su ecuacion de la recta es:", A )
    print("El coeficiente B de su ecuacion de la recta es:", B )
    print("El coeficiente x1 de su ecuacion de la recta es:", X1)
    print("El coeficiente x2 de su ecuacion de la recta es:", X2)
    print("")

    print("Para la siguiente ecuación:")
    print( f"\tY = {A}X + {B}")
    print("")

    y1 = A * X1 + B
    y2 = A * X2 + B

    print("Dados los siguientes puntos:")
    print( f"\tP1 ({X1}, {y1})")
    print( f"\tP2 ({X2}, {y2})")
    print("")

    distancia = ((float(X2) - float(X1))**2 + (y2 - y1)**2)**0.5

    print("La distancia entre ellos es:", distancia)
line()