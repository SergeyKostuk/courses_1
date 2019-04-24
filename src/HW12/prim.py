import json


def press_enter_to_continue():
    input('Press Enter to continue')


def init_db():
    with open('files/db.json', 'w') as db:
        db.write(json.dumps({}))


def read_db():
    with open('files/db.json') as db:
        data = json.loads(db.read())
    return data


def write_db(data):
    with open('files/db.json', 'w') as db:
        db.write(json.dumps(data))


def show_record(record):
    print(f'id: {record["id"]}')
    print(f'First name: {record["firstname"]}')
    print(f'Lastname name: {record["lastname"]}')
    print(f'Date of birth: {record["date_of_birth"]}')
    print(f'Profession: {record["profession"]}')
    print('-' * 10)


def show_all():
    data = read_db()
    records = data.get('records', [])
    print('-' * 10)
    print('Records')
    print('-' * 10)
    for record in records:
        show_record(record)
    press_enter_to_continue()


def create_new_record():
    firsname = input('First name: ')
    lastname = input('Last name: ')
    profession = input('Profession: ')
    date_of_birth = input('Date of birth(example: 12-06-1990): ')
    record = dict(
        firstname=firsname,
        lastname=lastname,
        profession=profession,
        date_of_birth=date_of_birth,
    )
    return record


def write_new_record():
    data = read_db()
    record = create_new_record()
    last_id = data.get('last_id', 0)
    record['id'] = last_id + 1
    data['last_id'] = record['id']
    records = data.get('records', [])
    records.append(record)
    data['records'] = records
    write_db(data)
    press_enter_to_continue()


def remove_record():
    data = read_db()
    record_id = input('Write id of record to remove: ')
    if not record_id.isdigit():
        print('Wrong input')
        return
    record_id = int(record_id)
    records = data['records']
    updated_records = filter(lambda record: record['id'] != record_id, records)
    data['records'] = list(updated_records)
    write_db(data)
    print(f'Record {record_id} was removed')
    press_enter_to_continue()


def edit_record():
    data = read_db()
    record_id = input('Write id of record to edit: ')
    if not record_id.isdigit():
        print('Wrong input')
        return
    record_id = int(record_id)
    records = data['records']
    filtered_records_with_index = [(record, i) for i, record in enumerate(records) if record['id'] == record_id]
    if not len(filtered_records_with_index):
        print(f'There is no record with id {record_id}')
        return
    record, index = filtered_records_with_index[0]

    new_firsname = input('New first name(press enter to not change): ')
    new_lastname = input('New first name(press enter to not change): ')
    new_proffesion = input('New first name(press enter to not change): ')
    new_date_of_birth = input('New first name(press enter to not change): ')

    changed_record = dict(
        id=record_id,
        firstname=new_firsname or record['firsname'],
        lastname=new_lastname or record['lastname'],
        profession=new_proffesion or record['profession'],
        date_of_birth=new_date_of_birth or record['date_of_birth'],
    )
    records[index] = changed_record
    data['records'] = list(records)
    write_db(data)
    print(f'Record {record_id} was edited')
    press_enter_to_continue()


def search_by_id():
    data = read_db()
    record_id = input('Write id of record to search: ')
    if not record_id.isdigit():
        print('Wrong input')
        press_enter_to_continue()
        return
    record_id = int(record_id)
    records = data['records']
    searched_records = list(filter(lambda record: record['id'] == record_id, records))
    if not searched_records:
        print(f'There is no records with id {record_id}')
        press_enter_to_continue()
        return
    show_record(searched_records[0])
    press_enter_to_continue()


def filter_by_keyword():
    data = read_db()
    records = data['records']
    keyword = input('Write keyword to search with filter: ')
    searched_records = list(
        filter(
            lambda record: keyword in record['firstname'] or keyword in record['lastname'], records
        )
    )
    print('-' * 10)
    print(f'Filtered records by keyword: {keyword}')
    print('-' * 10)
    for record in searched_records:
        show_record(record)
    press_enter_to_continue()