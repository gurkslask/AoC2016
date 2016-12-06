"""Solver for AoC1."""


def countdistance(input):
    return input[0] + input[1]


def walk(direction_list):
    directions = {
            0: 'N',
            1: 'E',
            2: 'S',
            3: 'W'
            }
    # y, x
    map_list = [0, 0]
    direction_ctr = 0
    for row in direction_list:
        if row[0] == 'R':
            direction_ctr += 1
            if direction_ctr > 3:
                direction_ctr = 0
        elif row[0] == 'L':
            direction_ctr -= 1
            if direction_ctr < 0:
                direction_ctr = 3
        if directions[direction_ctr] == 'N':
            map_list[0] += row[1]
        elif directions[direction_ctr] == 'E':
            map_list[1] += row[1]
        elif directions[direction_ctr] == 'S':
            map_list[0] -= row[1]
        elif directions[direction_ctr] == 'W':
            map_list[1] -= row[1]
    return map_list


def parseinput(input):
    return [[row[0], int(row[1:])] for row in input]

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().replace('\n', '').split(', ')
    print(data)
    print(countdistance(walk(parseinput(data))))
