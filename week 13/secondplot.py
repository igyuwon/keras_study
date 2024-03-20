import matplotlib.pyplot as plt
import random
lst = [1,2,5,3,7]
plt.title('test', fontdict={'size' : 30, 'color' : 'red'}, pad=20)
plt.xlabel('X-----', fontdic={'size' : 25})
plt.plot([0,1,2,3,4,],lst,'r^:') #x축 값과 색과 마커 추가 b : 파란색, k : 검정색
plt.show()