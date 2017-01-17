import random
dish = input('What would you like?')
if dish == ' ':
    lst = dish.split(', ')
    unique = set(lst)
    changeList = list(unique)
    for i,l in enumerate(changeList):
        time = random.randint(0, 1000)
        print(changeList[i].strip(' ').capitalize(),'.....',time,'minutes')
else:
  print('Input your dishes.')   
"""
не унікальні --- яйця(щось роблю не так з set)
є питання по for , якщо тільки одна змінна і --- помилка?


"""
