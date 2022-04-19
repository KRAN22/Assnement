# Assignment 2

def drawborder(x,y,z):
    print(x,y,z)
    def function(fnc):
        def helper(*args):
            print("Welcome.....")
            fnc(*args)
        return helper
    return function

@drawborder('*','#',40) 
def greet(msg):
    print("greet",msg)

@drawborder('=','_',30)
def RSVP(msg): 
    print("RSVP",msg)


greet("hello")
RSVP("HELLO")
