#Python
# Python Data Type
# Dictionary 1
"""
사람은 누구든지 "이름" = "홍길동" , "주민등록번호" = "xxxxxx-yyyyyyy"등으로 구분가능
Python 도 대응 관꼐를 나타낼 수 있는 Data Type 가 있다. 요즘 사용하는 대부분의 언어도
이러한 대응 관계를 나타내는 자료형을 가지고 있다. 이를 연관배열(Associative Array) , Hash 라고 한다

Python에서는 이러한 자료형을 dictionary라고 한다.
Key와 value를 한 쌍으로 갖는 Data type 이다

dictionary는 list , tuple 처럼 순차적으로 해당 요소값을 구하지 않고
key를 통해 value값을 구하는 것이다 .

"""
# dictionary 의 형태
dic = {"name":"Python", "Phone":"010-0000-0000", "addresss":"900710"}
print(dic)
a = {1: "hi"}
print(a)
a= {"a":[1,2,3]}
print(a)

#dictionary 요소 추가
a = {"a":1 }
a["b"] = 2
print(a)
a["c"] = "dictionary"
print(a)
a["d"] = [1, 2, 3,]
print(a)

#dictionary 요소 제거
del a["a"]
print(a)

#dictionary Key를 사용해서 value  얻기
grade = {"name":"홍길동", "age":30}
b=grade["name"]
print(b)
print(grade["name"])
print(grade["age"])

"""
list , tuple, string 에서는 요소의 값을 얻기 위해서 Indexing, Slicing 중 하나를 사용했다. 
하지만 dictionary에서는 Key를 사용해서 Value를 구하는 방법이다. 
어떤 Key의 Value를 얻기 위해서는 dictionary변수 이름[key]를 사용한다 

"""
a = {1: "a", 2: "b"}
print(a[1])
"""
dictionary를 생성할 때 주의사항 
dictionary에서 key는 고유한 값이므로 중복되는 key값을 설정해 놓으면 하나를 제외한 나머지 것들이 
모두 무시된다는 점을 주의해야 한다. 
a = {1:"A", 1:"B"}
print(a)
위와 같은 사항에서 같은 Key가 2개 존재할 경우에는 1:"A"는 무시된다 

dictionary 에서 key에는 list를 사용할 수 없다. 하지만 tuple는 사용이 가능하다 
a = {[1,2],"b"}
print(a)
TypeError: unhashable type: 'list'

"""
#dictionary 함수
#Key list 만들기
b=[]
a ={"name":"Python", "address":"Seoul", "phone":"010-1234-4321"}
b= a.keys()
print(b)
print(a.keys())
"""
x.keys()는 dictionary x의 key만을 모아서 dict_keys 객체를 돌려준다
dict_keys 객체는 다음과 같이 사용할 수 있다. list를 사용하는 것과 크게 차이는 없지만 
list 고유의 append, insert, pop, sort 함수는 수행할 수 없다 
for k in a.keys():
    print(k)
"""
#dict_keys 객체를 리스트로 변환하는 방법
b=list(a.keys())
print(b)
print(list(a.keys()))

#value 를 list 만들기
print(a.values())

"""
key를 얻는 것과  마찬가지로 Value만 얻고 싶다면 values함수를 사용하면 된다 
values 함수를 호출하면 dict_values 객체를 돌려준다 
"""