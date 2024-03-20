'''
input()을 이용하여 사용자 입력을 받은 후 정수 값으로 변환할 때
숫자가 아닌 문자가 입력되면 정수로 변환하는 과정에 ValueError 예외가 발생한다.
반복문과 예외 처리를 이용하여 정상적으로 정수 변환이 가능하도록 프로그래밍 하라.
'''

isDone = False

while not isDone:
    try:
        n = int(input("숫자를 입력하세요 : "))
        isDone = True
    except ValueError:
        print('정수가 아닙니다.')
print(n)