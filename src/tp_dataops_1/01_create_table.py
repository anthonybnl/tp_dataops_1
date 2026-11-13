from contextlib import closing

from db import make_connection
from dotenv import load_dotenv

load_dotenv("./.env")
load_dotenv("/data/.env.kestra")


def create_users_table(connection):

    sql_request = """
  CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(255),
    lastname VARCHAR(255),
    email VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );
  """

    with connection.cursor() as cursor:
        cursor.execute(sql_request)
    connection.commit()

    print("La table users a été créée.")


def main():
    with closing(make_connection()) as connection:
        create_users_table(connection)


if __name__ == "__main__":
    main()
