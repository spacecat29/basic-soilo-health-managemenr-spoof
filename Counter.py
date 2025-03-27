from collections import Counter 

val = [1,2,2,3,3,3,4,4,4,4]

ctr = Counter(val)   

print(ctr)

print('----------------------------')


#syntax class collecitons.Counter([iterable-or-maping])

print('----------------------------')


from collections import  Counter 

ctr1 = Counter([1,2,2,3,3,3])

ctr2 = Counter({1:3,2:1,3:2})

ctr3 = Counter('hello')

print(ctr1)
print(ctr2)
print(ctr3)

print('----------------------------')


from collections import Counter 
ctr = Counter([1,2,2,3,3,3,4,4,4,4])

print(ctr[1])
print(ctr[2])
print(ctr[3])
print(ctr[4])
print(ctr[5])

print('----------------------------')

from collections import Counter

ctr = Counter([1,2,3])
ctr.update([4,5,6])
print(ctr)

print('-------------------------------')

from collections import Counter 
 
ctr = Counter([1,2,2,3,3,3,4,4,4,4])
items = list(ctr.elements())

print(items)

print('-------------------------------')

from collections import Counter 

ctr = Counter([1,2,3,4,5,6,6,6,7,8,9,9,9])
items  = ctr.most_common()
print(items)

print('-------------------------------')

from collections import Counter 

ctr = Counter([1,2,2,2,3,3,3,3,3])
ctr.subtract([2,3,3])
print(ctr)

print('-------------------------------')

from collections import Counter

ctr1 = Counter([1,2,2,3])
ctr2 = Counter([2,3,3,4])

print(ctr1 + ctr2)

print(ctr1 - ctr2)

print(ctr1 & ctr2)

print(ctr1 | ctr2)
