def main():
    my_file = open('test.txt')
    print(my_file.readline().strip())

    my_file.close()


if __name__ == '__main__':
   main()
