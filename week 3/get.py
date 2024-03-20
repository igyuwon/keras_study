def get():
    def calc(a,b):
        return a+b
    return calc

n = get()
i = n(1,2)

print(i)
