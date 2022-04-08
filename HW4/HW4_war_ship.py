from random import randint


class Game:
    def __init__(self, row=7, col=7, quantity_ships=10):
        self.row = row
        self.col = col
        self.field_for_show = [['~' for _ in range(col)] for _ in range(row)]
        self.quantity_ships = quantity_ships

        # генерируем поле с пустыми ячейками
        field = [['' for _ in range(col)] for _ in range(row)]
        cycle = 0
        # генерируем рандомные коорд. для кораблей
        while cycle != quantity_ships:
            row_ship = randint(0, row - 1)
            col_ship = randint(0, col - 1)
            # если на полученных коорд. нет корабля то добавляем
            if field[row_ship][col_ship] == '':
                field[row_ship][col_ship] = 's'
                cycle += 1
            else:
                continue
        self.field = field

    def show_field(self):
        """
        Показывает поле игры пользователю
        """
        for i in self.field_for_show:
            print(i)

    def end_the_game(self):
        """
        проверяет факт окончание игры

        Returns:1 если все корабли подбиты
                2 если есть неподбитые корабли
        """
        hit = 0
        for row in self.field_for_show:
            for el in row:
                if el == 'X':
                    hit += 1
        if hit == self.quantity_ships:
            return 1
        return 0

    def hit_check(self, row_shot, col_shot):
        """
        В зависимости от того попал или нет изменяет ячейки поля
        Args:
            row_shot: координата строки для выстрела
            col_shot: координата столбца для выстрела
        """
        row_shot -= 1
        col_shot -= 1
        if self.field[row_shot][col_shot] == 's':
            self.field[row_shot][col_shot] = 'pass'
            self.field_for_show[row_shot][col_shot] = 'X'
        elif self.field[row_shot][col_shot] == 'pass':
            print('Эта клетка уже известна! ')
        else:
            self.field_for_show[row_shot][col_shot] = '0'
            self.field[row_shot][col_shot] = 'pass'


def mode_selection():
    """
    функция для выбора режима игры: можно задать свои аргументы или
    использовать стандартные

    Returns: экземпляр класса Game

    """
    comment_exit = 'Для выхода напишите "quit"\n'
    mode = int(input('Выбор режима:\nПо умолчанию-1\nИзменить параметры-2\n'))
    if mode == 1:
        print(comment_exit)
        field = Game()
    elif mode == 2:
        text = 'Укажите кол-во строк, столбцов поля и кол-во короблей: '
        row, col, quantity = map(int, input(text).split())
        print(comment_exit)
        field = Game(row, col, quantity)
    else:
        print('Неправильный ввод')
        field = None
    return field


def take_coordinate():
    """
    Принимает у пользователя координаты

    Returns:tuple('quit', 'quit') - если подали аргумент 'quit'
            tuple(int(arg), int(*arg)) - если подали аргумент два числа
            tuple(-1, -1) - если подали 1 число
    """
    row, *col = input('Укажите номер строки и столбца : ').split()
    if row == 'quit':
        return 'quit', 'quit'
    if len(col):
        return int(row), int(col[0])
    return -1, -1


def main():
    my_field = mode_selection()
    flag = True
    while flag:
        my_field.show_field()
        # если все корабли подбиты, выходим
        if my_field.end_the_game():
            print('Вы прошли игру!!!')
            break
        row, col = take_coordinate()
        # проверяем команду на выход
        if (row or col) == 'quit':
            break
        # проверяем валидность указанных коорд.
        elif (1 <= col <= my_field.col) and (1 <= row <= my_field.row):
            my_field.hit_check(row, col)
        else:
            print('координаты введены не верно')


if __name__ == '__main__':
    main()
