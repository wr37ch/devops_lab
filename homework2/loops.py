while True:
    N = int(input("Enter an integer. (Enter 0 if you want to exit) : "))
    base = 0
    if N > 20:
        print("Your integer is greater than 20! Enter an integer which is not greater than 20 ")
        continue
    elif N == 0:
        break
    else:
        while base < N:
            print(base*base)
            base += 1
