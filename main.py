from assistant import run_assistant
from utils.backup import load_data


def main():
    book = load_data()

    run_assistant(book)


if __name__ == "__main__":
    main()
