from math import log10

def error_absoluto(exacto, aproximado):
    return abs(exacto - aproximado)

def error_relativo(exacto, aproximado):
    return abs((exacto - aproximado) / exacto)

def significativas(er):
    return int(log10(5/er))
