from string import ascii_lowercase, ascii_uppercase
from random import randint, choice

letters = ascii_uppercase + ascii_lowercase



def letter_num(letter):
    num = ord(letter) - 65
    if num > 25:
        return num - 6
    return num


def lsd_radix_sort(arr):
    keys = [0 for _ in range(len(letters))]

    len_word = len(arr[0])
    for i in range(len_word - 1, -1, -1):
        for j in arr:
            keys[letter_num(j[i])] += 1
        for j in range(1,len( letters)):
            keys[j]+=keys[j-1]
        arr2 = ['' for _ in range(len(arr))]
        for j in range(len(arr) - 1, -1, -1):
            arr2[keys[letter_num(arr[j][i])]-1] = arr[j]
            keys[letter_num(arr[j][i])]-=1
        arr = arr2
        keys = [0 for _ in range(len(letters))]
    return arr


for i in range(100):
    ln = randint(1, 100)
    count = randint(1, 100)
    test_arr = ["".join(choice(letters) for i in range(ln)) for i in range(count)]
    arr_for_LSD_sort = test_arr.copy()
    test_arr.sort()
    arr_for_LSD_sort = lsd_radix_sort(arr_for_LSD_sort)
    assert arr_for_LSD_sort == test_arr
print("All Test Pass")