import random


def fact(num):  # factorial
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)


def combination_with_repitition(number_of_chars, length_of_word, deep_of_repetition):
    num_of_combinations = fact(length_of_word) / fact(length_of_word - number_of_chars)
    num_of_combinations = num_of_combinations / deep_of_repetition
    return num_of_combinations


def repetition_depth(string):
    repetition = 0
    for i in string:
        if string.count(i) > repetition:
            repetition = string.count(i)
    return repetition


def count_chars(string):
    counter_string = ''
    counter = 0
    for i in string:
        if i not in counter_string:
            counter_string = counter_string + i
            counter += 1
    return counter


def create_list_of_permuts(start_list, counter):
    while counter - 1 > 0:
        temp_list_of_shufels = list(start_list[0])
        random.shuffle(temp_list_of_shufels)
        temp_suffeld_string = ''.join(temp_list_of_shufels)
        if temp_suffeld_string not in start_list:
            start_list.append(temp_suffeld_string)
            counter -= 1
    return start_list


s = "saahtv"

counter = combination_with_repitition(count_chars(s), len(s), repetition_depth(s))

start_list = [s]

print(create_list_of_permuts(start_list, counter))
