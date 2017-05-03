def newton(f, df, x0, n=1000, tol_x=1e-6, tol_y=1e-6):
    """
    f: función a buscar raices. Objeto lambda.
    df: derivada de la función a buscar raices. Objeto lambda.
    x0: valor inicial para la busqueda.
    n: Número máximo de iteraciones. Si no se requiere usar n=float('inf')
    tol_x y tol_y: tolerancia permitida en ambos ejes. Si no se requiere tol=0.
    """
    cont = 0
    error_x = tol_x * 10 + 1
    error_y = tol_y * 10 + 1
    while (cont < n) and (tol_x < error_x) and (tol_y < error_y):
        x = x0 - f(x0) / df(x0)
        error_x = abs(x - x0)
        error_y = abs(f(x))
        x0 = x
        cont = cont + 1
    if (error_x <= tol_y) or (error_y <= tol_y):
        return x0
    else:
        return None


def punto_fijo(g, x0, n=1000, tol_x=1e-6):
    cont = 0
    error_x = abs(g(x0)) * 10 + 1
    while (cont < n) and (tol_x < error_x):
        x = g(x0)
        error_x = abs(x - x0)
        x0 = x
        cont = cont + 1
    if (error_x < tol_x):
        return x0
    else:
        return None
