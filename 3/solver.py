import re


def solver(data):
    num_corr = 0
    for row in data:
        print('Före {} \n Efter {}'.format(row, splitter(row)))
        if checker(splitter(row)):
            num_corr += 1
    return num_corr


def checker(lengths):
    lengths.sort()
    if lengths[2] >= lengths[1] + lengths[0]:
        return False
    else:
        return True


def splitter(text):
    restring = r'\s*(\d*)\s*(\d*)\s*(\d*)'
    return [int(i) for i in re.findall(restring, text)[0]]

if __name__ == '__main__':
    with open('input', 'r') as f:
        data = f.readlines()
    print(solver(data))
