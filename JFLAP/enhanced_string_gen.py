import itertools
output = open('./strings.txt', 'w')
MAX_LENGTH = 5
ALPHABET = ['a', 'b', 'c']
for length in range(1, MAX_LENGTH+1):
    for i in itertools.product(ALPHABET, repeat=length):
        output.write("".join(i) + '\n')
output.close()
