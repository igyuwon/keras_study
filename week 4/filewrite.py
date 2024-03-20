fd = open('data.dat', 'w') #step 1

fd.write('good morning\n')  #step 2
fd.write(str(3.14)+ '\n')

fd.close()  #step 3
###########
fd = open('data.dat', 'r')
print(fd.read())
fd.close()
###########
fd = open('data.dat', 'r')
'''
line1 = fd.readline()
print(line1)
line1 = fd.readline()
print(line1)
'''
for line in fd.readlines():
    print(line)
fd.close()