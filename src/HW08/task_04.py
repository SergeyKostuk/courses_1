def func(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        res = 'no valid decisions'

    elif d > 0:
        x_1 = (-b + d ** 0.5) / (2 * a)
        x_2 = (-b - d ** 0.5) / (2 * a)
        res = f'the decisions are x1 = {x_1}, x2 = {x_2}'
    else:
        x = -b / (2 * a)
        res = f'the decision is  x = {x}'
    print(res)


func(4.5, 60, 4)
