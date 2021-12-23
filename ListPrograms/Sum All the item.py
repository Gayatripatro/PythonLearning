def sum_All_list(items):
    sum = 0
    for x in items:
        sum += x
    return sum


print(sum_All_list([1, 2, -8]))
print(sum_All_list([10, 20, 80]))


# multiplies all the numbers in the list
def Mul_All_list(items):
    Multiplied_number = 1
    for x in items:
        Multiplied_number = x * Multiplied_number
    return Multiplied_number


print(Mul_All_list([5, 2, 8]))
