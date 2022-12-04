import random


def fact(num):  # factorial
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


def shuffle_till_can(list_of_perms, num_of_alphas):  # returns list with all permutations
    counter = fact(len(list_of_perms[0])) / ((fact(len(list_of_perms[0]) - num_of_alphas)) * fact(num_of_alphas))
    if counter == 1:
        counter = len(list_of_perms[0])
    while counter - 1 > 0:
        temp_shuffeld_list = list(list_of_perms[0])
        random.shuffle(temp_shuffeld_list)
        temp_shuffled_string = ''.join(temp_shuffeld_list)
        if temp_shuffled_string not in list_of_perms:
            list_of_perms.append(temp_shuffled_string)
            counter -= 1
    return list_of_perms


def permutations(s):  # main func
    start_list = []
    num_of_chars = 0
    counter_string = ''
    start_list.append(s)
    if len(s) > 0:
        for i in s:
            if i not in counter_string:
                counter_string = counter_string + i
                num_of_chars += 1
    return shuffle_till_can(start_list, num_of_chars)


string = "abba"

a = permutations(string)
print(a)
