#Python
# Python
# Variable
"""
 a= 1
 b = "Python"
 c = [1,2,3]
Python의 경우 변수를 생성할 때 저장된 값을 스스로 판단하여
자료형을 지정하기 때문에 변수명 앞에 DataType을 선언할 필요가 없다
변수이름 = 변수에 저장할 값
Python 에서 사용하는 변수는 개체를 가리키는 것이다
"""
a = [1,2,3,4]
print("a변수가 가리키는 메모리 주소 : ", id(a))
b = a
print("a변수가 가리키는 메모리 주소 : ",id(a))
print("b변수가 가리키는 메모리 주소 : ",id(b))

#a 와 b 가 가리키는 객체가 동일한가?
print ("a is b = ", a is b)

a[1] = 4
print(a)
print(b)

#b변수를 생성할 때 a 변수의 값을 가져오면서 a 와 다른 주소를 가리키도록 만드는 방법
# 첫번째 list 전체를 가리키는 [:]을 사용해서 복사한다
a= [1, 2, 3]

b =a[:]
a[1] =5
print(a)
print(b)
print("b가 가리키는 메모리 주소 : ", id(b))
print("a가 가리키는 메모리 주소 : ", id(a))

# 두번째 copy 모듈을 사용한다
from copy import copy
c = copy(a)
print(c)
print("a가 가리키는 메모리 주소 : ", id(a))
print("c가 가리키는 메모리 주소 : ", id(c))
print("a is c :" ,a is c)

#변수를 생성하는 여러가지 방법
a, b = ("Python", "life")
print( "a=",a ,"b=" , b)
c= d = "Python "
print(c, d)
c = 3
d = 4
print ("c =", c)
print ("d =", d)

c, d = d, c
print ("c =", c)
print ("d =", d)