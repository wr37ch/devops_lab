N = int(input("Enter your number: "))
def loops(N):
    base = 0
    if 1 <= N <= 20:
        while base < N:
            print(base * base)
            base += 1
        return

    else:
        print("Your integer is greater than 20 or less than 1! Enter the right one ")

loops(N)
