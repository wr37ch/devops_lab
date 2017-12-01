ARRAY = {int(x) for x in input("ARRAY NUMBERS: ").split()}
A = {int(x) for x in input("A SET NUMBERS: ").split()}
B = {int(x) for x in input("B SET NUMBERS: ").split()}
happiness_counter = 0
for x in ARRAY:
    if x in A:
        happiness_counter += 1
    elif x in B:
        happiness_counter -= 1
print(happiness_counter)
