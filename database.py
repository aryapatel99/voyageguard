import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE


def get_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )


def save_trip_evaluation(data):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO trip_evaluations 
        (destination, travel_date, budget, weather_risk, advisory_risk, budget_risk, final_score, risk_level, explanation)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data["destination"],
        data["travel_date"],
        data["budget"],
        data["weather_risk"],
        data["advisory_risk"],
        data["budget_risk"],
        data["final_score"],
        data["risk_level"],
        data["explanation"]
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()
