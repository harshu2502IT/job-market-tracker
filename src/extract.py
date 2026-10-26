import json
import os
from datetime import date

import requests

API_URL = "https://remotive.com/api/remote-jobs"


def fetch_jobs(search):
    response = requests.get(API_URL, params={"search": search}, timeout=30)
    response.raise_for_status()
    return response.json()


def save_raw(data, search):
    folder = os.path.join("data", "raw", str(date.today()))
    os.makedirs(folder, exist_ok=True)
    filename = search.replace(" ", "_") + ".json"
    path = os.path.join(folder, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return path


if __name__ == "__main__":
    search = "data engineer"
    data = fetch_jobs(search)
    path = save_raw(data, search)
    print("Saved", len(data["jobs"]), "jobs to", path)
    print("Legal notice:", data.get("0-legal-notice"))
