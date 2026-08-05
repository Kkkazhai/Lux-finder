from config import DATA_FOLDER
from core.storage import Storage


def main():
    storage = Storage(DATA_FOLDER)

    storage.save(
        "status.json",
        {
            "status": "ok"
        }
    )

    print("Lux Finder started")


if __name__ == "__main__":
    main()
