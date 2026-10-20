# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
sequence = []
if L > 0:
    sequence.append(0)
    for k in range(1, L):
        previous = sequence[k-1]
        candidate = previous - k
        if candidate > 0 and candidate not in sequence:
            sequence.append(candidate)
        else:
            sequence.append(previous + k)
            





# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence