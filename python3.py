# Data types

x = 10 # int
y = 20.5 # float
z = "hello" # str
a = True # bool
b = [1, 2, 3] # list
c = (1, 2, 3) # tuple
d = {1, 2, 3} # set
e = {'a': 1, 'b': 2, 'c': 3} # dict

# Operators

# Addition
print(x + y)

# Subtraction
print(x - y)

# Multiplication
print(x * y)

# Division
print(x / y)

# Floor division
print(x // y)

# Modulo
print(x % y)

# Exponentiation
print(x ** y)

# Equals
print(x == y)

# Not equals
print(x != y)

# Less than
print(x < y)

# Less than or equal to
print(x <= y)

# Greater than
print(x > y)

# Greater than or equal to
print(x >= y)

# Logical and
print(a and b)

# Logical or
print(a or b)

# Logical not
print(not a)

# Control flow

if x < y:
  print("x is less than y")
elif x > y:
  print("x is greater than y")
else:
  print("x is equal to y")

for i in b:
  print(i)

while x < y:
  print(x)
  x += 1

# Break
for i in b:
  if i == 2:
    break
  print(i)

# Continue
for i in b:
  if i == 2:
    continue
  print(i)

# Pass
for i in b:
  if i == 2:
    pass
  print(i)

# Functions

def add(x, y):
  return x + y

print(add(x, y))

add_lambda = lambda x, y: x + y
print(add_lambda(x, y))

def generator():
  for i in b:
    yield i

for i in generator():
  print(i)

# Classes

class MyClass:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f"MyClass(x={self.x}, y={self.y})"

obj = MyClass(x, y)
print(obj)

# Miscellaneous

# None
x = None
print(x)

# Length
print(len(b))

# Range
print(list(range(5)))

# Print
print("Hello, world!")

# Input
x = input("Enter a value: ")
print(x)

# Assert
assert x == y
