def reverse(number):
    if isinstance(number, (int, float)):
        number = str(number)
        number = number[::-1]
    return number


def no_dup(mydict):
    total_dict = {}
    for key in mydict:
        if mydict[key] in total_dict.values():
            continue
        else:
            total_dict[key] = mydict[key]
    return total_dict


def summarize(number):
    sum = 0
    if number >= 10:
        for i in str(number):
            sum += int(i)
        return summarize(sum)
    else:
        return number


def brick_lang(string):
    total_string = ''
    glasn = 'уеыаоэяиюё'
    for i in string:
        if i in glasn:
            total_string += i + 'к' + i
        else:
            total_string += i
    return total_string


# def bonus(text, string):
#     max_string = None
#
#     for el in text:
#         if el in string:
#             max_string += el
#         else:
#             if set(string) not in max_string:






