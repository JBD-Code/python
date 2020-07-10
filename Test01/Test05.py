#Python
# Python Data Type
# 문자열형(String) 4
# 정렬
#왼쪽 정렬
print("{0:<10}".format("Hello"))
#:<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 설정

#오른쪽 정렬
print("{0:>10}".format("Hello"))
#:<10 표현식을 사용하면 치환되는 문자열을 오른쪽으로 정렬하고 문자열의 총 자릿수를 10으로 설정

#가운데 정렬
print("{0:^10}".format("Hello"))


# 공백 채우기
print("{0:=^10}".format("Hello"))
print("{0:!^10}".format("Hello"))
print("{0:<^10}".format("Hello"))
print("{0:>^10}".format("Hello"))
print("{0:x>10}".format("Hello"))
print("{0:x<10}".format("Hello"))

# 소수점 표현하기
y= 3.14232323
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

# 문자열 formatting
name = "홍길동 "
age = 30
print(f"나의 이름은 {name}입니다. 나이는 {age} 입니다")
print(f"나는 내년이면 {age +1} 살이 됩니다")

#Python Dictionary Type Key Value 를 한 쌍으로 갖는 자료형
d = {"name": "홍길동", "age":30}
print(f"나의 이름은 {d['name']} 입니다 나이는 {d['age']+2} 입니다")

#정렬
print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":^10}')

#공백 채우기
print(f'{"hi":=^10}')
print(f'{"hi":!<10}')
print(f'{"hi":^>10}')

y = 3.42134234
print(f'{y:0.4f}')
print(f'{y:10.4f}')

# 문자열 관련 함수

# 1 문자 세기
a = "hobby"
print(a.count("b"))
a ="Hello World Python"
print(a.find("o"))
print(a.find("x"))
# 만약 찾는 문자나 문자열이 존재하지 않는다면 -1 을 반환 한다

a = "Life is too short"
print(a.index("t"))
# print(a.index("k"))
# find 함수와 다른 점은 존재하지 않는 문자열을 찾는 다면 오류를 발생 시킨다


# 문자열 삽입

print(",".join("Python"))
print(a.upper())
print(a.lower())
a = " Hi "
print(a.rstrip()) # 오른쪽 공백 지우기
print(a.strip())# 양쪽 공백 지우기
print(a.lstrip()) # 왼쪽 공백 지우기

# 문자열 바꾸기

a = "Life is too short"
print(a.replace("Life", "Your leg"))

#문자열 나누기
print(a.split())
b = "a:b:c:d:e"
print(b.split(":"))