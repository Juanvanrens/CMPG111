def determineLowest(list):
    lowestnumber = list[0]
    for i in list:

        if i < lowestnumber:
            lowestnumber = i

    return lowestnumber

def determineHighest(list):
    highestnumber = list[0]
    for i in list:

        if i > highestnumber:
            highestnumber = i

    return highestnumber

def determineTotal(list):
    total = 0
    for i in list:
        total += i

    return total


def determineAverage(total):

    average = total/20

    return average


def main():

    list = []
    for i in range(0,20):
        number = int(input("Enter a number: "))
        list.append(number)

    lowest = determineLowest(list)
    highest = determineHighest(list)
    total = determineTotal(list)
    average = determineAverage(total)

    print("\n---SUMMARY---")
    print("The lowest number is ", lowest)
    print("The highest number is ", highest)
    print("The total is", total)
    print("The average is", average)



if __name__ == "__main__":
    main()