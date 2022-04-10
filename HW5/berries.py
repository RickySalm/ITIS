class Raspberry:
    @staticmethod
    def states():
        states = ['missing', 'flowering', 'green', 'red']
        return states

    def __init__(self, index):
        self._index = index
        self._state = Raspberry.states()[0]

    def is_ripe(self):
        if self._state == Raspberry.states()[-1]:
            return True
        else:
            return False

    def grow(self):
        index_now_state = Raspberry.states().index(self._state)
        if not self.is_ripe():
            self._state = Raspberry.states()[index_now_state + 1]


class RaspberryBush:
    def __init__(self, number_of_raspberries):
        self.raspberries = [Raspberry(index) for index in range(number_of_raspberries)]

    def grow_all(self):
        for berries in self.raspberries:
            berries.grow()

    def all_are_ripe(self):
        for berries in self.raspberries:
            if not berries.is_ripe():
                return False
        return True

    def give_away_all(self):
        self.raspberries = None


class Human:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self.work()
        else:
            print('Еще рано собирать ягодки')

    @staticmethod
    def knowledge_base():
        text = 'Осенью лучше сажать малину с середины августа до начала октября, ' \
               'но не позднее двух недель перед замерзанием почвы. ' \
               'Посадочное место готовим так, как было описано выше. ' \
               'Корни каждого саженца расправляют и присыпают землей. ' \
               'Побеги после посадки обрезают и обильно поливают.'
        print(text)
