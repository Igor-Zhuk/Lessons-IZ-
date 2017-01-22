import random


class Dishes():
    def __init__(self, dishes):
        self.name = dishes.split(',')
        self.dish_name = [el.strip().capitalize() for el in self.name]
        self.uniqueList = list(set(self.dish_name))
    def calc_time(self):
        return random.randint(1,60)
    

dishes = input('What would you like?\n')
p = Dishes(dishes)
for i in range(len(p.uniqueList)):
    if p.uniqueList[i].strip() == '':
        print('No dishes')
    else:
        if len(p.uniqueList[i]) < 14:
            print(p.uniqueList[i],(17 - len(p.uniqueList[i]))*'.',p.calc_time())