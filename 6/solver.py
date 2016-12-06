"""Solver for advent of code 6"""
from collections import defaultdict

def read_file():
    """Read txt file."""
    columns = []
    temp_list = []
    with open('input.txt', 'r') as f:
        data = f.readlines()
    """for row in data:
        temp_list = [i[0] for i in row]
        columns.append(temp_list)"""
    for i in range(len(data[0])):
        columns.append([row[i] for row in data])
    return columns



def solver(data):
    """Count the occurence of characters in every line."""
    result_list = []
    print('hej:', data[2])
    for row in data:
        lista = ['a', 0]
        result_dict = defaultdict(int)
        for char in row:
            # Count occurences to a dict
            result_dict[char] += 1
        for key in result_dict:
            # Check if occurence is higher than stored in lista
            if result_dict[key] > lista[1]:
                lista = [key, result_dict[key]]

        print(result_dict)
        result_list.append(lista[0])
    return result_list

if __name__ == '__main__':
    # print(solver(read_file()))
    print(''.join(solver(read_file())))
