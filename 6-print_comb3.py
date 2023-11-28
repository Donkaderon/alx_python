full_number = ""
big_full_number = ""

for i in range(0, 80):
    number = "{:02d}".format(i)
    full_number += number + ","
    #big_full_number = full_number + "89"
    print(full_number)