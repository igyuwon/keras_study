#print(1, 2, 3)
#print(1, 2, 3, end = '\n')
#print(1, 2, 3, end='hello')

def foo(a, b = 0, *c, **d):
    print(a, b, c, d)

foo(1)
foo(1, 2)
foo(1, 2, 3)
foo(1, 2, 3, 4, point = 100,  grade = "A")
