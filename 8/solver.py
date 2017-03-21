import re


class Panel(object):
    def __init__(self, xLen, yLen):
        self.xLen = xLen
        self.yLen = yLen
        self.map = [[0 for j in range(self.xLen)]for i in range(self.yLen)]

    def rect(self, x, y):
        for row in range(y):
            for col in range(x):
                self.map[row][col] = 1

    def row(self, y, by):
        for i in range(by):
            self.map[y] = self.map[y][-1:] + self.map[y][:-1]

    def col(self, x, by):
        data = [row[x] for row in self.map]
        for i in range(by):
            data = data[-1:] + data[:-1]
        for i in range(len(self.map)):
            self.map[i-1][x] = data[i-1]

    def counter(self):
        count = 0
        for x in range(self.xLen):
            for y in range(self.yLen):
                count += self.map[y][x]

        return count

    def printer(self):
        for y in range(self.yLen):
            print('\n', end='')
            for x in range(self.xLen):
                print(self.map[y][x], end='')

    def interpreter(self, string):
        res_rect = re.search('^(.*) (.*)', string)
        res_rot = re.search('^(.*) (.*) (.*) (.*) (.*)', string)
        if res_rect.group(1) == 'rect':
            x = int(re.search('(\d)x', res_rect.group(2)).group(1) )
            y = int(re.search('x(\d)', res_rect.group(2)).group(1) )
            print('rect', x, y)
            self.rect(x, y)
        elif res_rot.group(1) == 'rotate':
            if res_rot.group(2) == 'row':
                y = int( re.search('y=(.*)', res_rot.group(3)).group(1) )
                by = int( res_rot.group(5) )
                print('row', y, by)
                self.col(y, by)
            elif res_rot.group(2) == 'column':
                x = int( re.search('x=(.*)', res_rot.group(3)).group(1) )
                by = int( res_rot.group(5) )
                print('col', x, by)
                self.col(x, by)



if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        data = f.readlines()
    test = Panel(50, 6)
    for command in data:
        test.interpreter(command)
    test.printer()
    print('\n')
    print(test.counter())
