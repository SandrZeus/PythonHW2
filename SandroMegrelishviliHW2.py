#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Sandro Megrelishvili 39851214
f = open("data.txt", "r")
data = f.read()#List
list1 = [float(x) for x in data.split()] #convert list1 to float
list2 = [float(x) for x in data.split()] #convert list2 to flaot
from matplotlib import pyplot as plt #drawing1 for unsorted list
plt.plot(list1,range(len(list1)))
plt.ylabel('item')
plt.xlabel('data')
plt.show()
import time #timer1
start1 = time.time() #time start1
def bubblesort(list2): #Bubble Sort list2
    swapped = False
    for n in range(len(list2)-1, 0, -1):
        for i in range(n):
            if list2[i] > list2[i + 1]:
                swapped = True
                list2[i], list2[i + 1] = list2[i + 1], list2[i]       
        if not swapped:
            return
bubblesort(list2)
end1 = time.time() #stop time1
TimeElapsed1 = (end1 - start1)
from matplotlib import pyplot as plt #drawing2 for sorted list
plt.plot(list2,range(len(list2)))
plt.ylabel('item')
plt.xlabel('data')
plt.show()
import time #timer2
start2 = time.time() #start time2
def selectionSort(list2, size): #Selection Sort list2 
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if list2[j] < list2[min_index]:
                min_index = j
        (list2[ind], list2[min_index]) = (list2[min_index], list2[ind])
size = len(list2)
selectionSort(list2, size)
end2 = time.time() #stop time2
TimeElapsed2 = (end2 - start2)
print('The elapsed time of Bubble Sort is:', TimeElapsed1, 'seconds')
print('The elapsed time of Selection Sort is:', TimeElapsed2, 'seconds')
if TimeElapsed1>TimeElapsed2: #the name of the fastest algorithm
    print('The fastest algorithm is Selection Sort:', TimeElapsed2, 'seconds')
else:
    print('The fastest algorithm is Bubble Sort:', TimeElapsed1, 'seconds')
f.close()


# In[ ]:




