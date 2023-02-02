def bmi_calculator(weight: float, height: float) -> float:
    imc = weight / (height / 100) ** 2
    return round(imc)


print("Welcome to TheBMI!")
try:
    weight = float(input("What is your weight in kilograms? "))
    height = float(input("What is your height in centimeters? "))
except ValueError:
    print("Error: only numbers are accepted.")
try:
    print(f"Your IMC is: {bmi_calculator(weight, height)}")
except ZeroDivisionError:
    print("You can't divide for zero.")
