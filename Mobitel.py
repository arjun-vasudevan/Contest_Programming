from sys import stdin

normal_keys = {''    :1, 'abc':2, 'def' :3,
               'ghi' :4, 'jkl':5, 'mno' :6,
               'pqrs':7, 'tuv':8, 'wxyz':9}

behaviours = [int(_) for _ in stdin.readline()[:-1].split()]
word = stdin.readline()[:-1]

corresponding = {k:i + 1 for i, k in enumerate(behaviours)}

new = ''

place = 0
for letter in word:
    norm_num = [normal_keys[x] for x in normal_keys.keys() if letter in x][0]
    num_times = [x.index(letter) + 1 for x in normal_keys.keys() if letter in x][0]
    if norm_num == place:
        new += '#'
    place = norm_num
    new += str(corresponding[norm_num]) * num_times

print new
