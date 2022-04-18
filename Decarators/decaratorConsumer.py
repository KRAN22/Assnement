from .noAgrspackage import fun_file as dec 
from .noAgrspackage import class_file as dwc
from .argrsPackage import fun_file as dwia
from .argrsPackage import class_file as cdwia

  
@dec.begin_end 
def fun2(a,b):
    print(f"we will win the soccer WC {a} {b}")

fun2(111, 222)


@dwc.StartStop
def fun3(x, y, z):
    print(f"Happy Sunday fun3 {x} {y} {z}")

fun3(10,20,30)


@dwia.dec_with_arg("Sachin","Suarav","Rahul")
def fun4(x, y):
    print(f"fun4 .. {x} {y}")

fun4(88, 77)


@cdwia.StartStopwitharguement("Dhoni","kohli","Rohit")
def fun5(x,y):
    print(f"I am from fun5 {x} {y}")

fun5(678, 567)
