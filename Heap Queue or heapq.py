#creating a Heapq
import heapq 

li = [50,40,20,15,10,30]

heapq.heapify(li) 

print("Heap Queue: ",li)

print('------------------------')

import heapq

h = [10,20,30,40,50]

heapq.heapify(h) 

#adding
heapq.heappush(h,5)
print(h)

#popping out smallest element from the Heapq 
min = heapq.heappop(h) 

print(h)

print('Smallest: ',min)
print(h)    

pritn('-------------------------------')

import heapq 

h = [10,20,30,40,50]
heapq.heapify(h) 

min = heapq.heappushpop(h,5)

print(min) 
print(h)

print('---------------------------------')

import heapq 

h = [10,20,30,40,50,50,70,80]
heapq.heapify(h)

maxi = heapq.nlargest(3,h) 
print('3 Laregst',maxi) 

mini = heapq.nsmallest(3,h) 
print("3 Smallest",mini)

import heapq 


list1 = [10,20,30,40]
heapq.heapify(list1)

repl = heapq.heapreplace(list1,5)
print(repl)
print(list1)

list2 = [50,60,70,80]

list3 = list(heapq.merge(list1,list2))
print("Mrged Heap",list3)
print('---------------------------------')

import heapq 


list1 = [10,20,30,40]
heapq.heapify(list1)

repl = heapq.heapreplace(list1,5)
print(repl)
print(list1)

list2 = [50,60,70,80]

list3 = list(heapq.merge(list1,list2))
print("Mrged Heap",list3)

print('-------------------------------')