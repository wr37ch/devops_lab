n_m = {int(x) for x in input().split()}
ARRAY = {int(x) for x in input().split()}
A = {int(x) for x in input().split()}
B = {int(x) for x in input().split()}
happiness_counter = 0
for x in ARRAY:
    if x in A and x not in B:
        happiness_counter += 1
    elif x in B and x not in A:
        happiness_counter -= 1
    else:
        continue
print(happiness_counter)
