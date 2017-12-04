a = input("Enter your string: ")
def functionname(a):
    result = ' '.join(w[::-1] for w in a.split())
    print(result)
    
functionname(a)
