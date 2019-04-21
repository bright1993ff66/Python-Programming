# Date: 2018-02-19
# Title: Popular Sorting Algorithms in Python
# Author: Haoliang Chang

#*****************************************************************

# First we import some modules we need
import sys

# Bubble Sort(O^2)

def bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i+1]:
                exchanges = True
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
            else:
                pass
        pass_num -= 1

# Selection Sort(O^2)
		
def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1): # fill_slot means the position in which we want to put our numbers
        pos_of_max = 0 # first we initially set the max value of this collection is a_list[0]
        for location in range(1, fill_slot + 1): # Here we create location because we want to compare other numbers with a_list[0]
            if a_list[location] > a_list[pos_of_max]: # From min to max
                pos_of_max = location
                
        a_list[fill_slot], a_list[pos_of_max] = a_list[pos_of_max], a_list[fill_slot]
		
# Insertion Sort(O^2)

def insertion_sort(a_list):
    
    for index in range(1, len(a_list)):
        current_value = a_list[index] # The current value would always hold the first value after the sublist
        position = index
        
        while position > 0 and a_list[position - 1] > current_value: # compare every item in the sublist with the current value
            a_list[position] = a_list[position - 1]
            position -= 1
            
        a_list[position] = current_value
		
# Shell Sort(Between O(n) and O(n^2)

def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
       
        print("After the increments", sublist_count, "the list becomes", a_list)
        
        sublist_count = sublist_count // 2
        
def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        
        while position > 0 and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position -= gap
            
        a_list[position] = current_value
		
# Merge Sort(O(nlogn), but need additional space for the merging process)

def merge_sort(A):
    merge_sort_helper1(A, 0, len(A)-1)
    
def merge_sort_helper1(A, first, last):
    if first < last: # To check whether the length of the list is 1 or not
        middle = (first + last) // 2
        merge_sort_helper1(A, first, middle)
        merge_sort_helper1(A, middle + 1, last)
        merge_sort_helper2(A, first, middle, last)
        
def merge_sort_helper2(A, first, middle, last):
    L = A[first:middle + 1]
    R = A[middle + 1:last + 1]
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i = j = 0
    
    for k in range(first, last+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
			
# Quick Sort(O(nlogn), but may degrade to O(n^2) if the split points are not near the middle of the list. No additional space is required.)

def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list)-1)
    
def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)
        
def partition(a_list, first, last):
    pivot_value = a_list[first]
    
    left_mark = first + 1
    right_mark = last
    done = False
    
    while not done:
        
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark += 1
            
        while right_mark >= left_mark and a_list[right_mark] >= pivot_value:
            right_mark -= 1
            
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]
            
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]
    
    return right_mark

def sort_the_list(fun_name, a_list):
    """Given a sorting algorithm name, return the corresponding sorted list."""
    if fun_name == 'bubble_sort':
        return bubble_sort(a_list)
    if fun_name == 'selection_sort':
        return selection_sort(a_list)
    if fun_name == 'insertion_sort':
        return insertion_sort(a_list)
    if fun_name == 'shell_sort':
        return shell_sort(a_list)
    if fun_name == 'merge_sort':
        return merge_sort(a_list)
    if fun_name == 'quick_sort':
        return quick_sort(a_list)
    else:
	raise ValueError('%s is not a valid sorting algorithm.' % fun_name)
		
# Test our functions
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sort_the_list('bubble_sort', a_list)
print(a_list)
