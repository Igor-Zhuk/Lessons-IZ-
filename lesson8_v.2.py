import random

dishes = input('What would you like?\n')

dishes = dishes.split(',')

lst = [el.strip().capitalize() for el in dishes]

lst = list(set(lst))

for i in range(len(lst)):
    time = random.randint(0, 60)

    if lst[i].strip() == '':
        print('No dishes')

    else:
        if len(lst[i]) < 14:
            print(lst[i],(17 - len(lst[i]))*'.',time)
        else:
            print(lst[i],time)
