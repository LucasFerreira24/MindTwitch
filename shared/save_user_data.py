import json
import os


def save_user_data(file_path, user: str = 'UserUndefined', points: int = 0):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []

        new_entry = {"user": user, "points": points}
        data.append(new_entry)

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
