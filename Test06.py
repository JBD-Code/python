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
a = [1, 2,3]
print(a[2]+ "Hi")
"""

print(str(a[2])+" hi")
#str 함수는 정수나 실수를 문자열의 형태로 바꾸어주는 Python의 내장 함수 이다

