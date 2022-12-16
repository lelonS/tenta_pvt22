import api

FIELD_CATEGORIES = {"fysik": "phy",
                    "kemi": "che",
                    "litteratur": "lit",
                    "ekonomi": "eco",
                    "fred": "pea",
                    "medicin": "med"}


def print_help():
    print("Ange ett år och fält eller 'q' för att avsluta")
    print(f"Fält att välja på: {', '.join(FIELD_CATEGORIES.keys())}")
    print("Exempel: 1965 fysik")


def handle_input_search(user_input):
    input_words = user_input.split()

    if len(input_words) == 2:
        year = input_words[0]
        field = input_words[1]
    elif len(input_words) == 1:
        year = input_words[0]
        field = ""
    else:
        print("Felaktigt antal ord")

    try:
        year = int(year)
    except ValueError:
        print("Felaktigt år")
        return

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
