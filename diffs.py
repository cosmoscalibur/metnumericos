# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 14:36:27 2016

@author: cosmoscalibur
"""

def diff_2p(x_points, y_points, scheme = 'right', **kwargs):
    if "n" in kwargs:
        n = kwargs["n"]
        if "h" in kwargs:
            h = kwargs["h"]
            a = x_points
        else:
            a = x_points[0]
            h = (x_points[1] - a) / n
    elif "h" in kwargs:
        h = kwargs["h"]
        a = x_points[0]
        n = int((x_points[1] - a) / h)
    else:
        n = len(x_points) - 1
    if len(x_points) - 1 != n:
        x_points = [a + i*h for i in range(n+1)]
    if not hasattr(y_points, '__iter__'):
        y_function = y_points
        y_points = [y_function(x_) for x_ in x_points]
    diff_fx = []
    cont = 0
    while cont < n:
        diff_eval = (y_points[cont + 1] - y_points[cont]) / \
            (x_points[cont + 1] - x_points[cont])
        diff_fx.append(diff_eval)
        cont += 1
    if scheme=='right':
        diff_fx.append(None)
    elif scheme=='left':
        diff_fx.insert(0, None)
    elif not scheme == 'none':
        diff_fx = None
    return diff_fx
