# Создать программу для работы с  учетными записями пользователей.
# Программа позволяет создавать, искать, править, фильтровать, удалять.
# Учетная запись пользователя представляет из себя словарь со следующими данными:
# имя, фамилия, дата рождения, профессия, числовой идентификатор(id).
# Для хранения данных использовать json файл. Задание выполнить в отдельной папке.
import json


def create_file():
    with open('source_base.txt', 'w'):
        pass


def filter_names():
    with open('source_base.txt') as my_file:
        my_list = [json.loads(line) for line in my_file]
        list_of_names = []
        for person in my_list:
            list_of_names.append(person['name'])
        list_of_names = list(set(list_of_names))
        list_of_names.sort()

    with open('source_base.txt', 'w') as my_file_1:
        for name in list_of_names:
            for person in my_list:
                if person['name'] == name:
                    my_file_1.write(f'{json.dumps(person)}\n')


def person(name, surname, DOB, profession, id):
    person_info = {
        "name": name,
        "surname": surname,
        "DOB": DOB,
        "profession": profession,
        "id": id
    }

    return person_info


def add_person(person_info):
    with open('source_base.txt') as my_file:
        my_list = [json.loads(line) for line in my_file]
        list_of_id = []
        if my_list == []:
            with open('source_base.txt', 'a') as my_file_1:
                data = json.dumps(person_info)
                my_file_1.write(f'{data}\n')
                return

        for person in my_list:
            list_of_id.append(person['id'])

            for el_id in list_of_id:
                if person_info['id'] == el_id:
                    print('incorect id')
                    return
        else:
            with open('source_base.txt', 'a') as my_file_1:
                data = json.dumps(person_info)
                my_file_1.write(f'{data}\n')


def change_with_id(id):
    with open('source_base.txt') as my_file:

        my_list = [json.loads(line) for line in my_file]
        for person in my_list:
            if person['id'] == id:
                person['name'] = input('name:')
                person['surname'] = input('surname:')
                person['DOB'] = input('DOB:')
                person['profession'] = input('profession:')
    with open('source_base.txt', 'w') as my_file_1:
        for person in my_list:
            my_file_1.write(f'{json.dumps(person)}\n')


def search_with_id(id):
    with open('source_base.txt') as my_file:

        my_list = [json.loads(line) for line in my_file]

        my_list = filter(lambda x: id == x['id'], my_list)
        for person in my_list:
            print()
            for key, value in person.items():
                print(f'{key} : {value}')


def show():
    with open('source_base.txt') as my_file:
        print('-----------------------')
        my_list = [json.loads(line) for line in my_file]
        for person in my_list:
            print()
            for key, value in person.items():
                print(f'{key} : {value}')
        print('-----------------------')


def del_person_with_id(id):
    with open('source_base.txt') as my_file:
        my_list = [json.loads(line) for line in my_file]

        my_list = filter(lambda x: id != x['id'], my_list)

    with open('source_base.txt', 'w') as my_file_1:
        for person in my_list:
            my_file_1.write(f'{json.dumps(person)}\n')


def main():
    a = person("misha", "ivanov", "19.03.1999", "programer", 133)
    b = person("bob", "falon", "13.13.1988", "comic", 132)
    c = person("maria", "petrova", "05.03.1976", "teacher", 130)
    d = person("varia", "petrova", "05.03.1976", "teacher", 132)
    add_person(a)
    add_person(b)
    add_person(c)
    add_person(d)
    show()
    filter_names()
    show()
    del_person_with_id(132)
    search_with_id(133)
    change_with_id(130)


if __name__ == '__main__':
    main()
