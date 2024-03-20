done = False
while not done: #True가 된다(할 일을 아직 완료하지 않았으면)
    value = int(input('data inputL'))
    if 0 <= value and value <= 100:
        break
    else:
        print('valid data range:0~100. Input again')
else:
    print('end of loop')
print('data:', value)