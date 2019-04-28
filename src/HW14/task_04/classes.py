class Math:
    def __init__(self, arg_1=None, arg_2=None):

        if len(arg_1.split()) > 1 or len(arg_2.split()) > 1:
            raise NoSpaces()

        elif not arg_1.lstrip('-').isdigit() or not arg_2.lstrip('-').isdigit():
            raise IncorrectInputError()
        self.arg_1 = arg_1
        self.arg_2 = arg_2

    def summ(self):
        print(float(self.arg_1) + float(self.arg_2))

    def diff(self):
        print(float(self.arg_1) - float(self.arg_2))

    def mult(self):
        print(float(self.arg_1) * float(self.arg_2))

    def division(self):
        print(float(self.arg_1) / float(self.arg_2))


class ComplexMath:
    def __init__(self, arg_1, arg_2, arg_3, arg_4):
        self.arg_1 = arg_1
        self.arg_2 = arg_2
        self.arg_3 = arg_3
        self.arg_4 = arg_4

    def summ(self):
        print(complex(self.arg_1, self.arg_2) + complex(self.arg_3, self.arg_4))

    def diff(self):
        print(complex(self.arg_1, self.arg_2) - complex(self.arg_3, self.arg_4))

    def mult(self):
        print(complex(self.arg_1, self.arg_2) * complex(self.arg_3, self.arg_4))

    def division(self):
        print(complex(self.arg_1, self.arg_2) / complex(self.arg_3, self.arg_4))
