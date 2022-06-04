def func1(string):
    check_list = '123'
    total = ''
    buf = ''
    for i in string:
        if i in check_list:
            buf += i
        else:
            if len(buf) > len(total):
                total = buf
                buf = ''
    return total
print(func1('13222221232125112300312112782140'))

def func2(data):
    all_val = {}
    for key, val in data.items():
        if val in all_val:
            all_val[val][0] += 1
            all_val[val].append(key)
        else:
            all_val[val] = [1, key]

    print(all_val)
    max_ = 0
    total = None
    for key, val in all_val.items():
        if val[0] > max_:
            max_ = val[0]
            total = val[1:]
    return total


a = {1: 'РНР', 2: 'РНР', 3: 'Python', 4: 'РНР', 5: 'Python', 6: 'JS', 7: 'Python' , 8: 'Python' , 9: 'РНР' , 0: 'Python'}
print(func2(a))

def func3(text):
    check_list = '1234567890'
    text_f = ''
    for i in text:
        if i in check_list:
            text_f += text[text.index(i):]
            break
    text_f = text_f[::-1]
    text_end = ''
    for i in text_f:
        if i in check_list:
            text_end += text_f[text_f.index(i):]
            break

    return text_end[::-1]
text = "I'll have two number 9s, а number 9 large, а number 6 with extra dip, а number 7, two number 45s, one with cheese, and а large soda"
print(func3(text))
