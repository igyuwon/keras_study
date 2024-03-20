class Score:
    def __init__(self, point = 0):
        self.point = point
    def set(self, p):
        self.point = p
    def get(self):
        return self.point

mine = Score(89)
print(mine.get())
mine.set(99)    #set에서 인스턴스변수 point가 만들어짐
print(mine.get())

yours = Score()
print(yours.get())