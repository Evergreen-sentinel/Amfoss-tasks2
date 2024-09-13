f = open("input.txt",'r')
s = f.read()
f.close()

f = open("output.txt",'w')
f.write(s)
f.close()