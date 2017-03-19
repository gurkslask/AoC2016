class Panel(object):
    def __init__(self, xLen, yLen):
        self.xLen = xLen
        self.yLen = yLen
        self.map = [], []
        for x in range(xLen):
            for y in range(yLen):
                self.map[x][y] = 0

    def rect(x, y):
        pass

    def row(y, by):
        pass

    def col(x, by):
        pass

    def counter(self):
        count = 0
        for x in range(self.xLen):
            for y in range(self.yLen):
                count += self.map[x][y]

    def printer(self):
        for x in range(self.xLen):
            print('\n')
            for y in range(self.yLen):
                print(self.map[x][y])


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        data = f.readlines()
    pass
