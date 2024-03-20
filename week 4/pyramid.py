class Pyramid:
    def __init__(self,height):
        #self.height = height
        self.set(height)    #값을 변경하는 건 일원화

    def set(self,height):
        self.height = height    #실제로 값 설정
    def show(self):
        for i in range(1, self.height+1):
            print(' ' * (self.height - i) + '#' * (i * 2 - 1))
    def getBlock(self):
        total = 0   #총 블록의 수
        for i in range(1, self.height + 1):
            total = total + (i * 2 - 1)
        return total
"""
p = Pyramid(5)
p.show()
print(p.getBlock())
p.set(7)
p.show()

print(__name__)
"""
