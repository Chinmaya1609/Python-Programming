def fibno(n):
    if n<= 1:
        return n
    else:
        return(fibno(n-1)+fibno(n-2))
print("Enter the positive integer:")

nterms=int(input())
if nterms <= 0:
    print("Please enter a positve integer")
else:
    print("Fibonacci Sequence:")
    for i in range(nterms):
        print(fibno(i))
        
