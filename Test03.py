#Python
# Python Data Type
# 문자열형(String) 2
# Pition 이라는 문자열을 Python으로 바꾸려고 하는 경우

a = "Pition"
print(a[:1])
print(a[2:])
print(a[:1] + "y" + a[2:])

#String Formatting
"""
"현재 온도는 18도 입니다"
"현재 온도는 20도 입니다" 

문자열 안의 특정한 값을 바꿔야 할 경우 가 있다
"""
a = "I eat %d apples." %3
print(a)
# 위의 코드 처럼 문자열 안에서 숫자를 넣고 싶은 자리에 %d를 넣어주고 삽입할 숫자 3은
# 가장 뒤에 있는 % 문자 다음에 써놓는다 %d를 문자열 포맷이라고 한다.

a = "I eat %s apples " %"five"
print(a)
#숫자를 넣기위해서는 %d를 써야 하고 문자열을 넣기 위해서는 %s를 써야 한다.
number =345
a = "I eat %s apples " %number
print(a)
#숫자를 나타내는 변수를 대입할 수 도 있다 .
#문자열 안에 1개 가 아닌 여러개 의 값을 넣을 경우

number = 10
day = "three"
b = "I ate %d apples. so Iwas sick for %s days." %(number, day)
print(b)
#마지막 % 다음 괄호 안에 , 로 구분하여 각각의 값을 넣는다



