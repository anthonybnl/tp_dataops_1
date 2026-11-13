import os
from urllib.parse import urlparse

import psycopg2
from dotenv import load_dotenv

load_dotenv("./.env")
load_dotenv("/data/.env.kestra")


def make_connection():
    conStr = os.environ["DATABASE_URL"]
    p = urlparse(conStr)

    pg_connection_dict = {
        "dbname": p.path[1:],
        "user": p.username,
        "password": p.password,
        "port": p.port,
        "host": p.hostname,
    }

    # `with conn` commit/rollback seulement, closing() ferme la connexion
    connection = psycopg2.connect(**pg_connection_dict)
    return connection
