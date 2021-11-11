def isPalindrome(Palindrom_str):
    return Palindrom_str == Palindrom_str[::-1]


def main():
    Palindrom_str = isPalindrome(input("Enter a string "))

    if Palindrom_str:
        print("Yes")
    else:
        print("No")
main()

