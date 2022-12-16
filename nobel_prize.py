import api

FIELD_CATEGORIES = {"fysik": "phy",
                    "kemi": "che",
                    "litteratur": "lit",
                    "ekonomi": "eco",
                    "fred": "pea",
                    "medicin": "med"}


def print_help():
    """Prints help text on how to use the program
    """
    print("Ange ett år och fält eller 'q' för att avsluta")
    print(f"Fält att välja på: {', '.join(FIELD_CATEGORIES.keys())}")
    print("Exempel: 1965 fysik")


def handle_input_search(user_input: str):
    """Handles user input for searching for a Nobel prize
    and prints the result

    Args:
        user_input (str): The user input
    """
    input_words = user_input.split()

    # Get year and field
    if len(input_words) == 2:
        year = input_words[0]
        field = input_words[1].lower()
        if field not in FIELD_CATEGORIES:
            print("Felaktigt område")
            return
    elif len(input_words) == 1:
        year = input_words[0]
        field = ""
    else:
        print("Felaktigt antal ord")
        return

    # Check if year is an int
    try:
        year = int(year)
    except ValueError:
        print("Felaktigt år")
        return

    # Get data from API and print it
    res = api.get_nobel_prize(year, FIELD_CATEGORIES.get(field, None))
    for award in res["nobelPrizes"]:
        api.print_award(award)


def main():
    print_help()
    while True:

        user_input = input(">")

        if user_input.lower() == "q":
            break
        elif user_input.lower() == "h":
            print_help()
        else:
            handle_input_search(user_input)


if __name__ == '__main__':
    main()
