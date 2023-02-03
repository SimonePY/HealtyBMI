import sqlite3


def retrieve() -> str:
    try:
        with sqlite3.connect("result.db") as database:
            cursor = database.cursor()
            cursor.execute("SELECT * FROM bmiResult")
            columns = [column[0] for column in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            if not results:
                return "No Data."
            else:
                return results
    except sqlite3.OperationalError:
        return "Error: database file not found."


def print_results(results) -> str:
    for result in results:
        print(f"Date: {result['datetime']}")
        print(f"Weight: {result['weight']}")
        print(f"Height: {result['height']}")
        print(f"BMI: {result['bmi']}")
        print("------------------------")


results = retrieve()
if results == "No Data.":
    print(results)
else:
    print_results(results)
