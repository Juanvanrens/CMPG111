def calcAverage(total):
    average = total/5
    return average


def determineGrade(average):
    if 90 <= average <= 100:
        return "A"
    elif 80 <= average <= 89:
        return "B"
    elif 70 <= average <= 79:
        return "C"
    elif 60 <= average <= 69:
        return "D"
    else:
        return "F"


def main():
    total = 0
    for i in range(5):
        testscores = int(input("Please enter your test score: "))
        total += testscores

    avg = calcAverage(total)
    grade = determineGrade(avg)

    print("Your average is", avg)
    print("Your grade is", grade)



if __name__ == "__main__":
    main()
