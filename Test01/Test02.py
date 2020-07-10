#Python
# Python Data Type
# 문자열형(String)
"""
    Python 에서 String 란 문자 단어로 구성된 문자들의 집합
    "Life is too short You need Python"
    "a"
    "123"

    문자열 생성 방법
    1. 큰 따옴표로 (")로  양쪽 둘러싸기
    "Hello World"
    2. 작은 따옴표로 (')로 양쪽 둘러싸기
    'Python'
    3. 큰 따옴표 세개를  연속으로 써서 양쪽 둘러싸기
    4. 작은 따옴표 세개를 연속으로 써서 양쪽 둘러싸기
"""
a = """Python"""
print(a)
b= '''Hello World!'''
print(b)

# 문자열에 작은 띠옴표 포함 시키기
# Python's favorite food is perl 을 출력할 때는 큰 따옴표로 둘러싼다
food = "Python's favorite food is perl"
print(food)

# 문자열에 큰 띠옴표 포함 시키기
# He Say "Python is vert easy." he say. 을 출력할 때는 작은 따옴표로 둘러싼다
say = 'He Say "Python is vert easy." he say.'
print(say)
# 백슬래시를 이용해 작은 따옴표와 큰 띠옴표 포함 시키기

food = 'Python\'s favorite food is perl'
print(food)
say = 'He Say \"Python is vert easy.\" he say.'
print(say)

#여러 줄의 문자열을 변수에 대입하고 싶을 떼
"""
    Life is too short 
    You need Python
"""
multiline = "Life is too short \nYou need Python"
print(multiline)

# 문자열 더하기
head = "Python\t"
tail = "is Fun!"
print(head+ tail)

#문자열 곱하기
print(head*2)

print("="*50)
print("My Python")
print("="*50)

#문자열 길이 구하기 len함수를 이용한다
str1 = "aaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbb"
print(len(str1))

#문자열 indexing
a = "Life is too long, You need Money!"
print(a[3])
print(a[-1])
#문자열을 뒤에서 부터 읽기 위해서는 Index에 - 를 붙인다

#문자열 Slicing
print(a[0:2])
#slicing 기법으로 a[시작 번호 : 끝 번호 ]를 지정할 때 끝 번호에 해당하는 것은 포함하지않는다
# print(a[0:2])을 수식으로 0 <= a <3 표현가능하다
print(a[0:4])
print(a[0:5])
# 공백 역시 문자와 동일하게 취급된다는 것을 주의하도록 하자
# a[사작 번호 : 끝 번호 ] 에서 끝 번호 부분을 생략 하면
# 시작 번호 부터 그 문자열의 끝까지를 뽑아 낸다
print(a[0:])


# a[사작 번호 : 끝 번호 ] 에서 시작 번호 부분을 생략 하면
# 끝 번호 부터 그 문자열의 처음까지를 뽑아 낸다
print(a[:33])

# a[사작 번호 : 끝 번호 ] 에서 시작 번호 와 끝 번호 부분을 생략 하면
# 그 문자열의 처음부터를 뽑아 낸다
print(a[:])

today = "20200705Rain"
year = today[:4]
day= today[4:8]
weather= today[8:]
print(year)
print(day)
print(weather)
