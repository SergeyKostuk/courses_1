# class A:
#     def print_smth(self):
#         print('a')
#
#     def a_method(self):
#         print('a method')
#
#
# class B(A):
#     def print_smth(self):
#         print('B')
#
#     def b_method(self):
#         print('b method')
#
#
# class C(A):
#     def print_smth(self):
#         print('C')
#
#     def c_method(self):
#         print('c method')
#
#

# class D(B, C):
#     def d_method(self):
#         print('d method')
# d = D()
# a = A()
# b = B()
# c = C()
# d.print_smth()
# a.print_smth()
# d.print_smth()
# print(list(filter(lambda x: '__' not in x, dir(A))))
# print(list(filter(lambda x: '__' not in x, dir(B))))
# print(list(filter(lambda x: '__' not in x, dir(C))))
# print(list(filter(lambda x: '__' not in x, dir(D))))
#
# d.print_smth()
class MyException(Exception):
    def __init__(self, message='AAA!!'):
        super().__init__(message)





class Book:
    def __init__(self, pages):
        if type(pages) != int:
            raise MyException('pages are int')
        self.pages = pages


a = Book('22')
