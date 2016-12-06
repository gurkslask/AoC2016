numpad = [[1,  2, 3], [4, 5, 6], [7, 8, 9]]
chars = {
        'U': [0, -1],
        'D': [0, 1],
        'L': [-1, 0],
        'R': [1, 0]
        }

def solver(data):
    numberlist = []
    for sequence in data:
        pos = [1, 1]
        for char in sequence:
            pos[0] += chars[char][0]
            pos[1] += chars[char][1]
            if pos[0] > 2:
                pos[0] = 2
            elif pos[0] < 0:
                pos[0] = 0
            if pos[1] > 2:
                pos[1] = 2
            elif pos[1] < 0:
                pos[1] = 0
        numberlist.append(numpad[pos[1]][pos[0]])
    return numberlist

if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        data_in = f.read().splitlines()
    print(solver(data_in))
