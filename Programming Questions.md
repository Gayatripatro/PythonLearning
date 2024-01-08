## List Programming Questions
* Write a Python function to find the maximum and minimum values in a given list.
``` # find the maximum and minimum values in a given list
# With Function
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


# Without Function
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
```# calculate the sum and average of elements in a list
# With Function
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

# Without Function
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
``` # remove duplicate elements from a list while preserving the original order
# With Function
def remove_duplicate_ele(list):
    unique_list = []
    for element in list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

list = [10, 30, 1, 10, 50, 80, 1]
print("Original list is: ", list)
print("After removing Duplicate element from the original list is:", remove_duplicate_ele(list))

# Without Function
list = [10,30,1,10,50,80,1]
unique_list = []
for element in list:
    if element not in unique_list:
        unique_list.append(element)
print("Original list is: ", list)
print("After removing Duplicate element from the original list is:",unique_list)
 ```


* Write a Python function to create a new list containing the squares of elements from the given list.
``` # create a new list containing the squares of elements from the given list.
list = [4,10,20,60,2]
new_square_list = []
for ele in list:
    ele = ele * ele
    new_square_list.append(ele)
print(new_square_list)
```

* Write a Python function to reverse a given list.
``` # reverse a given list
list = [10,40,2,30,10,90]
reversed_list = []
for elements in list:
    reversed_list.insert(0,elements)
print(reversed_list)

left = 0
right = len(list) - 1
while (left < right):
    # Swap
    temp = list[left]
    list[left] = list[right]
    list[right] = temp
    left += 1
    right -= 1
print(list)
```

* prime number for a given number
``` list1=[]
for num in range(1,100):
    if num>1:
        for i in range(2,num):
            if num%i ==0:
                break
        else:
            list1.append(num)
print(list1)

# using list comp 
Prime_num = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, num))]
print(Prime_num)
```
* Palindrome Palooza: [Create a list of all 3-digit palindromic numbers using list comprehension. (e.g., 121, 133, 292)]
* Write a Python function to count the occurrences of a specific element in a list.
* Write a Python function to merge two sorted lists into a single sorted list.
* Write a Python function to rotate a given list to the left by a specified number of positions.
* Write a Python function to find the missing number in a list containing consecutive numbers from 1 to n.
* Write a Python function to remove all negative numbers from a list.

## String Programming Questions
1. Anagram Check:
Write a function to determine if two strings are anagrams of each other. Anagrams are strings that have the same characters, but in a different order.

2. Longest Palindromic Substring:
Write a function to find the longest palindromic substring in a given string.

3. String Compression:
Write a function that performs basic string compression using the counts of repeated characters. For example, the string "aabcccccaaa" would become "a2b1c5a3". If the compressed string is not shorter than the original, return the original.

4. Regular Expression Matching:
Implement a function that checks if a given string matches a given regular expression.

5. Reverse Words in a String:
Write a function to reverse the order of words in a given string, while keeping the words themselves unchanged.

6. String Rotation:
Write a function that determines whether one string is a rotation of another. For example, "waterbottle" is a rotation of "erbottlewat".

7. First Non-Repeated Character:
Write a function to find and return the first non-repeated character in a string.

8. Minimum Window Substring:
Given two strings, S and T, find the minimum window in S which will contain all the characters in T.

9. Implement strStr():
Write a function that finds the index of the first occurrence of a substring in a given string. If the substring is not found, return -1.

10. Valid Palindrome:
Write a function that determines whether a given string is a palindrome, considering only alphanumeric characters and ignoring cases.

11. Group Anagrams:
Given an array of strings, group anagrams together. Two strings are anagrams if they contain the same characters but in a different order.

12. RLE Iterator:
Implement a run-length encoded string iterator. Given a run-length encoded string, implement an iterator that iterates through the original string.

13. Longest Common Subsequence:
Write a function that finds the length of the longest common subsequence between two strings.

14. Count and Say Sequence:
Implement the "count and say" sequence. Given an integer n, generate the nth sequence.

15. Valid Parenthesis String:
Write a function that determines whether a given string containing only '(', ')', and '*' characters is a valid parenthesis string.
