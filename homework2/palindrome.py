a = raw_input("Enter your word: ")
if a == a[::-1]:
    print(a + " is a palindrome")
else:
    print(a + " is not a palindrome")
