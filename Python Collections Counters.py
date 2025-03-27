#Counters

from collections import Counter

val = [1,2,2,3,3,3,4,4,4,4]
ctr = Counter(val)  
print(ctr)

#Creating A Counter

from collections import  Counter

ctr1 = Counter([1,2,2,3,3,3,4,4,4,4])

ctr2 = Coumter({1:2,2:3:1})

ctr3 = Counter('Hello')

print(ctr1)
print(ctr2)
print(ctr3)

#Accesing Counter Elements
from collections import Counter

ctr = Counter([1,2,2,3,3,3])

print(ctr[1])
print(ctr[2])
print(ctr[3])
print(ctr[4])

#Updating Counter

from collections import Counter
ctr = Counter([1,2,3])

#Adding new Elements
ctr.update([2,3,3,3])
print(ctr)


#Updating Counter

from  collections import Counter

ctr = Counter([1,2,2,3,3,3,3])
list_that_shit = list(ctr.elements())
print(list_that_shit)

#Counter Methods

from collections import Counter

ctr = Counter([1,2,2,3,3,3])
list_that_common = ctr.most_common(2)

print(list_that_common)



from collections import Counter
ctr = Counter([1,2,2,3,3,3])
ctr.subtract([2,3,3])

print(ctr)

#Arithmatic Operators On Counters

from collections import Counter

ctr1 = Counter([1,2,2,3])
ctr2 = Counter([2,3,3,4])

#Additon
print(ctr1+ctr2)
#subtract
print(ctr1-ctr2)
#Intersection
print(ctr1 & ctr2)
#Union
print(ctr1 | ctr2)


