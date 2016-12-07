import re


def solver(data):
    correct_ctr = 0
    for row in data:
        split_dict = splitter(row)
        bad = False
        for i in split_dict['bad']:
            if checker(i):
                bad = True
                break
        for i in split_dict['good']:
            if checker(i) and not bad:
                correct_ctr += 1
                break
    return correct_ctr


def checker(text):
    restring = r'(\w)(\w)\2\1'
    pos_ctr = 0
    for char in text:
        if re.match(restring, text[pos_ctr:pos_ctr + 4]) and not text[pos_ctr] == text[pos_ctr + 2]:
            return True
        pos_ctr += 1
    return False


def splitter(text):
    result_dict = {'good': [], 'bad': []}
    text = text.replace('[', ',').replace(']', ',')
    text = text.split(',')
    result_dict['good'] = text[0::2]
    result_dict['bad'] = text[1::2]
    return result_dict


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        data = f.readlines()
    print(solver(data))
