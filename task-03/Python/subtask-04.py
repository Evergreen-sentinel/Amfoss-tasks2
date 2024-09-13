def print_star_pattern(n):

    pattern = ""

    for i in range(1, n + 1, 2):
        pattern += ' ' * ((n - i) // 2) + '*' * i + '\n'


    for i in range(n-2, 0, -2):
        pattern += ' ' * ((n - i) // 2) + '*' * i + '\n'

    return pattern

f = open("input2.txt",'r')
s = int(f.read())
f.close()

pattern = print_star_pattern(s)

f = open("output2.txt",'w')
f.write(pattern)
f.close()
