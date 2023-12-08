#P0
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

#P1
common_elements = __import__('1-common_elements').common_elements

set_1 = { "Python", "hmed", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl", "hmed" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

#P2
update_dictionary = __import__('2-update_dictionary').update_dictionary

def print_sorted_dictionary(my_dict):
    """ Print sorted dictionary """
    keys = sorted(my_dict.keys())
    for k in keys:
        print("{}: {}".format(k, my_dict[k]))

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

#P3 
best_score = __import__('3-best_score').best_score

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

#P4
multiply_list_map = __import__('4-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)