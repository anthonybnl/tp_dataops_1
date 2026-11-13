import os
from contextlib import closing

from db import make_connection
from dotenv import load_dotenv

load_dotenv("./.env")
load_dotenv("/data/.env.kestra")

JSON_OUTPUT_PATH = os.environ["JSON_OUTPUT_PATH"]


def main():
    import json

    with open(JSON_OUTPUT_PATH, "r") as f:
        data = json.load(f)
    print(f"Données lues depuis {JSON_OUTPUT_PATH}: {data}")

    with closing(make_connection()) as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO users (firstname, lastname, email)
            VALUES (%s, %s, %s)
            ON CONFLICT (id) DO NOTHING
            """,
            (
                # data["results"][0]["login"]["uuid"],
                data["results"][0]["name"]["first"],
                data["results"][0]["name"]["last"],
                data["results"][0]["email"],
            ),
        )
        connection.commit()


if __name__ == "__main__":
    main()
