def biseccion(f, a, b, n, tol_x, tol_y):
    """
    f: función
    a: valor inicial del intervalo
    b: valor final del intervalo
    n: número total de iteraciones
    tol: tolerancia permitida (error máximo)

    Si el problema no tiene tolerancia se indica tol=0.
    Si el problema no tiene máx de iteraciones se indica n=float('inf')
    """
    # Inicialización
    cont = 0
    error_x = abs(b - a)
    error_y = min(abs(f(a)), abs(f(b)))
    # Bloque iterativo de la búsqueda
    while (f(a) * f(b) < 0) and (tol_x < error_x) and (tol_y < error_y) and (cont < n):
         c = (a + b) / 2
         error_y = abs(f(c))
         error_x = abs(a-c)
         if f(a) * f(c) < 0:
             b = c
         else:
             a = c
         cont = cont + 1
    # Bloque de validación
    if error_x <= tol_x:
        return c
    elif error_y <= tol_y:
        if abs(f(a)) <= tol_y:
            return a
        else:
            return b
    elif cont <= n:
        return c
    else:
        return None
