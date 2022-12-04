import random

string = "ab"


def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


def shuffle_till_can(list_of_perms, num_of_alphas):
    counter = fact(len(list_of_perms[0])) / (fact(num_of_alphas - len(list_of_perms[0])) * fact(num_of_alphas))
    while counter - 1 > 0:
        temp_shuffeld_list = list(list_of_perms[0])
        random.shuffle(temp_shuffeld_list)
        temp_shuffled_string = ''.join(temp_shuffeld_list)
        if temp_shuffled_string not in list_of_perms:
            list_of_perms.append(temp_shuffeld_list)
            counter -= 1
    return list_of_perms


def permutations(s):
    start_list = []
    num_of_chars = 0
    start_list.append(s)
    if len(s) > 0:
        for i in s:
            s = s.replace(i, '')
            num_of_chars += 1
    return shuffle_till_can(start_list, num_of_chars)


print(permutations(string))
