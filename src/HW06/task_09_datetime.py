# cоздать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут
import datetime
slow_trains = []
trains = [
    {
        'number': '1',
        'place_of_arrival': 'Nowere',
        'time_of_arrival': datetime.datetime(2020, 12, 1, 12, 41),
        'place_of_departure': 'Minsk',
        'time_of_departure': datetime.datetime(2019, 12, 1, 12, 21),
    },
    {
        'number': '2',
        'place_of_arrival': 'Warsaw',
        'time_of_arrival':  datetime.datetime(2019, 12, 3, 23, 42),
        'place_of_departure': 'Minsk',
        'time_of_departure':  datetime.datetime(2019, 12, 3, 21, 40),
    },
    {
        'number': '3',
        'place_of_arrival': 'Warsaw',
        'time_of_arrival':  datetime.datetime(2019, 12, 3, 20, 54),
        'place_of_departure': 'Minsk',
        'time_of_departure':  datetime.datetime(2019, 12, 3, 7, 40),
    },
]

for train in trains:
    travel_time = train['time_of_arrival'] - train['time_of_departure']
    if travel_time > datetime.timedelta(hours=7, minutes=21):
        slow_trains.append(train)
print('trains with travel time more than 7:20')
for train in slow_trains:
    for key, value in train.items():
        print(f'{key} --> {value}')
