value = 0
while value <= 0 or value > 100:
    value = int(input('input number(1~100) : '))
total = 0
for val in range(1, value + 1):
    if val % 2 == 0:
        total = total + val
print(total)