
# BMI Calculator using Class and Object

class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def show_result(self):
        bmi = self.calculate_bmi()
        print(f"Your BMI is: {bmi:.2f}")


def main():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in metres: "))

    # Create an object
    person = BMI(weight, height)

    # Call the function
    person.show_result()


if __name__ == "__main__":
    main()