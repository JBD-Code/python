#Python
# Python Data Type
# 튜플(Tuple) 1
"""
tuple 은 몇 가지 점을 제외하고 list 와 비슷하며 다른 점은 다음과 같다
- list는 [ ] 로 둘러 싸지만 tuple 는 ()로 둘러싼다
- list는 그 값이 생성 , 수정, 삭제가 가능하다
- tuple은 그 값을 수정할 수 없다
"""
# tuple의 형태
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 =  ("a", "b", "c" ,(1, 2,3))
print (t1)

"""
list 와 모습의 거의 비슷하지만 tuple 와 다른 2가지 차이점을 
찾아볼 수 있다. t2 =(1,)처럼 단지 1개의 요소를 가질 때는 요소
뒤에 반드시 , 붙여야 한다는 것과, t4=1,2,3  처럼 () 를 생략해도 무방하다 

tuple 의 요소 값을 제거 할 경우 

t1= (1,2,3,4)
del t1[0]
print(t1)
TypeError: 'tuple' object doesn't support item deletion

tuple 의 요소 값을 변경 할 경우 

t1= (1,2,3,4)
t1[0] = "x"
print(t1)
TypeError: 'tuple' object does not support item assignmen
"""

#tuple 다루기

#tuple Indexing
t1 = (1, 2, "A", "B")
t1[0]
print(t1[0])

#tuple slicing

print(t1[1:])

#tuple 더하기
t2 = ("C", "D")
t3 = ()
t3=t1 +t2
print("t3 = ",t3)

#tuple 곱하기
print(t3*3)

print(len(t3))
