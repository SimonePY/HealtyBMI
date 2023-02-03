import datetime
import sqlite3


def bmi(weight: float, height: float) -> float:
    formula = weight / (height / 100) ** 2
    return round(formula)


def save(weight: float, height: float, formula: float):
    database = sqlite3.connect("result.db")
    cursor = database.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS bmiResult (datetime DATE, weight FLOAT, height FLOAT, bmi FLOAT)")
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO bmiResult VALUES (?,?,?,?)", (today, weight, height, formula))
    database.commit()
    cursor.close()
    database.close()


print("Welcome to TheBMI!")

weight_input = input("What is your weight in kilograms? ")
height_input = input("What is your height in centimeters? ")

try:
    weight = float(weight_input)
    height = float(height_input)
except ValueError:
    print("Error: only numbers are accepted.")
    exit()

try:
    bmi_value = bmi(weight, height)
    print(f"Your BMI is: {bmi_value}")
    save_input = input("Do you want to save the result? (y/n) ").lower()
    if save_input == "y":
        save(weight, height, bmi_value)
        print("Data has been saved.")
    else:
        print("Data has not been saved.")
except ZeroDivisionError:
    print("You can't divide by zero.")
