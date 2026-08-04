#simple bmi calculator that input height and weight from the user

    
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")