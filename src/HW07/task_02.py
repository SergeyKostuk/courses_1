from task_01 import (
    km_mile,
    mile_km,
    lb_kg,
    kg_lb,
    oz_gr,
    gr_oz,
    litre_gal,
    pt_litre,
    litre_pt,
    cm_inch,
    inch_cm,
    gal_litre,
)

comands = {
    0: 'good bue',
    1: 'cm->inch',
    2: 'inch->cm',
    3: 'km->mile',
    4: 'mile->km',
    5: 'lb->kg',
    6: 'kg->lb',
    7: 'oz->gr',
    8: 'gr->oz',
    9: 'litre->gal',
    10: 'pt->litre',
    11: 'itre->pt',
    12: 'gal->litre',

}
while True:
    for key, value in comands.items():
        print(f'{key}:  {value}')

    a = int(input('select the comand: \n'))

    if a == 0:
        print('good bye!')
        break

    elif a not in comands.keys():
        print('wrong input,check comands')
        continue
    x = float(input('number of convertible units: x = '))
    if a == 1:
        print(f'convered {x} cm --> {cm_inch(x)} inch')
    elif a == 2:
        print(f'convered {x} inch --> {inch_cm(x)} cm')
    elif a == 3:
        print(f'convered {x} km --> {km_mile(x)} miles')
    elif a == 4:
        print(f'convered {x} miles --> {mile_km(x)} km')
    elif a == 5:
        print(f'convered {x} lb --> {lb_kg(x)} kg')
    elif a == 6:
        print(f'convered {x} kg --> {kg_lb(x)} lb')
    elif a == 7:
        print(f'convered {x} oz --> {oz_gr(x)} gr')
    elif a == 8:
        print(f'convered {x} gr --> {gr_oz(x)} oz')
    elif a == 9:
        print(f'convered {x} litre --> {litre_gal(x)} gal')
    elif a == 10:
        print(f'convered {x} pt --> {pt_litre(x)} litre')
    elif a == 11:
        print(f'convered {x} litre --> {litre_pt(x)} pt')
    elif a == 12:
        print(f'convered {x} gal --> {gal_litre(x)} litre')
