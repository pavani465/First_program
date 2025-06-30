a = int(input("Enter a value:"))
b = int(input("Enter a value:"))
c = input("Enter a opr:")

if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
else:
    print("Invalid opr")