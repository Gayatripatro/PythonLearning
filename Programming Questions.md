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
* Write a Python function to create a new list containing the squares of elements from the given list.
* Write a Python function to reverse a given list.
* Write a Python function to count the occurrences of a specific element in a list.
* Write a Python function to merge two sorted lists into a single sorted list.
* Write a Python function to rotate a given list to the left by a specified number of positions.
* Write a Python function to find the missing number in a list containing consecutive numbers from 1 to n.
* Write a Python function to remove all negative numbers from a list.
