try:
    n = int(input('input number : '))
    print(100/n)
except ZeroDivisionError:
    print('0을 사용할 수 없음.')
except ValueError:
    print('입력에 문자가 포함됨.')
finally:
    print('End of program')