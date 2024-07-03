import json
import time


def create_json(name: str, estimate: str) -> None:
    data = {"companies": [{"name": name, "estimate": estimate}]}

    time_file = time.strftime('%H-%M-%S')

    with open(f"app/static/data{time_file}.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return time_file
