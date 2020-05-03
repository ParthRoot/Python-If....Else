# find largest value of three

a = float(input("Enter the number of a : \n"))
b = float(input("Enter the number of b : \n"))
c = float(input("Enter the number of c : \n"))
if a > b and a > c:
    print("a is maximum")
elif a < b and b > c:
    print("b is maximum")
elif a == b and a == c:
    print("both are same")
elif a == b and a > c:
    print("a and b are same ")
    print("a and b are max")
elif a == c and a > b:
    print("a and c are same ")
    print("a and c are max")
elif b == c and a < b:
    print("b and c are same ")
    print("b and c are max")
else:
    print("c is maximum")




