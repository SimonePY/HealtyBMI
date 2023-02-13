import datetime as dt
import sqlite3 as sql
from typing import Union, List, Dict, Any


def create_bmi_result_table(db_file: str) -> None:
    with sql.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS bmiResult (datetime TEXT, name TEXT, weight REAL, height REAL, bmi REAL)")
        conn.commit()


def insert_bmi_result(db_file: str, name: str, weight: float, height: float, bmi: float) -> None:
    with sql.connect(db_file) as conn:
        cursor = conn.cursor()
        today = dt.datetime.today().strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO bmiResult VALUES (?,?,?,?,?)", (today, name, weight, height, bmi))
        conn.commit()


def retrieve_bmi_results(db_file: str) -> Union[str, List[Dict[str, Any]]]:
    with sql.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bmiResult")
        columns = [column[0] for column in cursor.description]
        results = cursor.fetchall()
        if results:
            return [dict(zip(columns, row)) for row in results]
        else:
            return "No Data."
