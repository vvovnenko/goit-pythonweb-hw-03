import json
from datetime import datetime


class Storage:
    def __init__(self, file: str):
        self.file = file

    def get_data(self) -> dict:
        try:
            with open(self.file, "r", encoding="utf-8") as fd:
                return json.loads(fd.read())
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return dict()

    def add_data(self, value: dict):
        data = self.get_data()
        data[str(datetime.now())] = value
        self.save_data(data)

    def save_data(self, data: dict):
        with open(self.file, "w", encoding="utf-8") as fd:
            fd.write(json.dumps(data, indent=4))
