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
a = input()
b = input("Enter : " ,)