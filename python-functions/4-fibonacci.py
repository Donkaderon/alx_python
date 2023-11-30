def fibonacci_sequence(n):
    sequence = [0, 1]  

    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]  
        sequence.append(next_number)

    return sequence[:n]

print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))




    