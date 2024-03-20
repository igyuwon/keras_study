'''
info = {}
print(info)
info['age'] = 20
print(info)
'''

info = {'kor' : 90, 'ai' : 95, 'math' : 99}

print(info.keys())
print(info.values())
print(info.items())


info['kor'] = 95

total = 0
for v in info.values():
    total = total + v

print(total)