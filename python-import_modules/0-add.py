a = 1
b = 2

add_module = __import__('add_0', fromlist=['add'])
result = add_module.add(a, b)
print("{} + {} = {}".format(a, b, result))