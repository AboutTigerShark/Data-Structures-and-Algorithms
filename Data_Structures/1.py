# coding:utf-8

# 列表推导式
def squared(x):
    return x*x

multiples = [squared(i) for i in range(30) if i % 3 is 0]
print(multiples)

# 字典推导式
mcase = {'a': 10, 'b': 34}
mcase_frequency = {v: k for k, v in mcase.items()}
print(mcase_frequency)

# 集合推导式
squared = {x**2 for x in [1, 1, 2]}
print(squared)