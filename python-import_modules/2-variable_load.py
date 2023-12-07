if __name__ == "__main__":
    add_module = __import__('variable_load_2')
    add_function = add_module.a
    print(add_function)