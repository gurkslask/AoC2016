import re
from collections import defaultdict
import operator


def solver(data):
    num_ctr = 0
    for row in data:
        num_ctr += checker(row.rstrip('\n'))
    return num_ctr


def checker(text):
    list_of_text = splitter(text)
    first_dict = defaultdict(int)
    result_dict = defaultdict(str)
    result_list = []
    for char in list_of_text[0]:
        first_dict[char] += 1
    for char in first_dict:
        result_dict[first_dict[char]] += char
    for i in range(5):
        greatest_key = max(result_dict.keys())
        temp_list = list(result_dict[greatest_key])
        temp_list.sort()
        result_list.append(temp_list[0])
        temp_list.pop(0)
        result_dict[greatest_key] = temp_list
        if result_dict[greatest_key] == []:
            result_dict.pop(greatest_key, None)
    if ''.join(result_list) == list_of_text[2]:
        return list_of_text[1]
    else:
        return 0


    

def splitter(text):
    restring = r'([a-z]*)([0-9]*)\[(\w*)\]'
    resubstring = r'[-]'
    text = re.sub(resubstring, '', text)
    temp_list = list([i for i in re.findall(restring, text)][0])
    temp_list[1] = int(temp_list[1])
    return temp_list

if __name__ == '__main__':
    with open('input', 'r') as f:
        data = f.readlines()
    print(solver(data))
