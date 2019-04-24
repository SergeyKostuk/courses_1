# cоздать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут
import datetime
travel_time = datetime.timedelta(hours=7, minutes=20)
slow_trains = []
trains = [
    {
        'number': '1',
        'place of arrival ': 'Warsaw',
        'time of arrival ': datetime.timedelta(hours=21, minutes=40) ,
        'place of departure': 'Minsk',
        'time of departure': datetime.timedelta(hours=12, minutes=21),
    },
    {
        'number': '2',
        'place of arrival ': 'paris',
        'time of arrival ': datetime.timedelta(hours=21, minutes=40),
        'place of departure': 'Minsk',
        'time of departure': datetime.timedelta(hours=21, minutes=40),
    },
    {
        'number': '3',
        'place of arrival ': 'Amsterdam',
        'time of arrival ': datetime.timedelta(hours=20, minutes=54),
        'place of departure': 'London',
        'time of departure': datetime.timedelta(hours=7, minutes=40),
    },
]

for train in trains:
    if train['time of arrival '] - train['time of departure'] > travel_time:
        slow_trains.append(train)
for train in slow_trains:
    for key, value in train.items():
        print(f'{key} --> {value}')

