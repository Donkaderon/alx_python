def safe_print_division(a, b):
    try:
        x = a / b
        print(x)
    except ZeroDivisionError:
        print("Oops! b must not be equal to 0")
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
            print("Inside result: None")
            return None
    finally:
        if 'result' in locals():
            print("Inside result: {}".format(result))
            return result
