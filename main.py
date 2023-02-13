import argparse as ap
from typing import List, Dict, Any

import databaseHandler as dH


def bmi(weight: float, height: float) -> float:
    return round(weight / (height / 100) ** 2)


def print_results(results: List[Dict[str, Any]]) -> None:
    for result in results:
        print(f"Name : {result['name']}")
        print(f"Date: {result['datetime']}")
        print(f"Weight: {result['weight']}")
        print(f"Height: {result['height']}")
        print(f"BMI: {result['bmi']}")
        print("------------------------")


def run_bmi_calculator(name: str, weight: float, height: float, save_result: bool) -> None:
    bmi_value = bmi(weight, height)
    print(f"{name} your BMI is: {bmi_value}")

    if save_result:
        dH.insert_bmi_result(db_file="result.db", name=name, weight=weight, height=height, bmi=bmi_value)
        print("Data has been saved.")
    else:
        print("Data has not been saved.")


pr = ap.ArgumentParser(prog="HealthyBMI", description="Calculate your BMI and store it easily!")

pr.add_argument("-N", "--name", type=str, required=False, help="Your name.")
pr.add_argument("-W", "--weight", type=float, required=False, help="Your weight in kilograms.")
pr.add_argument("-H", "--height", type=float, required=False, help="Your height in centimeters.")
pr.add_argument("-S", "--save", action="store_true", required=False, help="Save the result to the database.")
pr.add_argument("-R", "--retrieve", action="store_true", required=False,
                    help="Retrieve and print results from the database.")

args = pr.parse_args()

if args.retrieve:
    dH.create_bmi_result_table(db_file="result.db")
    all_results = dH.retrieve_bmi_results(db_file="result.db")
    if type(all_results) is list:
        print_results(all_results)
    else:
        print(all_results)
elif args.name and args.weight and args.height:
    dH.create_bmi_result_table(db_file="result.db")
    run_bmi_calculator(args.name, args.weight, args.height, args.save)
else:
    pr.print_help()
