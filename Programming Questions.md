## List Programming Questions
* Write a Python function to find the maximum and minimum values in a given list.
```#find the maximum and minimum values in a given list
#With Function
def find_max_min(list):
    max = list[0]
    min = list[0]
    for num in list:
        if num > max:
            max = num
        elif num < min:
            min = num
    return min,max
lists = [10,30,800,8,90]
print(find_max_min(lists))


#Without Function
list = [10,30,800,8,90]
max = list[0]
min = list[0]
for num in list:
    if num > max:
        max = num
print("Maxmum value of the list is",max)
for num in list:
    if num < min:
        min = num
print("minimum value of the list is", min)
```
* Write a Python function to calculate the sum and average of elements in a list.
```#calculate the sum and average of elements in a list
#With Function
def calculate_sum_avg(list):
    sum = 0
    avg = 0
    for i in list:
        sum = sum + i
        avg = sum / len(list)
    return sum,avg
    #return sum is (sum), avg is (avg)
list = [100,910,20,30,40,500]
print(calculate_sum_avg(list))

#Without Function
list = [100,910,20,30,40,500]
sum = 0
avg = 0
for i in list:
    sum = sum + i
    avg = sum / len(list)
print(sum)
print(avg)
```
* Write a Python function to remove duplicate elements from a list while preserving the original order.
```#remove duplicate elements from a list while preserving the original order
#With Function
def remove_duplicate_ele(list):
    unique_list = []
    for element in list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

list = [10, 30, 1, 10, 50, 80, 1]
print("Original list is: ", list)
print("After removing Duplicate element from the original list is:", remove_duplicate_ele(list))

#Without Function
list = [10,30,1,10,50,80,1]
unique_list = []
for element in list:
    if element not in unique_list:
        unique_list.append(element)
print("Original list is: ", list)
print("After removing Duplicate element from the original list is:",unique_list)
```


* Write a Python function to create a new list containing the squares of elements from the given list.
```#create a new list containing the squares of elements from the given list.
list = [4,10,20,60,2]
new_square_list = []
for ele in list:
    ele = ele * ele
    new_square_list.append(ele)
print(new_square_list)```

* Write a Python function to reverse a given list.
* Write a Python function to count the occurrences of a specific element in a list.
* Write a Python function to merge two sorted lists into a single sorted list.
* Write a Python function to rotate a given list to the left by a specified number of positions.
* Write a Python function to find the missing number in a list containing consecutive numbers from 1 to n.
* Write a Python function to remove all negative numbers from a list.
