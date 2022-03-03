from matplotlib import pyplot as plt


class Point:
    def __init__(self, x, y, s):
        self.__x = x
        self.__y = y
        self.__s = s

    def __getitem__(self, key):
        total = None
        if key == 0:
            total = self.__x
        elif key == 1:
            total = self.__y
        elif key == 2:
            total = self.__s
        return total

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def s(self):
        return self.__s


def distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def read_data(path):
    with open(path, 'r', encoding='utf-8') as file:
        database = {}
        for line in file:
            address, *raw = line.strip().split('\t')
            database[address] = Point(*tuple(map(float, raw)))
    return database


def task1(database):
    count = -1
    maximum = 0
    coordinates = [None, None]
    for i in database:
        f_point = database[i]
        for j in database:
            s_point = database[j]
            total_dist = distance(f_point, s_point)
            if total_dist <= 0.5:
                count += 1
        if count > maximum:
            maximum = count
            count = -1
            coordinates[0] = f_point.x
            coordinates[1] = f_point.y
        else:
            count = -1
    return coordinates


def distance_house(main_point, index_min_point, other_points):
    for i in other_points:
        if i == other_points[index_min_point]:
            continue
        else:
            if distance(main_point, i) <= 1.0:
                return 0
            else:
                continue
    return 1


def task2(database: dict):
    count = -1
    list_coord = [Point(0, 0, 0)] * 10
    number_house = [0] * 10
    for i in database:
        f_point = database[i]
        for j in database:
            s_point = database[j]
            total_dist = distance(f_point, s_point)
            if total_dist <= 0.5:
                count += 1
        min_dist = min(number_house)
        if min_dist < count:
            index_min_dist = number_house.index(min_dist)
            if distance_house(f_point, index_min_dist, list_coord):
                number_house[index_min_dist] = count
                list_coord[index_min_dist] = f_point
                count = -1
            else:
                count = -1
        else:
            count = -1
    for i, el in enumerate(list_coord):
        list_coord[i] = (el.x, el.y)
    return list_coord


def counting_people(point):
    return (point.s*0.7)//18


def task3(database: dict):
    list_coord = [Point(0, 0, 0)] * 15
    people = [0] * 15
    count = 0
    for i in database:
        f_point = database[i]
        count += counting_people(f_point)
        for j in database:
            s_point = database[j]
            total_dist = distance(f_point, s_point)
            if total_dist <= 0.5:
                count += counting_people(s_point)
        min_number_people = min(people)
        if count > min_number_people:
            index_min_number_people = people.index(min_number_people)
            if distance_house(f_point, index_min_number_people, list_coord):
                people[index_min_number_people] = count
                list_coord[index_min_number_people] = f_point
                count = -1
            else:
                count = -1
        else:
            count = -1
    for i, el in enumerate(list_coord):
        list_coord[i] = (el.x, el.y)
    return list_coord


def plot(database, best_coords):
    """
    НЕ МЕНЯТЬ КОД!
    Отрисовка точек 2D
    Args:
        database (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
        best_coords (list): для задачи 1 это (x, y), для задачи 2-3 это [(x1,y1), (x2,y2) ... (xn,yn)]
    """
    plt.close()
    fig, ax = plt.subplots(figsize=(8, 8))
    plt.plot([coord[0] for coord in database.values()],
             [coord[1] for coord in database.values()], '.', ms=5, color='k', alpha=0.5)
    if isinstance(best_coords[0], tuple):
        for x, y in best_coords:
            circle = plt.Circle((x, y), 0.5, color='r', fill=False, zorder=2)
            ax.add_patch(circle)
        plt.plot([coord[0] for coord in best_coords],
                 [coord[1] for coord in best_coords], '.', ms=15, color='r')
    elif isinstance(best_coords[0], float):
        x, y = best_coords
        circle = plt.Circle((x, y), 0.5, color='r', fill=False, zorder=2)
        ax.add_patch(circle)
        plt.plot(*best_coords, '.', ms=15, color='r')
    else:
        raise ValueError("Проверь, что подаёшь список кортежей или кортеж из двух координат")
    plt.show()


def homework():
    path = "buildings.txt"
    database = read_data(path)
    best_task1 = task1(database)
    plot(database, best_task1)

    top10_task2 = task2(database)
    plot(database, top10_task2)

    top15_task2 = task3(database)
    plot(database, top15_task2)


if __name__ == '__main__':
    homework()
