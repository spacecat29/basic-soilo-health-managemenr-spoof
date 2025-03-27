from collections  import OrderedDict

print('THis is A ORdinary Dict')

dicto = {}
dicto['a'] = 1
dicto['b'] = 2
dicto['c'] = 3
dicto['d'] = 4

for key,value in dicto.items():
    print(key,value)  

print("This is an Oredered Dict")

orddict = {}
orddict['a'] = 1
orddict['b'] = 2
orddict['c'] = 3
orddict['d'] = 4

for key,value in orddict.items():
    print(key,value)

print('---------------------------------')

from collections import OrderedDict 

print("Before: ")
od = OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4
for key,value in od.items():
    print(key,value)  

print("AFter: ")
od['c']=5
for key,value in od.items():
    print(key,value)

print('---------------------------------')

from collections import OrderedDict

od1 =  OrderedDict([('a',1),('b',2),('c',3)])
od2 =  OrderedDict([('c',3),('b',2),('a',1)])

print(od1 == od2)

print("-----------------------------------")

from collections import OrderedDict

my_dict = OrderedDict([('a',1),('b',2),('c',3)])

reversed_shit = OrderedDict(reversed(list(my_dict.items())))

for key,value in reversed_shit.items():
    print(key,value)

print("-----------------------------------")

from collections import OrderedDict

my_dict = OrderedDict([('a',1),('b',2),('c',3)])
last_item = my_dict.popitem(las=True)

print(last_item)

print("------------------------------------")

from collections import OrderedDict

my_dict = OrderedDict([('a',1),('b',2),('c',3)])

my_dict.move_to_end('a')

my_dict.move_to_end('b',last=False) 

for key,value in my_dict.items():
    print(key,value)  

print("------------------------------------")

from collections import OrderedDict

print("This is Orederd SHit ")

odz = OrderedDict()
odz['a']=1
odz['b']=2
odz['c']=3
odz['d']=4

for key,value in odz.items():
    print(key,value)

print('Deleted')
odz.pop('c')
for key,value in odz.items():
    print(key,value)

print('Inserting') 
odz['c']=3
for key,value in odz.items():
    print(key,value) 

print("------------------------------------")

from collections import OrderedDict

my_dict = OrderedDict([('a',1),('b',2),('c',3)])

my_dict['d'] = 4 

my_dict.update([('e',5),('f',6)])
my_dict.move_to_end('e',last=False) 

for key,value in my_dict.items():
    print(key,value)

print("------------------------------------")
