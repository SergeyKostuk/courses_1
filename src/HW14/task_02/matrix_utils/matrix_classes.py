from random import randint


class Matrix:
    def __init__(self, data=None):
        if not data:
            self.n = self.m = 5
            data = []
            for i in range(self.n):
                row = []
                for j in range(self.m):
                    row.append(randint(1, 40))
                data.append(row)
        else:
            self.n = len(data)
            self.m = len(data[0])
        self.data = data

    def __str__(self):
        return ' '.join(map(str, self.data))
