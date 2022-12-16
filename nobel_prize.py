import requests
import api
# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur apiet fungerar
# vi använder oss enbart av /nobelPrizes
# Dokumentation, hjälp samt verktyg för att testa apiet fins här: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1


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


def handle_user_input(user_input):
    input_words = user_input.split()

    if len(input_words) == 2:
        year = input_words[0]
        field = input_words[1]
    elif len(input_words) == 1:
        year = input_words[0]
        field = ""
    else:
        print("Felaktigt antal ord")

    res = api.get_nobel_prize(int(year), FIELD_CATEGORIES.get(field, None))

    # TODO 20p Skriv ut hur mycket pengar varje pristagare fick, tänk på att en del priser delas mellan flera mottagare, skriv ut både i dåtidens pengar och dagens värde
    #   Skriv ut med tre decimalers precision. exempel 534515.123
    #   Skapa en funktion som hanterar uträkningen av prispengar och skapa minst ett enhetestest för den funktionen
    #   Tips, titta på variabeln andel
    # Feynman fick exempelvis 1/3 av priset i fysik 1965, vilket borde gett ungefär 282000/3 kronor i dåtidens penningvärde

    for award in res["nobelPrizes"]:
        prize_amount = award["prizeAmount"]
        prize_adjusted = award["prizeAmountAdjusted"]
        print(
            f"{award['categoryFullName']['se']} prissumma {prize_amount} SEK")

        for laureate in award["laureates"]:
            print("-"*80)
            print(laureate['knownName']['en'])
            print(laureate['motivation']['en'])
            portion = laureate['portion']
        print("-"*80)


def main():
    print_help()
    while True:

        user_input = input(">")

        if user_input.lower() == "q":
            break
        elif user_input.lower() == "h":
            print_help()
        else:
            handle_user_input(user_input)


if __name__ == '__main__':
    main()
