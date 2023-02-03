import sqlite3
from typing import Union, List, Dict, Any


def retrieve() -> Union[str, List[Dict[str, Any]]]:
    try:
        with sqlite3.connect("result.db") as database:
            cursor = database.cursor()
            cursor.execute("SELECT * FROM bmiResult")
            columns = [column[0] for column in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return "No Data." if not results else results
    except sqlite3.OperationalError:
        return "Error: database file not found."


def print_results(results: List[Dict[str, Any]]) -> None:
    for result in results:
        print(f"Name : {result['name']}")
        print(f"Date: {result['datetime']}")
        print(f"Weight: {result['weight']}")
        print(f"Height: {result['height']}")
        print(f"BMI: {result['bmi']}")
        print("------------------------")


results = retrieve()
if isinstance(results, str):
    print(results)
else:
    print_results(results)
