import json
import os


class Storage:

    def __init__(self, folder):
        self.folder = folder
        os.makedirs(folder, exist_ok=True)

    def save(self, filename, data):
        path = os.path.join(self.folder, filename)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=2
            )
