if __name__ == "__main__":
    a = 10
    b = 30

    add_module = __import__('add_0')
    add_function = getattr(add_module, 'add')
    result = add_module.add(a, b)
    output = "{} + {} = {}\n".format(a, b, result)
    print(output)