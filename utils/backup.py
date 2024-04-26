import pickle
from pathlib import Path

from classes import AddressBook


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        path = Path(filename)
        if path.is_file():
            with open(filename, "rb") as f:
                return pickle.load(f)
        else:
            return AddressBook()
    except FileNotFoundError:
        return AddressBook()
