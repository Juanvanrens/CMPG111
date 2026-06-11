print("==================================\n"
      "     CMPG 111 PRACTICE MENU\n"
      "==================================\n"
      "1. FINANCIAL DECISIONS\n"
      "2. GENERAL CONDITION CHECKING\n"
      "3. TEXT / COMPARISON TASKS\n"
      "4. ACADEMIC TASKS\n"
      "==================================")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:

    print("\na. Determine Sales Bonuses\n"
          "b. Checking Payment Satus\n"
          "c. Salary comparison\n"
          "d. Loan Qualification Assessment\n"
          "e. Special offer Eligibility")

    choice = input("Enter your choice (a-e):")

    if choice == "a":
        sales = int(input("Please enter your sales: "))

        if sales > 5000:
            print("Your bonus: 500.0")
            print("Your sales:", sales)

        elif sales < 5000:
            print("Your sales:", sales)

    if choice == "b":
        balance = int(input("Please enter your balance: "))
        amount = int(input("Please enter the payment amount: "))

        if balance == 0:
            print("Insufficient funds")

        if balance != amount:
            print("You have not paid enough")


    if choice == "c":
        salary = int(input("Please enter your salary: "))

        if salary <= 20000:
            print("Small Salary")

        else:
            print("Big Salary")

    if choice == "d":
        salary = int(input("Please enter your salary: "))
        years = int(input("Please enter your years on job: "))

        if salary >= 30000:
            if years >= 2:
                print("You qualify for the loan")

            elif years < 2:
                print("You must have been on your current job for at least 2 years")

        else:
            print("You must earn at least 30k to qualify")

    if choice == "e":
        age = int(input("Please enter your age: "))
        student = input("Are you a student? (yes/no): ")

        if age > 60 or student == "yes":
            print("You get the special")

        else:
            print("You do not get the special.")\


elif choice == 2:

    print("a. Weather Temperature Evaluation\n"
          "b. Lego Age Restriction\n"
          "c. Even Number Checker\n")

    choice = input("Enter your choice (a-c)")
    if choice == "a":
        temp = int(input("Please enter the temperature: "))

        if temp < 40:
            print("A little cold, isn't it?")

        else:
            print("Nice weather we're having.")

    elif choice == "b":
        age = int(input("Please enter your age: "))

        if 4 <= age <= 94:
            print("You can play Lego")

        else:
            print("You cannot play Lego")



    elif choice == "c":
        num = int(input("Enter a number: "))

        if num % 2 == 0:
            print("Even number!")

        else:
            print("Uneven number!")

    else:
        print("Invalid sub - menu choice.")

elif choice == 3:
    choice = input("Enter your choice (a): ")

    if choice == "a":
        user1 = input("Please enter User 1: ")
        user2 = input("Please enter User 2: ")

        if user1 == user2:
            print(user1, "=", user2)

        elif user1 > user2:
            print(user1, ">", user2)

        elif user1 < user2:
            print(user1, "<", user2)

    else:
        print("Invalid sub - menu choice.")

elif choice == 4:
    choice = input("Enter your choice (a):")
    if choice == "a":
        score = int(input("Please enter your score: "))

        if score >= 90:
            print("Your grade is A")
        elif 80 <= score < 90:
            print("Your grade is B")
        elif 70 <= score < 60:
            print("Your grade is C")
        elif 60 <= score < 70:
            print("Your grade is D")

        else:
            print("Your grade is F")


    else:
        print("Invalid sub - menu choice.")
