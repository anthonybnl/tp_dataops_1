import os
import time
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv("./.env")
load_dotenv("/data/.env.kestra")

JSON_OUTPUT_PATH = os.environ["JSON_OUTPUT_PATH"]

API_URL = os.environ.get("API_URL", "https://randomuser.me/api/")


def is_api_available():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        print(response.status_code)
        if response.status_code == 200:
            return (True, response.json())
        return (False, None)
    except Exception as e:  # noqa
        print(f"Erreur: {e}")
        return (False, None)


def sensor(poke, poke_interval: float = 5, timeout: float = 60) -> Any:
    deadline = time.monotonic() + timeout
    while True:
        (ok, data) = is_api_available()
        if ok:
            return data
        if time.monotonic() + poke_interval > deadline:
            raise TimeoutError(f"Sensor timeout après {timeout}s")
        print(f"Attente de {poke_interval}s avant la prochaine tentative...")
        time.sleep(poke_interval)


def handle_data(data: dict):
    # on écrit le fichier JSON sur le disque
    import json

    with open(JSON_OUTPUT_PATH, "w") as f:
        json.dump(data, f)
    print(f"Données reçues: {data}")
    print()
    print(f"Fichier JSON écrit sur {JSON_OUTPUT_PATH}")


def main():
    fake_user = sensor(is_api_available, poke_interval=5, timeout=60)
    handle_data(fake_user)


if __name__ == "__main__":
    main()
