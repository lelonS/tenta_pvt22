import api


def print_help():
    """Prints help text on how to use the program
    """
    print("(Ange 'q' för att avsluta och 'h' för hjälp)")
    print("Ange ett år och fält för att få priset för det fältet för det året")
    print("Ange endast år för att få alla priser för det året")
    print(f"Fält att välja på: {', '.join(api.FIELD_CATEGORIES.keys())}")
    print("Exempel: '1965 fysik' eller '1965'")


def print_search(year: int, field: str):
    """Searches and prints the result using the API

    Args:
        year (int): The year
        field (str): The field (long name)
    """
    res = api.get_nobel_prize(year, api.FIELD_CATEGORIES.get(field, None))
    for award in res["nobelPrizes"]:
        api.print_award(award)


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
        if field not in api.FIELD_CATEGORIES:
            print(f"Fältet '{field}' kunde inte hittas")
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
        print("Felaktigt år (måste vara ett heltal)")
        return

    # Get data from API and print it
    print_search(year, field)


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
