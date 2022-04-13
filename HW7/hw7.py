import pickle


def open_file_with_pickle(file: str):
    with open(file, 'rb') as file:
        data = pickle.load(file)
    return data


def format_and_len(word):
    black_list = ',.<>/;:"\'][}{-_!?&*%$#@`~=+)(1234567890'
    total_len = 0
    total_word = ''
    for letter in word:
        if letter in black_list:
            continue
        total_word += letter
        total_len += 1
    return total_word.lower(), total_len


def func1(data):
    total_dict = {i: 0 for i in range(10)}
    dict_all_word = {}
    for dict_ in data:
        massage = dict_['body'].strip().split()
        # massage - список не отформатированных слов
        for word in massage:
            word, len_ = format_and_len(word)
            if word in dict_all_word:
                dict_all_word[word] += 1
                if word in total_dict:
                    total_dict[word] += 1
                    continue
                min_word = min(total_dict, key=total_dict.get)
                min_word_val = total_dict[min_word]
                if min_word_val < dict_all_word[word]:
                    total_dict[word] = dict_all_word[word]
                    total_dict.pop(min_word)
                continue
            if len_ < 5:
                continue
            dict_all_word[word] = 1
    return list(total_dict)


def func2(data):
    all_len = sum(map(len, (dict_['body'].split() for dict_ in data)))
    len_data = len(data)
    return all_len/len_data


def func3(data, key='positive'):
    total_dict = {}
    for dict_ in data:
        if not dict_['edited']:
            if len(total_dict) < 10:
                total_dict[dict_['score']] = (dict_['author'], dict_['body'])
                continue
            if key == 'positive':
                min_in_dict = min(total_dict)
                if min_in_dict < dict_['score']:
                    total_dict[dict_['score']] = (dict_['author'], dict_['body'])
                    total_dict.pop(min_in_dict)
            elif key == 'negative':
                max_in_dict = max(total_dict)
                if max_in_dict > dict_['score']:
                    total_dict[dict_['score']] = (dict_['author'], dict_['body'])
                    total_dict.pop(max_in_dict)
    authors = []
    bodies = []
    for author, body in total_dict.values():
        authors.append(author)
        bodies.append(body)
    return bodies, authors


def func5(data, word):
    all_words = 0
    count = 0
    for dict_ in data:
        massages = dict_['body'].strip().split()
        for word_data in massages:
            word_data, _ = format_and_len(word_data)
            if word_data in ' ' or word_data.isdigit():
                continue
            all_words += 1
            if word_data == word.lower():
                count += 1
    return count/all_words


def number_in_massage(data):
    count = 0
    check_list = '1234567890'
    for dict_ in data:
        for number in check_list:
            if number in dict_['body']:
                count += 1
                break
    return count


def get_category(data):
    list_category = {}
    for dict_ in data:
        text = dict_['subreddit']
        if text in list_category:
            list_category[text] += 1
            continue
        list_category[text] = 1
    return list_category


def rus_letter(data):
    total_list = set()
    russian_letter = 'йцукенгшщзхъэждлорпавыфячсмитьбю'
    for dict_ in data:
        massages = dict_['body'].strip().split()
        for word in massages:
            for letter in russian_letter:
                if letter in word:
                    total_list.add(word)
    if total_list:
        return total_list
    return None


def main():
    data = open_file_with_pickle('data.pickle')
    print(func1(data))
    print(func2(data))
    print(func3(data))
    print(func3(data, key='negative'))
    print(func5(data, 'LOL'))
    print(number_in_massage(data))
    print(get_category(data))
    print(rus_letter(data))


if __name__ == '__main__':
    main()
