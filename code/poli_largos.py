def poli_100():
    """
    P_{100}(x) = x^{100} - 5x^{50} - 1
    """
    poli = list()
    poli.append(1)
    poli.extend(49 * [0])
    poli.append(-5)
    poli.extend(49 * [0])
    poli.append(-1)
    return poli

def poli_intercalado_0_11():
    """
    \sum\limits_{n=0}^{10}(n-5)(-1)^n x^{2n}
    """
    poli = list()
    for i in range(11):
        poli.append((i-5)*(-1)**i)
        poli.append(0)
    poli.reverse()
    return poli
