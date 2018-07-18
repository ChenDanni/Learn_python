# 2018/07/17
# -----------------------------------
# IO
# -----------------------------------
# output
print("hello word")
# output in the same line
print("first ", end="")
print("second")
# input
name = input("input your name: ")
print("hello ", name)

# -----------------------------------
# VARIABLE
# -----------------------------------

# declare
a = 1
a = b = c = 1
a, b, c = 1, 2, 3

# swap
a, b = b, a

# get variable type
type(a)

# get varable id
id(a)

# -----------------------------------
# DATA TYPE
# -----------------------------------
# number
# int 2/8/10/16
n1 = 0b1010
n2 = 0o777
n3 = 999
n4 = 0xfff
# float
f1 = 1.1112
f2 = 111e-2
# complex number
c1 = 1 + 2j
c2 = complex(1, 2)
# boolean
b1 = True
b2 = False
# string triple quotation mark: change line
s1 = '111'
s2 = "111"
s3 = """111"""

# list
list1 = [1, 2, 3]

# tuple
tuple1 = (1, 2, 3)
tuple2 = 1, 2, 3

# dictionary
dict1 = {1: 2, 2: 3, 3: 4}

# set
set1 = {1, 2, 3, 4}

# transfer
s4 = str(dict1)
b3 = bool(a)

# && = and
# ! = not
# || = or
# include
b4 = 2 in set1
b5 = 2 not in set1
# check type
b6 = isinstance(set1, set)

# if / else
if b1:
    print(1)
elif b2:
    print(2)
else:
    print(3)

# while
while b1:
    print(1)
else:
    print("end")

# for
for n in set1:
    print(n)