#Python
# Python class
"""
class Calculater:
    def __init__(self):
        self.result=0
    def __add__(self, num):
        self.result +=num
        return self.result

cal1 = Calculater()
cal2 = Calculater()

print(cal1.__add__(3))
print(cal1.__add__(4))
print(cal2.__add__(5))
print(cal2.__add__(6))


Calculator class 를 이용해 만든 계산기 cal1, cal2를 Pyhton에서는 객체라고 부르며
각각의 역할을 수행한다. 그리고 다른 결과값과 상관없이 독립적인 값을 유지한다.
class를 이용하면 계산기 대수가 늘어나더라도 객체를 생성하기만 하면 되기 때문에
함수를 사용하는 것과 달리 매우 간단해진다.
"""

class Calculator:
    def __init__(self):
        self.result = 0
    def __add__(self, num1):
        self.result+=num1
        return self.result
    def __sub__(self, num2):
        self.result-=num2
        return self.result
    def __mul__(self, num3):
        self.result*=num3
        return self.result

cal = Calculator()
print(cal.__add__(20))
print(cal.__mul__(5))
print(cal.__sub__(5))

"""
Python에서 class 와 object  
JAVA에서 class 와 object와 동일하다. 
과자를 만드는 과자틀과 그것을 사용해 만드는 과자 
        
        과자 틀 -  class 
        과자    - object 
class오 만든 object에는 중요한 특징이 있다. 객체마다 고유한 특징을 가진다. 
동일한 클래스로 만든 객체들은 서로 영향을 주지 않는다. 
"""
class Cookie:
    pass
a= Cookie()
b= Cookie()
"""
위의 class는 아무 기능도 갖고 있지 않는 껍질뿐인 클래스이다. 하지만 이렇게 껍질뿐인 
class 도 object를 생성하는 기능이 있다. 

[object와 instance의 차이] 
class로 만든 object를 instance라고 한다.  그렇다면 object와 instance의 차이는 무엇인가 
a = Cookie() 이렇게 만든 a 는 object이다. a object는 Cookie의 instance이다. 
즉 instance라는 것은 특정 object(a)가 어떤 class(Cookie)의 object인지를 관계 위주로 설명할 때 
사용한다. "a는 instance" 라는 표현 보다는 "a는 object"라는 표현이 어울리며 
"a"는 Cookie의 object"라는 말 보다 "a는 Cookie의 instance " 라는 표현이 맞다. 

#사칙연산 class 만들기
class FourCal:
   pass
a = FourCal()
print(type(a))

#pass 는 아무것도 수행하지 않는 문법으로 임시로 코드를 작성할 때 주로 사용한다
#위와 같이 a = Fourcla() 로 a 객체를 생성 그 다음 type(a)로 a 객체가 어떤 타입인지 확인

class Fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
a = Fourcal()
a.setdata(4,2)
"""
"""
setdata() 메소드에는 self, first, second 총 3개의 매개변수가 필요한데 실제로는 
a.setdata(4,2)처럼 2 개의 값만 전달했다. 그 이유는 a.setdata(4,2)처럼 호출을 하면 
setdata메소드의 첫번째 매개변수 self에는 setdata를 호출한 객체 a가 자동으로 전달되기
떼문이다. 
Python Method의 첫번째 매개변수 이름은 관례적으로 self 를 사용한다 . 
[메소드의 다른 호출방법] 
a = Fourcal 
Fourcal.setdata(a, 4, 2) 
위와 같이 클래스 이름.메소드 형태로 호출을 할 경우에는 객체 a 를 첫번째 매개변수 self에 꼭 
전달해 주어야 한다 하지만 아래의 경우처럼 객체.메소드 형태로 호출을 한자면 self를 반드시 생략한다 

a = Fourcal() 
a.setdata(4,2)

print(a.first)
print(a.second)

b = Fourcal()
b.setdata(7,3)
print(b.first)
print(b.second)
print(id(a.first))
#id함수는 객체의 주소를 돌려받는 Python의 내장함수이다 .
print(id(b.first))
"""
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal()
b = FourCal()
a.setdata(4,2)
b.setdata(6,5)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

print(b.add())
print(b.sub())
print(b.mul())
print(b.div())