from collections import deque

deq1 = deque(['name','DOB','age'])
print(deq1)

print('-------------------------------')

from collections import deque 

de = deque([10,20,30])

#add elements to the right
de.append(40)
#add elements to the left
de.appendleft(5)
#extend iterable
de.extend([50,60,70])
print("After Extend([50,60,70]): ",de)
#extendleft(iterable)
de.extendleft([0,5])
print("After Extend([0,5]):",de)
#remove method
de.remove(20)
print('After Rmeoving(20): ',de)  
#remove elements from the right
de.pop()
#remove elements from thr left
de.popleft() 
print("After Pop and Popleft: ",de)
#clear()-Removes a;; elements from the deque
de.clear()
print("After Clear():",de)


print('-------------------------------')

import collections

de = collections.deque([1,2,3,3,4,2,4])

#Acessing elements by index
print(de[0])
print(dq[-1])

#finding the lenght of the deque
print(len(de))

print("-----------------------------------")

from collections import  deque 
#creating a deque
de = deque([10,20,20,30,30,40,50,60,70,80])
#countinhg a deque
print(de.count(20))
print(de.count(30))
#Rotating THe Deque 2 steps to the right
de.rotate(2)
print(de) 
#Rotating THe Deque 3 steps to the left
de.rotate(-3)
print(de) 
#reverse the deque
de.reverse()
print(de)