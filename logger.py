import json

def save_logs(logs, filename="logs.json"):
    with open(filename, "w") as f:
        json.dump(logs, f, indent=2)
