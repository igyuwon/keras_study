lst = ['1,2,3,4,5,6,7,8,9', 'a,b,c,d,e,f,g', 'A,B,C,D,E,F,G']

tst = '\t\bgood, hello\b'
print(len(tst))
msg = tst.strip()
print(len(msg))
print(tst.split('oo'))

print(':::'.join(lst))