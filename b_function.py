# 2018/07/19
# definition
def func1():
    print("function 1")


def func2(a):
    print("function 2")
    print(a)


def func3(a=1, b=2):
    print(a, b)
    return a + b


def func4():
    global ga
    ga = 1


def func5():
    print(ga)


func1()
func2(1)
func3()
func4()
func5()
print(func3(1, 3))
