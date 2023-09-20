n = int(input("Enter the number "))
for x in range(2,n):
    if n%x==0:
        print("Not Prime")
        break
else:
    print("Prime")
