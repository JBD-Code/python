#Python
# Python 함수
"""
Python 함수의 구조
def 함수명(매개변수) :
    <수행할 문장>
    <수행할 문장
def는 함수를 만들때 사용하는 예약어, 함수의 이름의 개발자가 임의로 생성
함수 이름 뒤 괄호 안의 매개변수는 이 함수의 입력으로 전달되는 값을 받는 변수
"""
def add(a, b):
    return a * b
print(add(3,4))

a= 3
b= 5
c = add(a, b)
print(c)
"""

Python에서 parameter 와 arguments 는 혼용해서 사용되는 헷갈리는 
용어 이므로 잘 기억해야 한다. 
parameter 은 함수에 입력으로 전달된 값을 받는 변수 

def add(a, b) # a , b 는 매개변수  
    return a + b 
print(add(3, 4))  # 3 ,4는 인수 
arguments 는 함수를 호출할 때 전달하는 입력 값 
"""
# 일반적인 함수
def add(a, b):
    result = a*b
    return result

a= add(3, 4)
print(a)

#입력 값이 없는 함수
def say():
    return "Hello"

a= say()
print(a)

#결과값이 없는 함수
def add(a,b):
    print("%d, %d의 함은 %d입니다" %(a, b, a+b))
add(4,7)

#입력값과 결과값이 모두 없는 함수
def say() :
    print("Hello")
say()

#매개변수를 지정하여 호출하기
def add(a, b):
    return a+b

result = add(a=3, b=7)
print(result)
#매개변수를 지정하면 순서에 상관없이 사용할 수 있다

result = add(b= 4, a=12)
print(result)

#입력값이 몇 개가 될 지 모를 때 경우
def add_many(*args):
    result=0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3,4,5,6,7,8)
print(result)

def add_mul(choice, *args):
    if choice =="add":
        result = 0
        for i in args:
            result +=i
    elif choice =="mul":
        result = 1
        for i in args :
            result *= i
    return result

result = add_mul("add", 1,2,3,4,5,6,7,8)
print(result)
result = add_mul("mul", 1, 2,3,4,5,6,7,8)
print(result)

"""
keyword와 parameter 
keyword parameter을 사용할 때는 매개변수 앞에 별 두개 (**)를 붙인다 

def print_kwargs(**kwargs):
print(kwargs)
아래의 결과 처럼 입력값이 모두 dictionary type로 만들어져서 출력된 다는 것을
알수 있다. key=value
"""
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name="Python", version=3.83)

def add_and_mul(a, b):
    return a+b, a*b

result = add_and_mul(4,5)
print(result)
# 함수의 결과값은 2개가 아니라 언제나 1개로 반환
# 따라서 결과값은 tuple(a+b, a*b)로 돌려준다

result, result1 = add_and_mul(3, 4)
print(result, result1)

def say_name(name):
    if name=="Python":
        return
    print("Hello %s" %name)

say_name("JAVA")
say_name("Python")

# 매개변수 초기값 미리 설정하기
def say_myself(name, version, result=True):
    print("My name is %s 입니다" %name)
    print("%s's version is %s" %(name, version))
    if result :
        print("True")
    else :
        print("False")

say_myself("Python", "3.8")

#함수 안에서 선언한 변수의 효력 범위

a =1
def vartest(a):
    a+=1
vartest(a)
print(a)
"""
def vartest(a):
    a=a+1
vartest(3)
print(a)

"""
#함수 안에서 함수 밖의 변수를 변경하는 방법
# return 사용하기
a = 1
def vartest(a):
    a=a+1
    return a

a= vartest(a)
print(a)

#global 명령어 사용하기
b= 1
def vartest():
    global b
    b =b+ 1

vartest()
print("b=", b)
"""
global 명령어를 사용하면 vartest 함수 안의 global b 문장은 
함수 안에서 함수 밖의 b 변수를 직접사용하겠다는 것이다. 
"""

#lambda
"""
함수를 생성할 때 사용하는 예약어로 def 와 동일한 역할을 한다 
보통 함수를 한줄로 간결하게 만들거나, def를 사용할 정도로 복잡하지 않거나 
def를 사용할 수 없는 곳에 주로 사용한다 
"""
add = lambda a, b: a+b
result= add(12,4)
print("result = %d" %result)
#lambda 예약어로 만든 함수는 resutn 명령어가 없어도 결과값을 반환한다