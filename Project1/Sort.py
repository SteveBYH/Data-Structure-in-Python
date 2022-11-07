import time
from random import randint, shuffle
from copy import deepcopy

inc_ins_list=[[i for i in range(q)] for q in [1000,2500,5000,7500,10000]]#create a list containing all the test lists in increasing order
inc_sel_list=deepcopy(inc_ins_list)#create an identical list
ran_ins_list=[]
for i in inc_ins_list:
    q = deepcopy(i)
    shuffle(q)
    ran_ins_list.append(deepcopy(q))
ran_sel_list = deepcopy(ran_ins_list)
dec_ins_list=[[i for i in range(q,0,-1)] for q in [1000,2500,5000,7500,10000]]
dec_sel_list=deepcopy(dec_ins_list)

def insertion_sort(arr):
    for k in range (1,len(arr)):
        j = k
        cur = arr[k]
        while j>0 and arr[j-1]>cur:
            arr[j]=arr[j-1]
            j = j-1
        arr[j] = cur

def selection_sort(arr):
    for k in range (len(arr)):
        j = k + 1
        curr = arr[k]
        pos = k
        while j < len(arr):
            if curr > arr[j]:
                curr = arr[j]#record the list element
                pos = j#record the position
            j = j+1      
        arr[pos] = arr[k]
        arr[k] = curr

def insertion_time(arr,sort_type):
    start = time.process_time()
    insertion_sort(arr)
    end = time.process_time()
    print(str(len(arr))+ str(sort_type) + '{:.6f}'.format(end-start))

def selection_time(arr,sort_type):
    start = time.process_time()
    selection_sort(arr)
    end = time.process_time()
    print(str(len(arr))+ str(sort_type) + '{:.6f}'.format(end-start))

if __name__ == '__main__':
    for i in inc_ins_list:
        insertion_time(i, " increasing insertion ")
    for i in inc_sel_list:
        selection_time(i, " increasing selection ")
    for i in ran_ins_list:
        insertion_time(i, " random insertion ")
    for i in ran_sel_list:
        selection_time(i, " random selection ")
    for i in dec_ins_list:
        insertion_time(i, " decreasing insertion ")
    for i in dec_sel_list:
        selection_time(i, " decreasing selection ") 