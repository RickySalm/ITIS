import random
from abc import ABC, abstractmethod


class Warrior:
    def __init__(self, name='No name', max_hp=100, hp=None, race='not specified', gender=0, evasion_prob=0, buff=0.1):
        self.name = name
        self.max_hp = max_hp
        self.race = race
        self.gender = gender
        self.buff = buff
        self.evasion_prob = evasion_prob
        if hp:
            self.hp = hp
        else:
            self.hp = self.max_hp

    def attack(self, enemy, union):
        pass

    def __repr__(self):
        return f'раса - {self.race}\n пол - {self.gender}\n имя - {self.name}\n hp - {self.hp}'


class Human(Warrior):
    def __init__(self, race='Human'):
        super().__init__(race=race)

    def attack(self, enemy, union=None):
        if isinstance(enemy, Berserk):
            if random.random() <= 0.1 + enemy.buff:
                return False
        if isinstance(enemy, Shaman):
            if random.random() <= 0.7 + enemy.buff:
                return False
        return True


class Light(Human):
    def __init__(self, name=None, gender=None, evasion_prob=None):
        super().__init__()
        self.name = name
        self.max_hp = 200
        self.hp = self.max_hp
        self.gender = gender
        self.evasion_prob = evasion_prob

    def attack(self, enemy, union=None):
        if super().attack(enemy):
            damage = random.randint(30, 50)
            enemy.hp -= damage
            return f'произвел атаку на <org_army> <{enemy.name_of_class()}> <{enemy.name}> силой <{damage}>'
        return f'промахнулся по <org_army> <{enemy.name_of_class()}> <{enemy.name}>'

    def name_of_class(self):
        return 'Light'


class Heavy(Human):
    def __init__(self, name=None, gender=None):
        super().__init__()
        self.name = name
        self.max_hp = 600
        self.gender = gender
        self.evasion_prob = 0.0
        self.hp = self.max_hp

    def attack(self, enemy, union=None):
        if super().attack(enemy):
            damage = random.randint(50, 70)
            enemy.hp -= damage
            return f'произвел атаку на <org_army> <{enemy.name_of_class()}> <{enemy.name}> силой <{damage}>'
        return f'промахнулся по <org_army> <{enemy.name_of_class()}> <{enemy.name}>'

    def name_of_class(self):
        return 'Heavy'


class Druid(Human):
    def __init__(self, name=None, gender=None):
        super().__init__()
        self.name = name
        self.max_hp = 100
        self.gender = gender
        self.evasion_prob = 0.0
        self.hp = self.max_hp

    def attack(self, enemy, union=None):
        if random.random() <= 0.3:
            if isinstance(enemy, Shaman):
                return 'пропустил'
            else:
                enemy.hp = 10
            return f'<заразил> <org_army> <{enemy.name_of_class()}> <{enemy.name}>'
        else:
            if isinstance(union, Druid):
                return 'пропустил'
            else:
                union.hp = union.max_hp
            return f'<вылечил> <human_army> <{union.name_of_class()}> <{union.name}>'

    def name_of_class(self):
        return 'Druid'


class Org(Warrior):
    def __init__(self, race='Org'):
        super().__init__(race=race)

    def attack(self, enemy, union=None):
        if isinstance(enemy, Light):
            if random.random() <= 0.3 + enemy.buff:
                return False
        if isinstance(enemy, Heavy):
            if random.random() <= 0.0 + enemy.buff:
                return False
        if isinstance(enemy, Druid):
            if random.random() <= 0.7 + enemy.buff:
                return False
        return True


class Berserk(Org):
    def __init__(self, name=None, gender=None):
        super(Berserk, self).__init__()
        self.name = name
        self.max_hp = 600
        self.gender = gender
        self.evasion_prob = 0.0
        self.hp = self.max_hp

    def attack(self, enemy, union=None):
        if super().attack(enemy):
            damage = random.randint(60, 90)
            enemy.hp -= damage
            return f'произвел атаку на <human_army> <{enemy.name_of_class()}> <{enemy.name}> силой <{damage}>'
        return f'промахнулся по <human_army> <{enemy.name_of_class()}> <{enemy.name}>'

    def name_of_class(self):
        return 'Berserk'


class Shaman(Org):
    def __init__(self, name=None, gender=None):
        super().__init__()
        self.name = name
        self.max_hp = 120
        self.gender = gender
        self.evasion_prob = 0.0
        self.hp = self.max_hp

    def attack(self, enemy, union=None):
        if random.random() <= 0.5:
            if isinstance(enemy, Druid):
                return 'пропустил'
            else:
                enemy.hp = 10
            return f'<заразил> <human_army> <{enemy.name_of_class()}> <{enemy.name}>'
        else:
            if isinstance(union, Shaman):
                return 'пропустил'
            else:
                union.hp = union.max_hp
            return f'<вылечил> <org_army> <{union.name_of_class()}> <{union.name}>'

    def name_of_class(self):
        return 'Shaman'


def checking_defeat_army(org_army, human_army):
    if not org_army:
        print('Победила аримя - org_army')
        return True
    elif not human_army:
        print('Победила армия - human_army')
        return True
    return False


def play_the_game():
    human_army = [Light(), Heavy(), Druid(), Druid()]
    org_army = [Berserk(), Shaman(), Shaman(), Berserk()]
    flag = True
    while flag:
        for attacking in map(random.choice, (org_army, human_army)):
            if attacking in org_army:
                enemy = random.choice(human_army)
                # шаман
                if isinstance(attacking, Shaman):
                    union = random.choice(org_army)
                    output = attacking.attack(enemy, union)
                    print(f'<org_army> <{attacking.name_of_class()}> <{attacking.name}> {output} ')
                # воин
                else:
                    output = attacking.attack(enemy)
                    print(f'<org_army> <{attacking.name_of_class()}> <{attacking.name}> {output}')
                if enemy.hp <= 0:
                    print(f'<human_army>, <{enemy.name_of_class()}>, <{enemy.name}> убит в бою')
                    human_army.remove(enemy)
            else:
                enemy = random.choice(org_army)
                # друид
                if isinstance(attacking, Druid):
                    union = random.choice(human_army)
                    output = attacking.attack(enemy, union)
                    print(f'<org_army> <{attacking.name_of_class()}> <{attacking.name}> {output} ')
                # воин
                else:
                    output = attacking.attack(enemy)
                    print(f'<human_army> <{attacking.name_of_class()}> <{attacking.name}> {output}')
                if enemy.hp <= 0:
                    print(f'<org_army>, <{enemy.name_of_class()}>, <{enemy.name}> убит в бою')
                    org_army.remove(enemy)

            if checking_defeat_army(human_army, org_army):
                flag = False
                break


if __name__ == '__main__':
    play_the_game()


