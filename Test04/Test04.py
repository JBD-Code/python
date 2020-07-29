#Python
# Python Exception 처리하기
"""
Python에서  예외가 발생하는 대표적인 유형
1 디렉터리 안에 없는 파일을 열고 시도했을 때 발생하는 오류
FileNotFoundError: [Errno 2] No such file or directory:

2 0으로 다른 숫자를 나누는 경우
ZeroDivisionError: division by zero

3 list에서 얻을 수 없는 값을 얻을 려고 하는 경우


"""
# 오류 처리 기법 1 try, except문
"""
try:    
    ...
except [발생오류[as 오류 메시지 변수]]:
    ...
    
1. try, except만 쓰는 방법 
try : 
    ...
except :
    ... 
이 경우는 오류 종류에 상관없이 오류가 발생하면 except 블록을 수행한다     

2. 발생 오류만 포함한 except문 
try:
    ...
except 발생오류 
    ...
이 경우는 오류가 방생했을 때 except문에 미리 정해놓은 오류 이름과 
일치할 때만 except 블록을 수행한다      

3. 발생오류와 오류 메시지 변수까지 포함한 except 문 
try:
    ...
except 발생오류 as 오류 메시지 변수 
    ...
"""

try :
    4 / 0
except ZeroDivisionError as e :
    print(e)

# 오류 처리 기법 2 try..finally 문

"""
try문에는 finally 절을 사용할 수 있다 finally절은 try문 수행 도중 
예외 발생 여부에 관계없이 항상 수행된다. 보통 finally 절은 사용한 자원을 
close 해야 할 때 많이 사용한다 
f = open("D:/file_example/new file1.txt", "w")
try :
    #수행할 문장 
finally:
    f.close()
 
"""

# 여러개의 오류 처리하기
"""
try:
    ...
except 발생오류1 : 
    ...
except 발생오류2 :
    ...
except 발생오류3 :
    ...
"""
try :
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다. ")

try :
    a = [1,3]
    print(a[4])
    4/0
except ZeroDivisionError as e :
    print(e)
except IndexError as e :
    print(e)

try :
    a = [1,4]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

# 오류 회피하기
try :
    f = open("Not File.txt", "r")
except FileNotFoundError :
    pass
"""
try 문 안에서 FileNotFoundError 가 발생한 경우에 pass 를 사용하여 
오류를 회피하도록 한다 
"""

# 오류 일부러 발생시키기
"""
오류를 일부러 발생시켜야 할 경우가 생긴다. 
Python은 raise 명령어를 사용해 오류를 강제로 발생 시킬 수 있다 
"""
class Bird:
    def fly(self):
        raise NotImplementedError
"""
위의 예제는 Bird 클래스를 상속받는 자식 클래스는 반드시 fly 라는
함수를 구현하도록 만들고 싶을 경우에 사용한다 
만약에 자식 클래스가 fly 함수를 구현하지 않은 상태로 fly 함수를 호출한다면 
그 결과는 어떻게 출력되는가 

class Eagle(Bird):
    pass
eagle = Eagle()
print(eagle.fly())
"""
class Eagle(Bird):
    def fly(self):
        print("very fast")
eagle = Eagle()
print(eagle.fly())

# 예외 만들기
class MyError(Exception):
    pass
def say_name(name):
    if name == "python":
        raise MyError()
    print(name)
try :
    say_name("java")
    say_name("python")
except MyError :
    print("허용되지 않는 이름입니다")