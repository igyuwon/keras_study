# 1. 연도를 입력 받는다.
year = int(input('연도를 입력하세요 : '))

# 2. 윤년 판단 조건문을 세운다.
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    # 3-1. 윤년 판단 조건에 따라 출력을 한다.
    print('윤년입니다.')
else:
    # 3-2. 윤년 판단 조건에 따라 출력을 한다.
    print('평년입니다.')