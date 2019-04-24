i = 0
pupils = [
    {
        'firstname': 'Masha',
        'group': '20',
        'physics': 7,
        'informatics': 6,
        'history': 8,
    },
    {
        'firstname': 'Misha',
        'group': '20',
        'physics': 2,
        'informatics': 2,
        'history': 2,
    },
    {
        'firstname': 'Alex',
        'group': '20',
        'physics': 3,
        'informatics': 6,
        'history': 8,
    },
]
good_pupls = []
for pupile in pupils:
    average_mark = (pupile['physics'] + pupile['informatics'] + pupile['history']) / 3

    if average_mark > 4:
        good_pupls.append(pupile)
    for pupl in good_pupls:
        for key, value in pupl.items():
            print(f'{key} --> {value}')
