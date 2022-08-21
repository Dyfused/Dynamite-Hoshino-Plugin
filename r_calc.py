import math


def case(order: int):
    switcher = {
        5: 3,
        9: 4,
        14: 5,
        20: 6,
        27: 7,
        35: 8,
        44: 9,
        54: 10,
        65: 11
    }
    return switcher.get(order, -1)


def arrc(num: int):
    c = {1: 279.879794687164, 2: 528.301077749884, 3: 422.128204580857, 4: 138.580738104051, 5: 318.252118021848,
         6: -21.3604901556347, 7: 89.799165984382, 8: 256.769254208808, 9: 110.044290813559, 10: 25.6857362881284,
         11: -3.45575127827165, 12: -11.2439540909426, 13: -46.0356135329964, 14: -42.4055325292137,
         15: -12.2459945433335, 16: 8.91771876412662, 17: 33.5454538433112, 18: 33.216005109172, 19: 29.9737147306553,
         20: 21.7501092277346, 21: 4.69435084736257, 22: -2.07316842598594, 23: -8.52746692063741,
         24: -11.4173961727952, 25: -13.7580079836705, 26: -14.3051642335754, 27: -8.34658365581463,
         28: -0.89353524074857, 29: 0.714990388514441, 30: 3.57845524206804, 31: 3.79243682942648, 32: 4.08195534054915,
         33: 6.23083840922214, 34: 5.49378824597485, 35: 1.69935797162909, 36: -7.95468233626518E-02,
         37: -9.28951907355424E-02, 38: -0.88520913997908, 39: -0.965617394829134, 40: -0.619991505598762,
         41: -1.48063492507091, 42: -2.21198484168029, 43: -1.15918404495256, 44: 6.90824302578919E-02,
         45: 7.86488698968826E-02, 46: 5.59550676107935E-03, 47: 0.120475552036249, 48: 0.194041976300861,
         49: 2.52469792567985E-02, 50: 0.128790661891046, 51: 0.42177821494088, 52: 0.385782806557072,
         53: 7.51328698680896E-02, 54: -8.02629465389211E-02, 55: -1.31400067817723E-02}

    return c[num]


def eval_chebyshev_poly(order: int, logx: int, logy: int, x: float, y: float):
    tx, ty, v = {}, {}, {}
    if logx != 1:
        x = (x - 11.35) / 5.65
    else:
        x = (math.log(x) - 2.28683975944836) / 0.546373584607856

    if logy != 1:
        y = (y - 0.9677015525) / 0.0322984475
    else:
        y = (math.log(y) - (-3.33888571301625E-02)) / 3.33888571301625E-02

    tcnt = case(order)
    if tcnt == -1:
        return 0.0

    if tcnt > 6:
        if x < -1:
            x = -1.0
        if x > 1:
            x = 1.0
        if y < -1:
            y = -1.0
        if y > 1:
            y = 1.0
    tx[1] = 1.0
    ty[1] = 1.0
    tx[2] = x
    ty[2] = y
    for i in range(3, tcnt + 1, 1):
        tx[i] = 2 * x * tx[i - 1] - tx[i - 2]
        ty[i] = 2 * y * ty[i - 1] - ty[i - 2]
    iv = 1
    for i in range(1, tcnt + 1, 1):
        for j in range(i, 0, -1):
            v[iv] = tx[j] * ty[i - j + 1]
            iv = iv + 1
    z = 0.0
    for j in range(1, order + 2, 1):
        z = z + arrc(j) * v[j]
    return z


def calc_r(rating: float, accuracy: float):
    return eval_chebyshev_poly(54, 1, 1, rating, accuracy)