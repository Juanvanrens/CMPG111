temp = int(input("Enter a temperature (in Celsius): "))

if temp <0:
    print("The temperature is Freezing Cold")

elif 0 <= temp <= 10:
    print("The temperature is Cold")

elif 11 <= temp <= 20:
    print("The temperature is Cool")

elif 21 <= temp <= 30:
    print("The temperature is Warm")

else:
    print("The temperature is Scorching")

