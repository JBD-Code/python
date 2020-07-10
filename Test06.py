#Python
# Python Data Type
# 리스트(List) 1
list = [1 ,2, 3, 4, 5]
print(list)
a= []
b= [1,2,3,4]
c= ["Life" , "is", "too", "long"]
d= [1, 2, "Life" , "is"]
e= [1, 2, ["Life", "is"]]
print(e)

# list 안에는 어떠한 자료형도 포함시킬 수 있다

#list Indexing
a= [1, 2,3]
print(a[0])
print(a[0]+ a[2])
b= a[0] +a[2]
print(b)
print(a[-1])

f = [1, 2, 3, ["a", "b", "c"]]
print(f[0])
print("list f의 f[-1] =" , f[-1])
#["a","b","c']의 "a"값 Indexing
print("f[-1][0]=", f[-1][0])
print(f[-1][1])

#3중 리스트에서 indexing
a = [1, 2, ["A", "B", ["Life","is","Long"]]]
print(a[-1][-1][0])
print(a[2][2][0])

#list Slicing
a = [1, 2,3,4,5,6,]
print(a[0:2])

#중첩된 리스트의 Slicing
a = [1,2,3,4, ["a","b","c",["life", "is", "good"]],4 ,5]
print(a[0:4])
print(a[4][:2])

#list 더하기
a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = a + b
print (c)
print(a+b)

#list 반복하기
print(a*4)

#list 길이 구하기

print("list a의 길이는 ",len(a),"입니다")

"""
초보자가 하기  쉬운 list 연산 오류 "Type Error"
a = [1,2,3]
print(a[2]+ "Hi")
"""

print(str(a[2])+" hi")
#str 함수는 정수나 실수를 문자열의 형태로 바꾸어주는 Python의 내장 함수 이다

#list 수정과 삭제
a= [1,2,3]
a[2] = 4
print(a)

#del 함수 사용해서 리스트의 요소 삭제하기
del a[1]
print(a)
a = [1,2,3,4,5,6]
del a[3:]
print(a)

#append 함수 사용해서 리스트의 요소 추가하기
a.append(4)
print(a)
a.append([4,2,1])
print(a)

#sort 함수를 사용해서 리스트를 정렬하기
a = [1, 4, 2, 34, 54, 12]
#print(a.sort()) 출력 X
a.sort()
# 숫자 정렬 가능
print(a)
b= ["c", "v" ,"a", "d","x"]
b.sort()
# 알파벳 정렬 가능
print(b)

#reverse 함수를 사용해서 리스트 뒤집기
#리스트 요소들을 순서대로 정렬한 후 다시 역순으로 정렬하는 것이 아니라 현재의 리스트를 뒤집는다
b.reverse()
print(b)

#index 함수를 사용해서 위치반환
c = [1, 2, 3, 4, 5]
d= c.index(3)
print(d)
print(c.index(4))

#insert 함수를 사용해소 list 요소 삽입
c.insert(4, "c")
print(c)
c.insert(6, 0)
print(c)

#remove 함수를 사용해서 list 요소 제거
#remove(x) 함수는 list에서 첫 번째로 나오는 x를 제거하는 함수
a =["a","b","c","b","a"]
a.remove("b")
print(a)

#pop 함수를 사용해서 요소 집어내기
#pop 함수는 list 의 마지막 요소를 돌려주고 그 요소는 삭제한다
a = [1,2,3,4]
print(a.pop())
print(a)

#pop(x)는 list 의 x번째 요소를 돌려주고 그 요소는 삭제한다
a = ["a", "b", "c", "d", "e"]
print(a.pop(1))
print(a)

#count 함수를 사용해서 list에 포함된 x의 개수 세기
a = [1, 2, 3, 4]
print(a.count(1))

#extend 함수를 사용하여 list 확장하기
#extend(x)에서 x에는 list 만 올 수 있으며 원래의 list 리스트에 x 를 더하게 된다
a = [1,2,3,4]
a.extend([6,7])
#a.extend([x,y])는  a+=[x,y]와 동일하다
a+=[4,5]
print(a)