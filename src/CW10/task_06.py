def main():
    with open('test.txt', 'w') as my_file:
        
        a = []
        while len(a) < 6:
            line = input()
            a.append(f'{line}\n')
        my_file.writelines(a)


if __name__ == '__main__':
    main()
