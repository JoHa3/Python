string_input = input("input string ")
palindrome = True
string_length = len(string_input)
for i in range(string_length // 2):
    if string_input[i] != string_input[string_length - 1 - i]:
        palindrome = False
        break
if palindrome:
    print("palindrome")
else:
    print("is not palindrome")