#Python
# Python Data Type
# bool
"""
bool data type 란 참(True), 거짓(False)를 나타내는  DataType이다
True , False는 Python 의 자료형으로 true, false 와 같이 사용하지 않고
항상 첫 문자를 대문자로 사용하여야 한다
"""
a = True
b = False
print(type(a)) #<class 'bool'>
print(type(b)) #<class 'bool'>
print("1==1 : " , 1==1)
print("2<1  : " , 2<1)

"""
자료형의 참과 거짓 

    값     |   True or False 
 "python"  |   True
     ""    |   False
  [1,2,3]  |   True
     []    |   False         
     ()    |   False
     {}    |   False
      1    |   True
      0    |   False
    None   |   False
 String, list, tuple, dictionary 등의 값이 비어 있으면 ("", [], (), {})
 False가 된다. 비어있지 않으면 True 가 된다 
 숫자의 경우 그 값이 0일 때 False 가 된다. 
 None의 경우 거짓을 의미한다        
"""
a= [1,2,3,4]
while a:
    print(a.pop())


if [] :
    print("True")
else:
    print("False")

if [1 ,2,  3]:
    print("True")
else:
    print("False")

# bool 연산
print("Python=", bool("Python"))
print("() =", bool())
print("[] =", bool([]))
print("0 =", bool(0))
print("1 =", bool(1))
print("[1,2,3] =", bool([1,2,3]))

