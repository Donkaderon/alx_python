import sys

def print_arguments(argv):
    num_arguments = len(argv)
    if num_arguments == 0:
        print("0 arguments.")
        print(".")
    else:
        if num_arguments == 1:
            print("1 argument:")
        else:
            print(f"{num_arguments} arguments:")
        
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
    print()
      
if __name__ == "__main__":
    print_arguments(sys.argv[1:])