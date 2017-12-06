N = int(input("Enter an integer: "))


def string_formatting(N):
    base = 1
    if 99 >= N >= 1:
        while base <= N:
            width = len('{0:b}'.format(N))
            print('{0:{w}d}'.format(base, w=width), '{0:{w}o}'.format(base, w=width),
                  '{0:{w}x}'.format(base, w=width).upper(), '{0:{w}b}'.format(base, w=width), )
            base += 1
    else:
        print("Your integer doesn't match constraints")
StringFormatting(N)
