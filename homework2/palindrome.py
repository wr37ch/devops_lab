# -*- coding: utf-8 -*-
a = input("Enter your word: ")


def palindrome(a):
    print(a[::-1])
    if a == a[::-1]:
        print(a + " is a palindrome")
    else:
        print(a + " is not a palindrome")

palindrome(a)
