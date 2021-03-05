output = open('./strings_ab.txt', 'w')
LENGTH = 5
d = { '0': 'a', '1': 'b' }
for i in range(2, 2**(LENGTH+1)):
    s = "".join(map(lambda x: d[x], bin(i)[2:]))
    output.write(s[1:] + '\n')
output.close()
