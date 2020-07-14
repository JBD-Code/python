#Python
# Python Data Type
# 집합 Set 1
"""
집합(set) 자료형은  Python 2.3부터 지원하기 시작
집합에 관련된 것을 쉽게 처리하기 위해 만든 Data Type
"""
#집합 자료형의 생성
s1 = set([1,2,3,])
print(s1)

s2 = set("Hello")
print(s2)

"""
s2 = set("Hello")을 보면 결과가 이상하다 
다음과 같은 집합 자료형의 특징을 알 수 있다 
- set은 중복을 허용하지 않는다 
- set는 순서가  존재하지 않는다 s2 = set("Hello")

tuple, list는 순서가 있기 때문에 indexing을 통해 자료형의 값을 얻을 수 있지만 
set 자료형은 순서가 없기(unordered)때문에 Indexing을 통해서 값을 얻을 수 없다 
set 자료형에 저장된 값을 얻기 위해서는 list, tuple로 형변환을  통해서 값을 얻을 수 있다. 
중복을 허용하지 않는 set의 특징 때문에 중복을 제거하기 위한 필터로 종종 사용된다  
"""
s3 = set([1,2,3,])
list1 = list(s3) # list 로 type 변환
print(list1[0])

tuple1 = tuple(s3) # tuple 로 type 변환
print(tuple1[1])


# set 자료형을 사용하여  교집합, 합집합, 차집합 구하기
# 교집합 구하기
s1 = set([1,2,3,"A","B"])
s2 = set(["A","B","C","D"])
print(s1&s2)
s3 = set([])
s3=s1.intersection(s2)
print("s3 = ", s3)

#합집합 구하기
print("s1|s2=",s1|s2)
s3= s1.union(s2)
print("s1.union(s2)=",s3)

#차집합 구하기
s3 = s1 -s2
print("s1-s2=",s3)
s3 = s2 - s1
print("s2-s1=", s3)
s3 = s1.difference(s2)
print("s1.difference(s2)=", s3)
s3 = s2.difference(s1)
print("s2.difference(s1)=", s3)

#집합 자료형 관련 함수
#요소 값 하나 추가하기(add)
s1 = set([1,2,3,])
s1.add(4)
print("s1.add(4)=",s1)

#요소 값 여러개 추가하기(update)
s1.update(["A","B","C"])
print("s1.update(['A','B','C'])=",s1)

#특정 요소 제거하기 (remove)
s1.remove(3)
print("s1.remove(3)=",s1)