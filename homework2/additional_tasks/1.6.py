# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

a = input("first list ")
list_a = set(map(int, a.split()))
b = input("second list ")
list_b = set(map(int,b.split()))

z = list_a.symmetric_difference(list_b)
for x in sorted(z):
    print(x)
