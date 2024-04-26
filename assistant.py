from handlers import (
    parse_input,
    add_contact,
    change_contact,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
)
from utils.backup import save_data
from colorama import Fore, Style


def colored_print(*args):
    print(Fore.YELLOW, *args, Fore.RESET, sep="")


def run_assistant(book):
    print("Welcome to the assistant bot!")
    while True:
        user_input = input(f"{Fore.GREEN}Enter a command: {Fore.RESET}")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            if book:
                save_data(book)
            colored_print("Good bye!")
            break
        elif command == "hello":
            colored_print("How can I help you?")
        elif command == "add":
            colored_print(add_contact(args, book))
        elif command == "change":
            colored_print(change_contact(args, book))
        elif command == "phone":
            colored_print(show_phone(args, book))
        elif command == "all":
            colored_print(show_all(book))
        elif command == "add-birthday":
            colored_print(add_birthday(args, book))
        elif command == "show-birthday":
            colored_print(show_birthday(args, book))
        elif command == "birthdays":
            colored_print(birthdays(book))
        else:
            colored_print("Invalid command.")
