'''
class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """
    pass

for i in range(4):
    u = User()
print(u.id)
'''

def test_args_kwargs(arg1, arg2, arg3):
    print ("arg1:", arg1)
    print ("arg2:", arg2)
    print ("arg3:", arg3)

arg = (4,8,9)
test_args_kwargs(*arg)

