class Value:
    def __init__(self):
        self.valid = False
    def __bool__(self):
        return self.valid
    def setValidity(self, validity):
        self.valid = validity

var = Value()
print(bool(var))  # False
var.setValidity(True)
print(bool(var))  # True

class Stack:
    def __init__(self):
        self.stack = list()
    def __len__(self):
        return len(self.stack)
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop()

stack = Stack()
print(len(stack))   # 0
print(bool(stack))  # False

stack.push(100)     # 100 �Է�
print(len(stack))   # 1
print(bool(stack))  # True

stack.pop()         # 100 ���
print(len(stack))   # 0
print(bool(stack))  # False








a = 10
b = 20

# 10 , 20 ���
# 1. ���� �������� �ֱ�
print(a, "," , b)

# 2. c ��Ÿ�� 
print("%d , %d" % (a,b), "%d , %d" % (a,b))

# 3. format �Լ�
print("{} , {}".format(a, b))

# 4. f-string
print(f"{a} , {b}")


a = input("input")
print(f"{a}")

b = int(input("input"))
print(f"{b}")

c = float(input("input"))
print(f"{c}")

import sys
a = sys.stdin.readline()
print(f"{a}")

b = int(sys.stdin.readline())
print(f"{b}")

c = float(sys.stdin.readline()) 
print(f"{c}")


if True:
    print("Hello world")  #4ĭ �鿩����
for n in range(0, 10):
  print(n) #2ĭ �鿩����
