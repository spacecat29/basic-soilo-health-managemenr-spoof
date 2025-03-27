from collections import OrderedDict

print("This IS Dict")
sadha_dict = {}
sadha_dict['a']=1
sadha_dict['b']=2
sadha_dict['c']=3
sadha_dict['d']=4

for key,value in sadha_dict.items():
    print(key,value)

print('This Is Oredered Dict')

oreder_dict = OrderedDict()
oreder_dict['a'] = 1
oreder_dict['b'] = 2
oreder_dict['c'] = 3
oreder_dict['d'] = 4

for key,value in oreder_dict.items():
    print(key,value)

print("---------------------------------------------")

from collections import OrderedDict

print("Before")
od = OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4

for key,value in od.items():
    print(key,value) 
    

od['c'] = 5 
print()
for key,value in od.items():
    print(key,value) 

print("---------------------------------------------")

from collections import OrderedDict

od1 = OrderedDict([('a',1),('b',2),('c',3)])
od2 = OrderedDict([('c',3),('b',2),('a',1)])

print(od1==od2)

print("---------------------------------------------")

from collections import defaultdict

d = defaultdict(int)  

L = [1,2,3,4,2,4,1,3,5]

for i in L:
    d[i]+=1
print(d)

print('-----------------------------------------------')