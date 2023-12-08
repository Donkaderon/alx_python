#PROJECT 0
no_c = __import__('0-no_c').no_c

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))


#PROJECT 1
print_matrix_integer = __import__('1-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

#PROJECT 2
multiple_returns = __import__('2-multiple_returns').multiple_returns

sentence = ""
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

#PROJECT1-1
print_matrix_integer = __import__('1-print_matrix_integer').print_matrix_integer

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print_matrix_integer(matrix)