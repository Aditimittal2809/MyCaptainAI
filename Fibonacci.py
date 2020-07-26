nterms = int(input("How many terms? "))
n1 = 0
n2 = 1
count = 0
if nterms<=0:
    print("Enter valid number of terms")
elif nterms==1:
    print("Fibonacci series upto " + str(nterms) + " is:")
    print(n1)
else:
    print("Fibonacci series is:")
    while count<nterms:
        print(n1)
        next = n1 + n2
        n1 = n2
        n2 = next
        count+=1
