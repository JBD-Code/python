#Python
# Python 내장함수
# 활용빈도가 높고 중요한 함수를 정리

#abs(x)
#어떤 숫자를 입력받았을 때 그 숫자의 절대값을 돌려주는 함수
print(abs(3))
print(abs(-3))
print(abs(-1.434))

#all(x)
#반복 가능한 (iterable) 자료형 x를 입력 인수로 받으면 이 x의 요소가
#모두 참이면 True, 거짓이 하나다로 있으면 False를 반환한다


print(all([1, 2, 3]))
print(all([1, 2, 0]))
print(all([]))

#any(x)
#반복가능한 (iterable)자료형 x를 입력 인수로 받으며 x 의 요소 중
#하나라도 참이 있으면 True 를 x가 모두 거짓일때에만 False를 반환한다

print(any([1,2,0]))
print(any([0,0,0]))
print(any([0, ""]))
print(any([]))

#chr
#chr(i)는 ASCII 코드 값을 입력받아 그 코드에 해당하는 문자를 출력한다

print(chr(97))
print(chr(48))

#dir
#dir은 객체가 자체적으로 가지고 있는 함수, 변수를 보여준다
print(dir([1,2,3]))
print(dir({"1":"a"}))

#divmod
#divmod(a,b)는 2개의 숫자를 입력받고 a를 b호 나눈 몫과 나머지 tuple 형태로 반환
print(divmod(7, 4))
print(7//4)
print(7%4)

#enumerate
#enumerate는 열거하다는 뜻히아 이 함수는 순서가 있는 자료형(list. tuple, String)를
#입력받아 index값은 포함하는 enumerate객체를 반환
for i, name in enumerate(["header", "body", "footer"]):
    print(i, name)

#eval
#eval(expression)은 실행 가능한 문자열(1+2, "hi" + "a")을 입력받아 문자열을 실행한
#r결과값을 반환한다
print(eval("1+2"))
print(eval('"Hello" + "Python"'))
print(eval("divmod(4,3)"))

#filter
#filter 함수는 첫 번째 인수로 함수 이름을 두 번째 인수로 그 함수에 차례로 들어갈 자료형을 받는다
#그리고 두 번째 인수인 반복 가능한 자료형을 첫번째 인수인 함수에 입력되었을 때 반환값이
#참인것 만 묶어서 반환한다

def positive(I):
    result=[]
    for i in I:
        if i > 0 :
            result.append(i)
    return result
print(positive([1, -3, 2, 0, -5, 6]))

#위 에서 만든 positive 함수는 리스트를 입력값으로 받아 각각의 요소를 판별 양수값만 반환한다
#아래와 같이 가난하게 만들 수 있다.
def positive(x):
    return x > 0
print(list(filter(positive, [1, -2, 3, 4, -5, 8])))

#hex
#hex(x)는 정수 값을 입력받아 16진수로 변환하여 반환하는 함수이다
print(hex(323))

#id
#id(object)는 객체를 입력받아 객체 고유 주소 값을 반환하는 함수이다
a =3
print(id(a))
b=a
print(id(b))

#input
#input([prompt])sms 사용자 입력을 받는 함수이다. 매개변수로 문자열을 주면
#그 문자열은 prompt가 된다
# a = input()
# b = input("Enter : ",)

#int
#int(x)는 문자열 형태의 숫자, 소수점이 있는 숫자등을 정수형태로 반환
#정수를 입력받으면 그대로 반환한다

print(int("3"))
print(int(3.4))

#2진수로 표현된 11의 10진수의 값은 다음과 같이 구한다
print(int("11", 2))

#16진수로 표현된 1A의 10진수의 값은 다음과 같이 구한다
print(int("1A",16))

#isinstance
#isinstance(object, class)는 첫번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다
#입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True 거짓이면 False를 반환
class Person :
    pass
a = Person()
print(isinstance(a, Person))
b =3
print(isinstance(b, Person))

#len
#len(s)은 입력값 s의 길이(요소 전체 개수)를 반환하는 함수 이다
print(len("Python"))
print(len([1,2,3,4,5,6,7,8,9,10]))
print(len((1, "A")))

#list(s)
#list(s)는 반복 가능한 자료형 s를 입력받아 list 만들어 반환하는 함수이다
print(list("Python"))
print(list((1,2,3)))
a = [1, 2, 3]
b = list(a)
print(b)

#map(f, iterable)은 함수f 와 반복 가능한 자료형 iterable 자료형을 입력을 받는다
#map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과룰 묶어서 반환하는 함수이다

def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number**2)
    return result

result = two_times([1,2,3,4,5])
print(result)

#위의 예제를 map함수를 사용하여 아래와 같이 바꿀 수 있다
def two_time(x):
    return x**2
a = list(map(two_time, [1,2,3,4]))
print(a)

#max
#max(iterable)는 인수로 반복 가능한 자료형을 입력받아 그 최대값을 반환하는 함수 이다
a = max([1, 8, 2, 4, 20, 100])
print(a)
b = max("python")
print(b)

#min
#min(iterable) 함수는  max 함수와 반대로 , 인수로 반복 가능한 자료형을 입력받아
# 최소값을 반환하는 함수이다
c = min([0.5, -1, 2, 4, 10])
print(c)
d = min("String")
print(d)

#oct
#oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수이다.
print(oct(34))
print(oct(112))

#open
#open(filename, [mode])은 "파일 이름"과 "읽기 방법"을 입력받아 파일 객체를
#반환하는 함수이다. 읽기 방법(mode)를 생략하면 기본값인 읽기 전용모드(r)로 파일
#객체를 만들어 돌려준다
"""
    mode  |   설명 
    w     |   쓰기 모드로 파일 열기 
    r     |   읽기 모드로 파일 열기
    a     |   추가 모드로 파일 열기
    b     |   바이너리 모드로 파일 열기 
"""

#ord
#ord(c)는 문자의 ASCII 코드 값을 반환하는 함수이다
#ord 함수는 chr 함수와 반대이다
print(ord("a"))
print(ord("0"))

#pow
#pow(x, y)는 x의 y제곱한 결과값을 반환하는 함수이다
a= pow(2, 4)
print(a)

#range
#range([start,] [,step])는 for문과 함께 자주 사용되는 함수이다
#이 함수는 입력 받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 준다
#인수가 1개일 경우 : 시작 숫자를 지정하지 않으면 range 함수는 0부터 시작한다
a= list(range(5))
print(a)

#인수가 2개일 경우 : 시작 숫자와 끝 숫자를 의미, 단 끝 숫자는 해당 범위에 포함되지 않는다

b =list(range(1,10))
print(max(b))

#인수가 3개일 경우 : 세번째 인수는 숫자 사이의 거리를 의미한다
c = list(range(1, 10, 2))
print(c)

#round
#round(number[,ndigits]) 함수는 숫자를 입력받아 반올림해주는 함수이다
#[, ndigits]는 있을 수도 있고 없을 수도 있다는 의미이다.
print(round(4.564))
print(round(3.4545, 2))

#sorted
#sotred(iterable)함수는 입력값을 정렬한 후 그 결과를 list로 반환
a= sorted([3,1,2])
print(a)
b = sorted(["e", "a", "b", "F","c"])
print(b)

#str
#str(object)은 문자열 형태로 객체를 반환하는 함수
print(str(3))
print(str("hi".upper()))
print(str("PYTHON".lower()))

#tuple
#tuple(iterable)은 반복 가능한 자료형을 입력받아 tuple형태로 반환하는 함수
#만약 tuple이 입력으로 들어오면 그대로 반환
a= tuple("abc")
print(a)

#type
#type(object)는 입력값의 자료형을 알려주는 함수이다
print(type("abe"))
print(type([ ]))

#zip
#zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수이다
a= list(zip([1,2,3] ,[4,5,6]))
print(a)
b = list(zip([1,2,3], [4,5,6], [7,8,9]))
print(b)
c= list(zip("abc", "def"))
print(c)