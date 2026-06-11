a = int(input("Enter the length of stick #1: "))
b = int(input("Enter the length of stick #2: "))
c = int(input("Enter the length of stick #3: "))

if (a + b) > c and (b + c) > a and (a + c) > b:
    print("Triangle possible")

    if a == b == c:
        print("Equilateral triangle possible")

    elif a == b or b == c or c == a:
        print("Isosceles triangle possible")

    else:
        print("Scalene triangle possible")


else:
    print("No Triangle possible")

