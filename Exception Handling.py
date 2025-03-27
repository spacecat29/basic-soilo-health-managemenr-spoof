try:
    num =  int(input("Enter A Number"))
    ans = 69/num
    print(ans)

except ValueError:
    print('Enter A Int NUmber')

except ZeroDivisionError:
    print('Enter A Divisible Number')

print('-----------------------------------------')

try:
    xy = int(input('Enter A Number'))
    yz = int(input('Enter A Number'))
    print(xy*yz)

except ValueError:
    print("Enter  number")

except ZeroDivisionError:
    print('Enter A Divisible Number')

print('-----------------------------------------')

a_list = [10,20,30,40]

try:
    vart = int(input('Enter A Number'))
    print('The Number Is: ',a_list[vart])

except ValueError:
    print("Enter A Value")

except ZeroDivisionError:
    print('Cant Divide By Zero')

print('-----------------------------------------')

try:
    filename = str(input('Enter A file name')) 
    with open(filename,'r') as read_it:
        content = read_it.read() 
        print(content)

except FileNotFoundError:
    print('Error This Shit Is NOt Here')
finally:
    print('End Of Program')

print('-----------------------------------------')

try:
    name_of_file = str(input('Enter A Fucking File Name'))
    with open(name_of_file,'r') as readitor:
        scanning = readitor.read() 
        print(scanning)

    try:
        vary = int(input('Enter A Number'))
        zuo = vary/100
        print(zuo)
    except ValueError:
        print('Cant Divide')

except  FileNotFoundError:
    print('no File FOund')

finally:
    print('End OF Program')

print('-----------------------------------------')

class InvalidAgeError(Exception):
    def __init__(self,age,message = 'Invalid Age Enter An Age'):
        self.age = age
        self.message = message
        super().__init__(self.message)

def check_the_age(age):
    if age < 0 or age > 99:
        raise InvalidAgeError(age)
    else:
        print('Valid Age')

try:
    aged = int(input('Input Age'))
    check_the_age(aged)

except InvalidAgeError as error:
    print(f"{error.message} You Entered Wrong Age {error.age}")

except ValueError:
    print('Not zProper Value')

finally:
    print('End Of Program')

print('-------------------------------------------')

try:
    with open('yoyo.txt','r') as reader_file:
        content = reader_file.read() 
        print(content)
    
    with open('name_of_file','w') as write_in_file:
        vartt = write_in_file.write(content)

except FileNotFoundError:
    print('Error Here')

except IOEError:
    print('ANother Error')

finally:
    print('This Shit is Over')