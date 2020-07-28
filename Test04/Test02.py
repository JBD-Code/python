#Python
# Python class Constructor
"""
class Calculator:
    def setdata(self, first, second):
        self.first=first
        self.second=second
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

a = Calculator()
a.setdata(4,5)
print(a.add())
print(a.sub())

a = Calculator()
print(a.add())

Traceback (most recent call last): Error 출력 
Calculator 클래스의 instance a 에 setdata 메소드를 수행하지 않고 바로 add 메소드를 수행하면 
AttributeError: 'Calculator' object has no attribute 'first' Error 이 발생한다 
setdata 메소드를 수행해야 할 object a의 객체 변수 first, second가 생성 되기 때문이다. 

이렇게 객체의 초기값을 설정해야 할 필요가 있을 때는 setdata와 같은 메소드를 호출하여 
초기값을 설정하는 것보다는 생성자를 구현하는 것이 안전하다. 
생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메소드를 의미한다
"""
from Test04.Test01 import Calculator


class Calculator:
    def __init__(self, first, second):
        self.first=first
        self.second=second
    def setdata(self, first, second):
        self.first=first
        self.second=second
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

a = Calculator(6,10)
print(a.first)
print(a.add())

# class의 inheritance
"""

class MoreCalculator(Calculator):
    pass
class를 상속하기 위해서는 다음과 같이 
클래스의 이름 뒤 괄호 안에 상속할 클래스의 이름을 넣어주면 된다 

class 클래스 이름 (상속할 클래스 이름) 

MoreCalculator 클래스는 Calculator 클래스를 상속했으므로 
Calculator 클래스의 모든 기능을 사용할 수 있어야 한다. 

a = MoreCalculator(6,6)
print(a.add())
print(a.mul())

보통 상속은 기존 클래스를 변경하지 않고 기능을 추가 하거나 기존 기능을 변경하려고 할 때 사용 
클래스에 기능을 추가하고 싶으면 기존 클래스를 수정하면 되는데 굳이 상속으로 받아서 처리해야 하는가
하는 의문이 들 수 도 있지만, 기존의 클래스가 라이브러리 형태로 제공 혹은 수정이 허용되지 않는 
상황이라면 상속을 사용하여야 한다 



class MoreCalculator(Calculator):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreCalculator(5, 4)
print(a.pow())

# class Method overriding

b = Calculator(4, 0)
print(b.div())


ZeroDivisionError: division by zero 
Calculator 클래스의 객체 b에 4, 0의 값으로 초기화 하고 div 메소드를 호출하면 
위와 같은 ZeroDivisionError: division by zero 오류가 발생한다. 
하지만 0으로 나눌 때 오류가 아닌 0을 반환하려고 만들고 싶다면 어떻게 해야 하는가 
"""

class SafeCalculator(Calculator):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/self.second

a = SafeCalculator(4,0)
print(a.div())

# 클래스 변수
"""
객체 변수는 다른 객체들에 영향을 받지 않지 않고 그 값을 유지한다
객체변수와는 성격이 라든 클래스 변수에 대해서 알아보자 
"""
class Family :
    lastname = "KIM"
"""
Family 클래스에 선언한 lastname 이 클래스 변수 이다 
클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언, 생성한다 

"""
print(Family.lastname)
a= Family()
b= Family()
print(a.lastname)
print(b.lastname)

Family.lastname="PARK"
print(a.lastname)
print(b.lastname)

"""
클래스 변수 값을 변경했더니 클래스로 만든 객체의 lastname값도 모두 변경된다는 것을 
확인할 수가 있다. 즉 클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징이 있다. 
"""
print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))
"""
id값이 모두 값으므로 Family,lastname, a.lastname, b.lastname은 모두 같인 메모리를 
기리키고 있다. 
"""


