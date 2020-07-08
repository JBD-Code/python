#Python
# Python Data Type
# 문자열형(String) 3
#String Formatting 2
"""
    %s String
    %c character
    %d Imteger
    %f floating-pointer
    %o 8진수
    %x 16진수
    %% Literal% (문자 % 자체 )
"""

a = "I have %s apples " %3
print(a)
a = "rate is %s" %3.2453
print(a)

#formatting 연산자 %d와 %를 같이 쓸 때는 %%를 사용한다

b = "Error is %d%%" %98
print(b)

# 정렬과 공백
print("%10s" % "hi")
#위의 예문은 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽 정렬하고 나머지는
#공백으로 표기한다
print("%-10sjane" % "Hi")

#소수점 표현
#3.41231231을 소수점 네번째 자리까지만 나타내고 싶은 경우
print("%0.4f" % 3.41231231)
print("%10.4f" % 3.41231231)

#format 함수를 사용한 Formatting
# 숫자 바로 대입 
a = "I eat {0} apples".format(4)
print(a) 
# 문자 바로 대입
b= "I eat {0} apples".format("five")
print(b)
number = 3
day = "three"
b= "I ate %d apples. so i was sick for %s days" %(number, day)
print(b)

#이름으로 넣기
c= "I ate {number} apples. so i was sick for {day} days" .format(number=10, day=3)
print(c)

#인덱스와 이름을 함께 쓰기
c= "I ate {0} apples. so i was sick for {day} days" .format(4, day=3)
print(c)
