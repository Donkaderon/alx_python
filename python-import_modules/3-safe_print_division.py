def safe_print_division(a, b):
    try:
        x = a / b
        print(x)
    except ZeroDivisionError:
        print("Oops! b must not be equal to 0")

    finally:
        if 'result' in locals():
            print("Inside result: {:.1f}".format(result))
            print("{:d} / {:d} = {:.1f}".format(a, b, result))
        else:
            print("Inside result: None")
            print("{:d} / {:d} = None".format(a, b))
