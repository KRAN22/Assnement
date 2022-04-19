# Assignment 3

def logBeforeAfter(fnc):
    def helper(*args,):
        print("welcome.......")
        fnc(*args)
    return helper

@logBeforeAfter
def fun(x, y):
    print("fun", x, y)

@logBeforeAfter
def fun1(*args):
    print("fun1", args[2])

@logBeforeAfter
def fun2(**kwargs):
    print("fun2", kwargs)

@logBeforeAfter
def fun3(*args, **kwargs):
    print("fun3", args, kwargs)

logBeforeAfter(fun)

fun(10,20)
fun1("Kranthi","bharagv","ajay")
fun2()
fun3()
