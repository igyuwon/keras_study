kScore = 95
mScore = 98
total = kScore + mScore
average = total / 2
print('Total = ', total, 'Average = ', average)

#수와 논리값 표현의 예
data0 = 10
data0 = data0 + 0xF
data1 = 0x7+0b111
f1 = 3.14
f2 = 1e-2
isAlive = True
print(data0, data1 ,f1 + f2, isAlive)

#문자열에 대한 예
data = '철수와 친구들'
print(data)
print(data[0],data[4],data[6])
print(data[2:5])
print(data[:4])
print(data[2:])

#화면 출력의 간단한 예
n1 = 1
n2 = 2
print(n1, n2, n1+ n2, 'Good Morning')
print(n1, n2, n1+ n2, sep = '::')
print(n1, n2, n1+ n2, sep = '::', end = 'END')
print(n1 + n2, 0.00314e+3)

"""#키보드 입력의 예
width = input('width of rectangel ?? ')
width = int(width)
height = input('height of rectangle ?? ')
height = int(height)
print('area of rectangle : ', width * height)"""

"""#산술 연산의 예
n1 = int(input('Input the first number : '))
n2 = int(input('Input the second number : '))
print(n1 + n2, n1 * n2, n1 / n2, n1 // n2, n1 % n2) 
print( +n1, -n1)
print( n1 + - n2 ** 2 + 1) #연산 우선순위"""

#비트 연산자 사용 예
n = 0xFF # 0b1111_1111, 255
m = 7 # 0b0111
n_r4 = n >> 4 # 0b0000_1111
# print(n, n_r4)
print(n & m, n | m, n ^ m, ~n)

#대입 연산자 사용의 예
n1 = 10
n2 = 3
total = 0
print(total)
total += n1
print(total)
total += n2
print(total)
