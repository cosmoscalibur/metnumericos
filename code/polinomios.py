def horner_p(a, x0):
    """
    a: vector de coeficientes del polinomio.
    x0: valor en el cual se desea evaluar el polinomio.
    """
    b = list()
    b.append(a[0])
    for coeficiente in a[1:]:
        b.append(b[-1] * x0 + coeficiente)
    return b[-1], b[:-1]

def horner_pq(a, x0):
    """
    a: vector de coeficientes del polinomio.
    x0: valor en el cual se desea evaluar el polinomio.
    """
    P, b = horner_p(a, x0)
    Q, c = horner_p(b, x0)
    return P, Q

def newton_horner(a, x0, n=1000, tol_x=1e-6, tol_y=1e-6):
    """
    a: vector de coeficientes del polinomio.
    x0: valor inicial para la busqueda.
    n: Número máximo de iteraciones. Si no se requiere usar n=float('inf')
    tol_x y tol_y: tolerancia permitida en ambos ejes. Si no se requiere tol=0.
    """
    cont = 0
    error_x = tol_x * 10 + 1
    P, b = horner_p(a, x0)
    error_y = abs(P)
    while (cont < n) and (tol_x < error_x) and (tol_y < error_y):
        P, Q = horner_pq(a, x0)
        x = x0 - P / Q
        error_x = abs(x - x0)
        error_y = abs(P)
        x0 = x
        cont = cont + 1
    if (error_x <= tol_x) or (error_y <= tol_y):
        P, b = horner_p(a, x0)
        return x0, b
    else:
        return None

def newton_horner_n(a, x0, n=1000, tol_x=1e-6, tol_y=1e-6, N=1):
    raices = list()
    for cont in range(N):
        x0, a = newton_horner(a, x0, n, tol_x, tol_y)
        raices.append(x0)
    return raices
