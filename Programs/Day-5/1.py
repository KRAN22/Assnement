# Assignment 1

def noZero(fnc):
    def helper(*args):
        print("Welcome......")
        print(fnc(*args))
    return helper


@noZero
def div(x,y):
	return x/y

@noZero
def mul(x,y):
	return x*y

@noZero
def add(x,y):
	return x+y
@noZero
def sub(x,y):
	return x-y

zero = noZero(add)
# zero(10,20)
add(10,20)
div(10,20)
mul(10,20)
sub(10,20)
