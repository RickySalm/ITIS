from bs4 import BeautifulSoup


def new_num_base(link):
    with open(f'{link}', encoding='utf-8') as num_base:
        return [data.strip().split(';')[0:3] for data in num_base if 'Татарстан' in data]


def only_digit(text, add=False):
    new_text = ''
    text = text.strip()
    if add:
        for el in text:
            if el.isdigit() or el == '.':
                new_text += el
            else:
                break
        return float(new_text)
    else:
        for el in text:
            if el.isdigit():
                new_text += el
        return new_text


num_data = new_num_base('9_ABC.csv') + new_num_base('8_ABC.csv') + new_num_base('4_ABC.csv') + new_num_base('3_ABC.csv')
db = []
with open('page.html', encoding='utf-8') as file:
    result = open('result.txt', 'w', encoding='utf-8')
    soup = BeautifulSoup(file, 'lxml')
    for teg in soup.find_all('div', attrs={'class': 'apartament-info'}):
        title = teg.find_all('h5', attrs={'class': 'apartament-title'})[0].text.split(',')
        if ('3' in title[0]) and (45 <= only_digit(title[1], True) <= 65) and (3 <= only_digit(title[2], True) <= 15):
            user_num = teg.find_all('div', attrs={'class': 'mobile-number'})[0].text
            format_user_num = only_digit(user_num)[1:]
            for base_num in num_data:
                if base_num[0] == format_user_num[0:3]:
                    if int(base_num[1]) <= int(format_user_num[3:]) <= int(base_num[2]):
                        format_title = ''.join(title)
                        result.write(f'{(format_title + " " + user_num)}\n')

    result.close()
