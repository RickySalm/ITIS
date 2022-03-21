def f1(f_list, s_list):
    f_list.sort()
    s_list.sort()
    return f_list == s_list


def f2(f_tuple, s_tuple):
    return f_tuple + s_tuple


def f3(list_, d):
    total_tuple = *(x for x in list_ if x >= d),
    total_list = [x for x in list_ if x < d]
    return total_tuple, total_list


def f4(list_):
    for i in range(len(list_)):
        if list_[i] != list_[-i - 1]:
            return False
    return True


def f5(list_):
    total_list = [index for index, el in enumerate(list_) if el != 0]
    return total_list


def f6(list_, num):
    list_razn = [abs(x-num) for x in list_]
    return list_[list_razn.index(min(list_razn))]


def f7(list_):
    list_ = sorted(list_)
    total = [list_[-1], list_[-2], list_[-3]]
    return total


def f8(list_):
    len_list = len(list_)
    if len_list % 2 == 0:
        f = (len_list // 2) - 1
        del list_[f]
        del list_[f]
    else:
        f = (len_list // 2)
        del list_[f]
    return list_


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
    list_ = tuple(args)
    start = 0
    end = 4
    cycle = len(args)/4
    while cycle > 0:
        total_list.append(list_[start:end])
        start = end
        end += 4
        cycle -= 1
    return total_list

# превраитить из 2D
# [[1,2,3], [2], [4,5,6], [0]]
# в 1D
# [1,2,3,2,4,5,6,0]
k = [[1,2,3], [2], [4,5,6], [0]]
l = [b for x in k for b in x ]
print(l)
