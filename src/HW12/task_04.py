import json


class DBOfClinic:

    @staticmethod
    def init_db():
        with open('db.json', 'w') as db:
            db.write(json.dumps({}))

    @staticmethod
    def show_record(record):
        print(f'id: {record["id"]}')
        print(f'First name: {record["firstname"]}')
        print(f'Lastname name: {record["lastname"]}')
        print(f'Date of birth: {record["date_of_birth"]}')
        print(f'Profession: {record["profession"]}')
        print(f'kind of amimal: {record["PEt"]["kind"]}')
        print(f'name of amimal: {record["PEt"]["name_of_pet"]}')
        print(f'age of amimal: {record["PEt"]["age"]}')

        print('-' * 10)

    @staticmethod
    def show_all():
        data = DBOfClinic.read_db()
        records = data.get('records', [])
        print('-' * 10)
        print('Records')
        print('-' * 10)
        for record in records:
            DBOfClinic.show_record(record)

    @staticmethod
    def read_db():
        with open('db.json') as db:
            data = json.loads(db.read())
        return data

    @staticmethod
    def write_db(data):
        with open('db.json', 'w') as db:
            db.write(json.dumps(data))

    @staticmethod
    def write_new_record():
        data = DBOfClinic.read_db()
        record = Master.create_new_record()
        lool = Pet.record_about_pet()
        last_id = data.get('last_id', 0)
        record['PEt'] = lool
        record['id'] = last_id + 1
        data['last_id'] = record['id']
        records = data.get('records', [])
        records.append(record)
        data['records'] = records
        DBOfClinic.write_db(data)

    @staticmethod
    def remove_record():
        data = DBOfClinic.read_db()
        record_id = input('Write id of record to remove: ')
        if not record_id.isdigit():
            print('Wrong input')
            return
        record_id = int(record_id)
        records = data['records']
        updated_records = filter(lambda record: record['id'] != record_id, records)
        data['records'] = list(updated_records)
        DBOfClinic.write_db(data)
        print(f'Record {record_id} was removed')

    @staticmethod
    def search_by_id():
        data = DBOfClinic.read_db()
        record_id = input('Write id of record to search: ')
        if not record_id.isdigit():
            print('Wrong input')

            return
        record_id = int(record_id)
        records = data['records']
        searched_records = list(filter(lambda record: record['id'] == record_id, records))
        if not searched_records:
            print(f'There is no records with id {record_id}')

            return
        DBOfClinic.show_record(searched_records[0])


class Master(DBOfClinic):
    @staticmethod
    def create_new_record():
        name = input('Name: ')
        lastname = input('Last name: ')
        profession = input('Profession: ')
        date_of_birth = input('Date of birth(example: 12-06-1990): ')

        record = dict(
            firstname=name,
            lastname=lastname,
            profession=profession,
            date_of_birth=date_of_birth,
        )
        return record


class Pet(Master):
    @staticmethod
    def record_about_pet():
        kind = input('Kind of pet: ')
        name = input('Name of your pet: ')
        age = input('How old is it:')

        record = dict(

            kind=kind,
            name_of_pet=name,
            age=age,

        )
        return record


def main():
    DBOfClinic.init_db()
    DBOfClinic.write_new_record()
    DBOfClinic.write_new_record()
    DBOfClinic.remove_record()
    DBOfClinic.search_by_id()


if __name__ == "__main__":
    main()
