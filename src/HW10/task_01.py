# В конец существующего текстового файла записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.
def main():
    with open('test.txt', 'a') as my_file:
        for i in range(3):
            line = input()
            my_file.write(f'{line}\n')
if __name__ == '__main__':
   main()
