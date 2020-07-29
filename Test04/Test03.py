#Python
# Python module
"""
module란 함수반 변수 또는 클래스를 모아 놓은 파일이다.
다른 Python 프로그램에서 불러와서 사용할 수 있게 만든 Python File
import 모듈 이름
from 모듈이름 import 모듈함수


def add(a, b):
    return a+b
def sub(a, b):
    return a-b
print(add(1,4))
print(sub(12,2))

def add(a, b):
    return a+b
def sub(a, b):
    return a-b

if __name__ =="__main__":
    print(add(1, 43))
    print(sub(20, 1))
"""
PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r**2)

def add(a, b):
    return a+b