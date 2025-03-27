def hello_decorator(func1):
    def inner_func1():
        print('This is before exxecution of code')

        func1()
        print('This is during end of executation of code')

    return inner_func1

def middle_function():
    print('This is during function')

middle_func = hello_decorator(middle_function)
middle_func()
print('----------------------------------------------------')

import time 
import math 

def calculate_time(func3):
    def inner1(*args,**kwargs):
        start = time.time()
        func3(*args,**kwargs)
        end = time.time()
        print('Total Time Taken: ',func3.__name__,end-start) 
    return inner1 

@calculate_time
def Factorial(numb):
    time.sleep(2)
    print(math.factorial(numb))

Factorial(9)
print('--------------------------------------------------------')

def new_deco(func2):
    def inner2(*args,**kwargs):
        print('This Before Execution')
        function_variable = func2(*args,**kwargs)
        print('This Is After Execution')
        return function_variable

    return inner2

@new_deco
def deco_func(a,b):
    print('inside the function')
    return a+b 

print('Sum Of This Shit',deco_func(1,2))

print('--------------------------------------------------------')

def funk1(samp):
    def innerfunck():
        function_var = samp() 
        return function_var*function_var
    return innerfunck


def funk2(samp2):
    def inner_funk2():
        function_var_2 = samp2()
        return 2*function_var_2
    return inner_funk2

@funk1
@funk2
def number():
    return 10 

@funk2
@funk1
def number2():
    return 10 


print(funk1(funk2(number())))
print(funk2(funk1(number2())))