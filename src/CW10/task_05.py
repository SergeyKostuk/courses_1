def write_a_string():
    i = 1
    my_file = open('test.txt')
    while True:
        line = my_file.readline()
        if i == 5:
            print(line)
            break
        i += 1
    my_file.close()


def first_N_strings(n):
    i = 1
    my_file = open('test.txt')
    while True:
        line = my_file.readline().strip()

        print(line)
        if i == n:
            break
        i += 1
    my_file.close()


def write_from_to(a, b):
    i = 1
    my_file = open('test.txt')
    while True:
        line = my_file.readline().strip()
        if i >= a and i <= b:
            print(line)
        if i > b:
            break
        i += 1
    my_file.close()


def Read_all():
    my_file = open('test.txt')
    while True:
        line = my_file.readline().strip()
        if not line:
            break
        print(line)
    my_file.close()


def main():
    print()
    write_a_string()
    print()
    first_N_strings(5)
    print()
    write_from_to(2, 4)
    print()
    Read_all()


if __name__ == '__main__':
    main()
