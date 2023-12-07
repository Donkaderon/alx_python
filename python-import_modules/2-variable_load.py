add_module = __import__('variable_load_2')
add_function = getattr(add_module, 'a')
print(add_function)