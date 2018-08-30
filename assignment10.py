import random

#Q1

f = open('test.txt', 'r')               # file open operation for f1
lines = f.readlines()
n = int(input('enter the number of lines you want to print from the end'))
print(lines[:n])

#Q2

f = open('test2.txt')
line = f.read()
split = line.split()
print(split)


#Q3

f2 = open('test.txt', 'w')
for l in lines:
    f2.write(l)
f2.close()                              # file close operation for f2

#Q4

f2 = open('output3.txt', 'a')
f3 = open('test2.txt', 'r')
for l in lines:
    li = f3.readline()
    f2.write(l + li)                    #the write concatenation does not ignore \n and also concatenate's it
f2.close()
f3.close()

#Q5

f2 = open('test5.txt', 'w')
for i in range(0, 100):
    s = str(random.randint(0, 1000)) + '\n'
    f2.write(s)
f2.close()
f3 = open('out5.txt', 'r+')
f2 = open('test5.txt', 'r')
e_line = f2.read()
e = e_line.split()
e.sort()
f3.write(str(e))
f2.close()
f3.seek(0)
print(f3)

# note that sorting in this program happens in context to string data type not integer
