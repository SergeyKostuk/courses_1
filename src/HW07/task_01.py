# Написать 12 функций по переводу:
# Дюймы в сантиметры
# Сантиметры в дюймы
# Мили в километры
# Километры в мили
# Фунты в килограммы
# Килограммы в фунты
# Унции в граммы
# Граммы в унции
# Галлон в литры
# Литры в галлоны
# Пинты в литры
# Литры в пинты
from typing import Union
def inch_cm(x):
    x *= 2.54
    return x


def cm_inch(x: Union[int, float]) -> float:
    x *= 0.39
    return x


def mile_km(x):
    x *= 1.61
    return x


def km_mile(x):
    x *= 0.621
    return x


def lb_kg(x):
    x *= 0.454
    return x


def kg_lb(x):
    x *= 2.205
    return x


def oz_gr(x):
    x *= 28.35
    return x


def gr_oz(x):
    x *= 0.0352
    return x


def litre_gal(x):
    x *= 0.264
    return x


def gal_litre(x):
    x *= 3.785
    return x


def pt_litre(x):
    x *= 0.473
    return x


def litre_pt(x):
    x *= 2.113
    return x
a = 'lol'
print(43%360)