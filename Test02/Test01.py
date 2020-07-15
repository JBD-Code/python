#Python
# Python 제어문
# if 문
money = True
if money :
    print("Taxi")
else :
    print("Walk")
"""
if문의 형태
if 조건문 :
    수행할 문장1
    수행할 문장2
else :
    수행할 문장 A
    수행할 문장 B    
"""

"""
주의사항 들여쓰기 (indentation)
if문을 만들 때는 if 조건문 아래 문장 부터 if 문에 속하는
모든 문장에 들여쓰기 (indentation)을 해주어야한다  
아래 처럼 작성하면 오류가 발생한다. 

if 조건문 :
    수행할 문장1
수행할 문장2   

수행할 문장1, 수행할 문장2 와 수행할 문장 3의 들여쓰기가 다르기 때문이다 
if 조건문 :
    수행할 문장1
    수행할 문장2   
        수행할 문장3
        
IndentationError: expected an indented block
"""

"""
주의사항 (:)
if 조건문 뒤에는 반드시 :이 붙는다  
"""
"""
비교연산자 
x < y   | x가 y보다 작다 
x > y   | x가 y보다 크다  
x == y  | x와 Y가 같다
x != y  | x와 Y가 같지 않다 
x >= y  | X가 y보다 크거나 같다 
x <= y  | X가 y보다 작거나 같다
"""
x, y = 3, 2
print("x > y : " , x>y)
print("x < y : " , x<y)
print("x == y : " , x==y)
print("x != y : " , x!=y)

money = 2000
if money >= 3000:
    print("Taxi")
else :
    print("walk")
"""
조건을 판단하기 위해 사용하는 다른 연산자로는 
and, or, not 가 있다 
    연산자          설명 
    x or y     |    x와 y 둘 중에 하나만 참이어도 참이다 
    x and y    |    x와 y 모두 참이어야 참이다 
     not x     |    x가 거짓이면 참이다     
"""

#돈이 3000원 이상 있거나 카드가 있다면 Taxi를 타고 그렇지 않다면 walk

money = 2000
card = True
if money >=3000 or card:
    print("Taxi")
else :
    print("walk")
""" 
x in s, x not in s 
    in       |     not in 
 x in list   |    x not in list 
 x in tuple  |    x not in tuple
 x in String |    x not in String         
"""

result =1 in [1, 2, 3]
print ("result :", result)
result = 1 not in [1, 2,3,]
print("result :", result)

print("a" in ("a", "b", "c"))
print("j " not in "python")

pocket = ["paper", "cellphone", "money"]
if "money " in pocket :
    print("Taxi")
else :
    print("walk")

# 조건문에서 아무 것도 하지 않게 설정하고 싶을 경우
if "money" in pocket:
    pass
else :
    print("Card")

""" 
주머니에 돈이 있으면 버스를 타고, 
주머니에 돈은 없지만 카드가 있으면 택시를 타고, 
돈도 없고 카드도 없으면 걸어 가라.
"""
pocket = ["paper", "handphone"]
card = True
if "money " in pocket:
    print("Bus")
else :
    if card :
        print("Taxi")
    else :
        print("walk")

if "money" in pocket:
    print ("Bus")
elif card:
    print("Taxi")
else:
    print("walk")

# if 문 한 줄로 작성하기
if "money" in pocket:
    pass
else :
    print("Card")

if "money" in pocket :pass
else: print("Card")

score = 70
if score >= 60:
   message = "success!"
   print(message)
else :
    message = "failure!"
    print(message)