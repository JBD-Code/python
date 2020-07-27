#Python
# Python 파일 읽고 쓰기
# 파일 생성하기
# 파일에 새로운 내용을 추가하기
"""
쓰기 모드 ("w")로 파일을 열때 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라지게 된다
하지만 원래 있는 값을 유지하면서 새로운 값을 추가해야 할 경우에는 파일을 추가모드("a")로 열면 된다
"""
"""
f = open("new file.txt", "w")
f.close()

파일을 생성하기 위해서는 Python 내장 함수 open을 사용한다. 
open 함수는 아래와 같이 "파일 이름"과 "파일 열기 모드" 를 입력값으로 받고, 

    파일 객체 = open("파일이름", "파일 열기모드")

결과값으로 파일 객체를 돌려준다 
파일 열기 모드 |  설명 
     r        | 읽기 모드 - 파일을 읽기만 할 때 사용  
     w        | 쓰기 모드 - 파일에 내용을 쓸 때 사용  
     a        | 추가 모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용 

파일을 쓰기모드로 열면, 해당 파일이 이미 존재할 경우 원래 있던 내용이 전부 사라진다 
해당 파일이 존재하지 않음녀 새로운 파일이 생성된다. 
위의 예제에서는 디렉터리에 파일이 없는 상태에서 "new file.txt"를 쓰기모드인 "w"로 
열었기 때문에 "new file.txt"라는 이름의 새로운 디렉터리에 생성되는 것이다       

#new file.txt 파일은 D:/file_example디렉터리에 생성하고 싶다면 아래와 같이 작성한다

f = open("D:/file_example/new file.txt", "w")
f.close()

#프로그램의 출력값을 파일에 직접 쓰기

f =open("D:/file_example/new file1.txt", "w")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()
#프로그램의 외부에 저장된 파일을 읽기
# 1 readline() 함수 이용하기
f =open("D:/file_example/new file1.txt", "r")
line = f.readline()
print(line)
f.close()

f =open("D:/file_example/new file1.txt","r")
while True:
    line = f.readline()
    if not line:break
    print(line)
f.close()


# 2 readlines 함수 사용하기
f = open("D:/file_example/new file1.txt","r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()
# readlines 함수는 파일의 모든 줄을 읽어서 각가의 줄을 요소로 갖는 list로 반환
# 따라서 위의 예제는 lines 리스트는 ["1 번째 줄입니다", "2번째 줄입니다"..."10번째 줄입니다] 가 된다

# 3 read 함수 사용하기
f = open("D:/file_example/new file1.txt","r")
data= f.read()
print(data)
f.close()
# f.read()는 파일의 내용 전체를 문자열로 돌려준다 따라서 data는 파일 전체의 내용이다



f= open("D:/file_example/new file1.txt","a")
for i in range(11, 20):
    data = "%d번째 줄입니다\n" %i
    f.write(data)
f.close()
"""
#with 문과 함께 사용하기
"""
 파일을 열면 위와 같이 항상 close 해주는 것이 좋다. 
 하지만 이렇게 파일을 열고 닫는 것을 자동으로 처리할 수 있도록 도와주는 것이  with문이댜 
"""

with open("D:/file_example/new file2.txt", "w") as f:
    f.write("Life is toos short, you need Python")
