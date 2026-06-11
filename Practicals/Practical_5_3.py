import math

MAX_NUMBERS = 5

def analyseSum(Total):
    sum = Total
    squareroot = Total**0.5
    log = math.log(Total)

    print(f"\tThe sum of the numbers is: {sum: .2f}")
    print(f"\tThe square root of the sum: {squareroot: .4f}")
    print(f"\tThe logarithm of the sum of the numbers: {log: .4f}")


def main():
    Total = 0
    for i in range(MAX_NUMBERS):
        number = int(input(f"Enter a positive real number #{i+1}: "))

        while number < 0:
            number = int(input("Enter a number: "))

        Total += number

    analyseSum(Total)

    return Total




if __name__ == "__main__":
    main()