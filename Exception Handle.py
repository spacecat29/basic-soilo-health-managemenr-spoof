x = 5
y = 'hello'
try:
    z = x+y
except TypeError:
    print("Error Can't be Figured Out")

print('---------------------------------------------------')
a = [1,2,3]
try: 
    print('Second Element = ', a[0])
    print('Second Element = ', a[3])

except:
    print('Error Occured')
print('---------------------------------------------------')
#Specific Exception
def fun(a):
    if a < 6:
        b = a/(a-3)

    print('Value Of B= ',b)

try:
    fun(5)
    fun(3)

except ZeroDivisionError:
    print('Zero Division Error Here')

except NameError:
    print('Name Error Here')

print('---------------------------------------------------')

def AbyB(a,b):
    try :
        c = ((a+b)/(a-b))

    except ZeroDivisionError:
        print('ZeroDivision Error Is Here')

    except:
        print(c)

AbyB(115,30)
AbyB(3,3)

