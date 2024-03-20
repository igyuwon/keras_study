score = int(input('Input your score : '))
if score > 100 or score < 0:
    print('Out of range') # block 1
elif score < 60:
    print('Fail') # block 2
elif score < 80:
    print('Pass') # block 3
# print('Not bad')# block 3
else:
    print('Pass & Excellent') # block 4