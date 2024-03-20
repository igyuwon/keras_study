'''
random 모듈을 이용하여 0~100사이의 정수 난수 10개를 생성하여 리스트에 저장하라.
리스트에 저장된 정수 중 가장 큰 수와 작은 수를 찾아 출력하라.
리스트의 메소드를 이용하여 가장 큰 수와 작은 수의 인덱스를 출력하라.
'''

import random

lst = []
#a = random.randint(0,100)
#print(a)

for n in range(0,10):
    lst.append(random.randint(0,100))
print(lst)

minIdx = 0
for i in range(1, len(lst)):
    if lst[i] > lst[minIdx]:
        minIdx = i
print(lst[minIdx], minIdx)


