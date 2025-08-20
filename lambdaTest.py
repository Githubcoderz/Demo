from random import randint

lst = [randint(1, 100) for _ in range(10)]
print(lst)
sortListReverse = sorted(lst, key=lambda x: x, reverse=True)
print(sortListReverse)
sortList = sorted(lst, key=lambda x: x)
print(sortList)
lstOne = [('a', 60), ('b', 20), ('c', 99), ('d', 77)]
print(lstOne)
lstOneReverse = sorted(lstOne, key=lambda x: x[1], reverse=True)
print(lstOneReverse)