class Animal:
    def __init__(self,d):
        self.dog = d
    def get(self):
        return self.dog
dog = Animal(4)
print(dog.get())