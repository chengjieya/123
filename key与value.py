# d = {10: 'cat', 20: 'dog', 30: 'pet', 20: 'zoo'}
# print(d)
# lst1 = [10, 20, 30, 40]
# lst2 = ['cat', 'dog', 'pet', 'zoo', 'car']
# ziobj = zip(lst1, lst2)
# print(ziobj)
# d = dict(ziobj)
# print(d)
# d = dict(cat=10, dog=20)
# print(d)
# t = (10, 20, 30)
# print({t: 10})
# print('max:', max(d))
# print('min:', min(d))
# print('len:', len(d))


d = {1001: '李梅', 1002: '王华', 1003: '张峰'}
# print(d)
# d[1004] = '张丽丽'
# print(d)
# keys = d.keys()
# print(keys)
# print(list(keys))
# print(tuple(keys))
# values = d.values()
# print(values)
# print(list(values))
# print(tuple(values))
# lst = list(d.items())
# print(lst)
# d = dict(lst)
# print(d)
# print(d.pop(1001))
# print(d)
# print(d.pop(1008, '不存在'))
# print(d.popitem())
# print(d)
# d.clear()
# print(d)
# print(bool(d))
import random
d = {item: random.randint(1, 100) for item in range(4)}
print(d)

lst = [1001, 1002, 1003]
lst2 = ['陈妹妹', '王一一', '李丽丽']
d = {key: value for key, value in zip(lst, lst2)}
print(d)
