import json
import requests
import time


def get():
    for i in range(9, 12):
        url = f"https://1platefood.com/portal/resources?page={i}&sort=last_verified_at&availability=Available"
        resp = requests.get(url)
        time.sleep(resp.elapsed.total_seconds())

        with open("resources.json", "w") as file:
            json.dump(json.loads(resp.text)["data"], file, indent=4)
