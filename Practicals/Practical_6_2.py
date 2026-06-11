import random




def generateRandom():
    numbers = []
    random.seed(111)
    for i in range(7):

        numbers.append(random.randint(1, 49))
    
    return numbers

def selectNumbers():
    usernumbers = []

    for i in range(7):
        num = int(input("Enter a number: "))
        while num < 1 or num > 49:
            print("Error, please enter a number between 1 and 49")
            num = int(input("Enter a number: "))
        usernumbers.append(num)

    print(f"Your numbers are {usernumbers}", end=" ")

    return usernumbers

def displayLottery(lottery_numbers, usernumbers):
    lottery_numbers.sort()
    matches = []
    print("")
    

    for num in lottery_numbers:
        if num in usernumbers:
            matches.append(num)
    print("The lotto numbers are:", lottery_numbers)
    print("\nThe matches are:", matches)


def main():
    print("\n[0,0,0,0,0,0,0]\n")
    usernumbers = selectNumbers()
    lottery_numbers = generateRandom()
    displayLottery(lottery_numbers, usernumbers)

if __name__ == "__main__":
    main()
