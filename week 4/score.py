#import pyramid
from pyramid import Pyramid

class Score:
    def set(self, p):
        self.point = p
    def get(self):
        return self.point

mine = Score()

mine.set(99)    #set에서 인스턴스변수 point가 만들어짐
print(mine.get())

print(__name__)

p = Pyramid(3)
p.show()