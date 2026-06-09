weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in centimeters (cm): "))

meters = height/100

bmi = weight/(meters**2)
print(f"BMI: {bmi:.3f}")