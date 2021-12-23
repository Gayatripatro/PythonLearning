def largest_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max


print(largest_num_in_list([10, -892, 8, 218]))

# smalest number in the list
def smallest_num_in_list(list):
    small = list[0]
    for a in list:
        if a < small:
            small = a
    return small


print(smallest_num_in_list([10, -892, 8, 218]))