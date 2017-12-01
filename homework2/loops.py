N = int(input("Enter your number: "))
def loops(N):
    base = 0
    if N > 20:
        print("Your integer is greater than 20! Enter an integer which is not greater than 20 ")
    else:
        while base < N:
            print(base * base)
            base += 1
        return

loops(N)
