WATER_PER_DAY = 15
num_days = 0

def getValidNumber():
    num_days = int(input("Enter the number of days: "))

    while num_days <= 0 or num_days > 12 or type(num_days) != int:
        print("Invalid input, please enter a positive number not exceeding 12")
        num_days = int(input("Enter the number of days: "))





    return num_days

def warnHighUsage(num_days, high_count):


    if high_count == 0:
        print(f"Well done. Your water usage during the {num_days} days did not exceed the limit of {WATER_PER_DAY} litres per day.")

    elif 1 <= high_count <= 3:
        print(f"Your water usage has been too high for {high_count} out of the {num_days} days. Please reduce your water usage.")

    else:
        print(f"Warning: Your water usage has been too high for {high_count} out of the {num_days} days. Your water supply will be terminated if not reduced.")

    return high_count


def showSummary(num_days, total_used, avg_used, high_count):
    print("--- Water Usage Summary ---")
    print(f"Number of days tracked: {num_days}")
    print(f"Total water usage: {total_used}")
    print(f"Average water usage: {avg_used}")
    print(f"Days exceeding allowed usage: {high_count}")



def main():
    num_days = getValidNumber()
    total_used = 0
    high_count = 0
    for i in range(num_days):
        water_used = int(input(f"Enter the water usage for day {i + 1}:"))
        total_used += water_used

        if water_used > WATER_PER_DAY:
            high_count += 1

    avg_used = total_used / num_days
    showSummary(num_days, total_used, avg_used, high_count)
    warnHighUsage(num_days,high_count)

    return avg_used, total_used

if __name__ == "__main__":
    main()