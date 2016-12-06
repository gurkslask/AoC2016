import collections

ans1, ans2 = '', ''
with open('input.txt') as fp:
    for stuff in zip(*fp.read().strip().split('\n')):
        counter = collections.Counter(stuff).most_common()
        ans1 += counter[0][0]
        ans2 += counter[-1][0]
print(ans1)
print(ans2)
