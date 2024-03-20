def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i), "*" * (2 * i - 1))
    return n

x = int(input('층 : '))
pyramid(x)

'''
def pyramid(height):
    for level in range(1, height + 1):
        print((" " * (height - level)) +("*") * (level * 2 - 1) )
        #print((' '* ())+('*' * ()))
        
pyramid(7)
'''

