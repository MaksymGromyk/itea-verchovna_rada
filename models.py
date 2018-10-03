"""
. Якщо вік, зріст,  вага, імя, прізвище однакові -
вважати, що це той самий депутат. Закодити цю логіку.
Тобто не можна додати такого ж депутата якщо він вже існує у фракції.
. Закодити Клас БазаДанихВерховної ради. Реалізувати в ньому 2 статичних методи:
отримати верховну раду із бази даних
записати верховну раду в базу даних
"""


class Human():
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def __hash__(self):
        return hash(self.weight) + hash(self.height)

    def __eq__(self, other):
        return self.weight == other.weight and \
            self.height == other.height

    def __str__(self):
        return 'weight is {}, height is {}'.format(self.weight, self.height)


class Deputat(Human):
    def __init__(self, weight, height, last_name, first_name, bribe_taker=False):
        Human.__init__(self, weight, height)
        self.last_name = last_name
        self.first_name = first_name
        self.bribe_taker = bribe_taker

    def __hash__(self):
        return hash(self.weight) + hash(self.height) + hash(self.last_name) + \
            hash(self.first_name) + hash(self.bribe_taker)

    def __eq__(self, other):
        return self.weight == other.weight and \
            self.height == other.height and \
            self.last_name == other.last_name and \
            self.first_name == other.first_name and \
            self.bribe_taker == other.bribe_taker
    # [atr in atr in dir(self) if not atr.startswith("_") and not callable(atr)]

    def __str__(self):
        return 'Dossier:\n{} {} ({}kg, {}sm). Bribe amount = {}grn'.format(
            self.last_name, self.first_name, self.weight, self.height, getattr(self, 'bribe', 'Not bribetaker'))

    def give_tribute(self):
        if self.bribe_taker:
            bribe = int(input('What is your bribe?\n'))
            if bribe > 10000:
                print('He is not with us animore\n')
            else:
                # self.bribe = bribe if not self.bribe else self.bribe + bribe
                if getattr(self, 'bribe', None):
                    self.bribe += bribe
                else:
                    self.bribe = bribe
        else:
            print('You are not able to bribe him.\n')


class Fraction():
    def __init__(self, initialization):
        self.initialization = initialization

    def __set__(self):
        print('Deleted the deputat')
        self.initialization = Deputat(input('Enter the Dossier: \n'))

    def __delete__(self):
        print('Deleted the deputat')
        del self.initialization
        

    def bribers_sorted(self):
        pass

    def the_biiggest_briber(self):
        pass

    def all_deputats(self):
        pass

    def clean_up_from_dirt(self):
        pass

    def is_deputats_available(self):
        pass


class Verchovna_Rada():
    def add_fract(self):
        pass

    def dell_fract(self):
        pass

    def show_all_fract(self):
        pass

    def show_fract(self):
        pass

    def add_dept_to_fract(self):
        pass

    def del_dept_from_fract(self):
        pass

    def all_bribers(self):
        pass

    def all_deputats(self):
        pass

    def if_dept_in_vr(self):
        pass

    ''' . Якщо вік, зріст,  вага, імя, прізвище однакові -
    вважати, що це той самий депутат. Закодити цю логіку.'''
    def __hash__(self):
        pass

    def __eq__(self, other):
        pass


class BDVR():
    @staticmethod
    def get_vr():
        pass

    @staticmethod
    def push_vr():
        pass
