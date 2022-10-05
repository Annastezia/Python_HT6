from random import randint

def fillList(size):
    return [randint(0, 10) for _ in range(size)]

def uniqueValues(list):
    return [a for a in set(list)]

size = int(input('Введите кол-во чисел: '))

startList = fillList(size)
print(startList)
print(uniqueValues(startList))