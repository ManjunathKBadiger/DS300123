# Check character is vowel or not

char = input("Enter a character : ")
lenght = len(char)
# print("lenght of character ", lenght)
vowels = "aeiouAEIOU"
if lenght == 1:
    if char in vowels:
        print("Yes it is vowel")
    else:
        print("it is not vowel")
else:
    print("Please enter a single character")