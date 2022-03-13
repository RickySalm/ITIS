def f1(f_list, s_list):
    f_list.sort()
    s_list.sort()
    return f_list == s_list


def f2(f_tuple, s_tuple):
    return f_tuple + s_tuple


def f3(list, d):
    total_tuple = *(x for x in list if x >= d),
    total_list = [x for x in list if x < d]
    return total_tuple, total_list


def f4(list):
    for i in range(len(list)):
        if list[i] != list[-i-1]:
            return False
    return True


def f5(list):
    total_list = [index for index, el in enumerate(list) if el != 0]
    return total_list


def f6(list, num):
    list_razn = [abs(x-num) for x in list]
    return list[list_razn.index(min(list_razn))]


def f7(list):
    list = sorted(list)
    total = [list[-1], list[-2], list[-3]]
    return total


def f8(list):
    len_list = len(list)
    if len_list % 2 == 0:
        f = (len_list // 2) - 1
        del list[f]
        del list[f]
    else:
        f = (len_list // 2)
        del list[f]
    return list


def f9(num):
    t = num
    num = abs(num)
    num = str(num)
    a = len(num)
    b = 0
    arr = []
    while a != 0:
        a -= 1
        arr.append(int(num[b]) * 10**a)
        b += 1
    for i in range(len(arr)):
        arr[i] = str(arr[i])
    if t >= 0:
        print(" + ".join(arr))
    else:
        print("-", " - ".join(arr))


def f10(*args):
    total_list = []
    list = tuple(args)
    start = 0
    end = 4
    cycle = len(args)/4
    while cycle > 0:
        total_list.append(list[start:end])
        start = end
        end += 4
        cycle -= 1
    return total_list
