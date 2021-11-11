#using len(): len() is used for print the length of the string
str1 = "Sabya"
print(len(str1))

# take the input from user and without using len()


def get_length_of_string(input_str):
    len = 0
    for ch in input_str:
        len += 1
    return len


def get_splitted_string(input_str):
    start, end = 0, 0
    splitted_list =[]
    for ch in input_str:
        if ch !=' ':
            end+=1
        else:
            splitted_list.append(input_str[start:end])
            start, end = end+1, end+1

    splitted_list.append(input_str[start:end])
    return splitted_list

def main():
    strs = input("give the input for finding the length of a string :")
    splitted_list = get_splitted_string(strs)
    for str1 in splitted_list:
        len = get_length_of_string(str1)
        print("the input string is : {} lenth is {}".format(str1, len))

main()
