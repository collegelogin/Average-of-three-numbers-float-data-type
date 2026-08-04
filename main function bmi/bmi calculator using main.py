
def bmi(weight, height): #defining the function bmi that takes weight and height as parameters
    return weight / (height ** 2) #return the bmi value by dividing weight by height squared
if __name__ == "__main__": #main function that runs when the script is executed

 weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
print("Your BMI is: ", bmi(weight, height)) #print the bmi value by calling the bmi function with weight and height as arguments
