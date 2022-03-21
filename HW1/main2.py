def open_file(f):
    def wrapper(arg):
        with open(arg, 'r', encoding='UTF-8') as file:
            file = [line.strip('\n').split() for line in file]
            file = list(filter(None, file))
        return f(file)
    return wrapper


@open_file
def number_of_words(file):
    count_word = 0
    for i in file:
        count_word += len(i)
    print('кол-во слов:', count_word)
    """
    def count_words(file):
        return sum([len(par.split()) for par in file])
    """


@open_file
def average_word_length(file):
    count_letter = 0
    count_word = 0
    for i in file:
        for j in i:
            count_word += 1
            count_letter += len(j)
    print('средняя длина слов', count_letter / count_word)


@open_file
def number_of_letters(file):
    a = set()
    count_let = 0
    for i in file:
        for j in i:
            count_let += len(j)
            a.add(len(j))
    print('кол-во букв', count_let)


@open_file
def number_of_rows(file):
    print('кол-во абзацев', len(file))


@open_file
def top_words_by_length(file):
    dict_word = {}
    list_word = []
    for i in file:
        for j in i:
            if len(list_word) != 10:
                list_word.append(j)
            else:
                for _ in list_word:
                    if len(_) < len(j):
                        list_word[list_word.index(_)] = j
                        break
    for i in list_word:
        dict_word[i] = len(i)
    print('топ слов по длине', dict_word)


@open_file
def frequent_letters(file):
    dict_letters = {}
    maximum_frequency = {}
    for i in file:
        for j in i:
            for let in j:
                if let in dict_letters:
                    dict_letters[let] += 1
                else:
                    dict_letters.update({let: 1})
    top_num = sorted(dict_letters.values())[-1:-11:-1]
    for key, val in dict_letters.items():
        if val in top_num:
            maximum_frequency[key] = val
    print('топ самых частых букв', maximum_frequency)


def replacing_words(file, replaced_words, rigth_words):
    file_ = open(file, 'r', encoding='UTF-8')
    text = file_.read()
    file_.close()
    file_ = open(file, 'w', encoding='UTF-8')
    file_.write(text.replace(replaced_words, rigth_words))
    file_.close()


def russian_update(file, sec_file):
    start = open(file, 'r', encoding='utf-8')
    fin = open(sec_file, 'w', encoding='utf-8')
    text = start.read()
    russ_letters = 'ейцукнгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ '
    last_letter = None
    for i in text:
        if i in russ_letters:
            if last_letter == ' ' and i == ' ':
                continue
            else:
                last_letter = i
                fin.write(i)
    start.close()
    fin.close()


def main():
    file = 'book2.txt'
    number_of_words(file)
    average_word_length(file)
    number_of_letters(file)
    number_of_rows(file)
    top_words_by_length(file)
    frequent_letters(file)
    replacing_words(file, "Анна Павловна", "anna pavlovna")
    russian_update(file, 'book4.txt')


if __name__ == '__main__':
    main()
