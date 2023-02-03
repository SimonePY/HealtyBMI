import datetime
import os
import sqlite3


def bmi(weight: float, height: float) -> float:
    return round(weight / (height / 100) ** 2)


def create() -> None:
    if not os.path.exists("result.db"):
        with sqlite3.connect("result.db") as database:
            cursor = database.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS bmiResult (datetime TEXT, name TEXT, weight REAL, height REAL, bmi REAL)")
            database.commit()


def save(name: str, weight: float, height: float, formula: float) -> None:
    with sqlite3.connect("result.db") as database:
        cursor = database.cursor()
        today = datetime.datetime.today().strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO bmiResult VALUES (?,?,?,?,?)", (today, name, weight, height, formula))
        database.commit()


def run_bmi_calculator() -> None:
    name = input("What is your name? ")
    weight = float(input("What is your weight in kilograms? "))
    height = float(input("What is your height in centimeters? "))

    bmi_value = bmi(weight, height)
    print(f"{name} your BMI is: {bmi_value}")

    if input("Do you want to save the result? (y/n) ").lower() == "y":
        save(name, weight, height, bmi_value)
        print("Data has been saved.")
    else:
        print("Data has not been saved.")


print("Welcome to TheBMI!")
create()
run_bmi_calculator()
