from config import DATA_FOLDER
from core.storage import Storage


def main():
    storage = Storage(DATA_FOLDER)

    storage.save(
        "status.json",
        {
            "project": "Lux Finder",
            "version": "0.1.0",
            "status": "running"
        }
    )

    print("Lux Finder started")


if __name__ == "__main__":
    main()
