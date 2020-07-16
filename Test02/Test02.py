#Python
# Python 제어문
# while 문
"""
while문의 기본 구조
while<조건문>
    <수행할 문장>
    <수행할 문장>
    <수행할 문장>
"""
from turtledemo.tree import tree

treeHit=0
while treeHit< 10:
    treeHit = treeHit+1
    print("나무를 %d 번 찍었습니다" %treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다")
prompt="""
    1. Add
    2. Del
    3. List
    4. Quit
    Enter number:"""
number = 0

while number != 4 :
    print(prompt)
    number = int(input())

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다 ")
    coffee = coffee -1
    if coffee ==0 :
        print("커피가 다 떨어졌습니다")
        break


coffee = 10
while True:
    money = int(input("돈을 넣어주세요"))
    if money ==300 :
        print("커피를 줍니다")
        coffee = coffee -1
    elif money > 300 :
        print("거스름돈을 %d를 주고 커피를 줍이다" %(money-300))
    else :
        print("돈을 다시 돌려주고 커피를 주지 않습니다")
        print("남은 커피의 양은 %d 개입니다" %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지랍니다")
        break


#while문의 제일 처음으로 돌아가기
a = 0
while a < 10 :
    a = a+1
    if a % 2 == 0 : continue
    print(a)

#무한 Loop
"""
while True :
    수행할 문장1 
    수행할 문장2   
"""
while True :
    print("Ctrl+F2를 눌러야 while문을 빠져나갈수 있습니다")
