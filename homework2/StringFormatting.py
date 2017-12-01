while True:
    N = int(input("Enter an integer. (Enter 0 if you want to exit) : "))
    base = 1
    if N > 99:
        print("Your integer is greater than 99! Enter an integer which is less  than 99 ")
        continue
    elif N == 0:
        break
    elif N < 1:
        print("Your integer is less than 1! Enter an integer which is  greater than 1 ")
        continue
    else:
        while base <= N:
            width=len('{0:b}'.format(N))
            print('{0:{w}d}'.format(base, w=width), '{0:{w}o}'.format(base, w=width), '{0:{w}x}'.format(base, w=width).upper(), '{0:{w}b}'.format(base, w=width), )
            base += 1
