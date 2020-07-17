#Python
# Python 제어문
# for 문
"""
for 문의 기본 구조
for 변수 in list(tuple, String) :
    수행할 문장 1
    수행할 문장 2
"""

test_list = ["one", "two", "three"]
for i in test_list :
    print (i)

a =[(1,2), (3,4), (5,6)]
for(first, last) in a :
    print (first + last)
number = 0
marks = [90, 25, 65, 45, 80]
for a in marks :
    number = number +1
    if a > 60 :
        print("%d번 학생의 점수는 %d 이므로 합격" %(number, a))
    else :
        print("%d번 학생의 점수는 %d 이므로 불합격" %(number, a))

#for 문과 continue

marks= [90, 25, 67, 45 , 80]
number = 0
for mark in marks:
    number = number +1
    if mark < 60:
        continue
        print("%d 번 학생 축하합니다 %d이므로 합격입니다 " %(number, mark))

#for 문과 자주 사용하는 range 함수

a = range (10)
print(a)

#range(0, 10)은 0부터 10 미만의 숫자를 포함하는 range 객체를 만들어 준다
#시작 숫자와 끝 숫자를 지정하려면 range(시작 숫자, 끝 숫자)형태를 사용하는 데
#이 때 끝 숫자는 포함되지 않는다.

add = 0
for i in range(1, 11):
    add+=i
    print(add)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다 합격입니다" %(number+1))
"""
len 함수는 list 안의 요소의 개수를 돌려준다 len(marks) = 5 
range(len(marks)) 는 range(5) 가 된다 
"""

#for range 를 이용한 구구단
for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end= " ")
    print("")

#  list comprehension 사용하기
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)


a = [3, 4, 5, 6]
result = [num * 3 for num in a]
print(result)

a = [1, 2, 3, 4, 5, 6]
result = [num*3 for num in a if num % 2 ==0]
print(result)