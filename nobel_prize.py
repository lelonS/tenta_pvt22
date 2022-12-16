import requests

# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur apiet fungerar
# vi använder oss enbart av /nobelPrizes
# Dokumentation, hjälp samt verktyg för att testa apiet fins här: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1


FIELD_CATEGORIES = {"fysik": "phy",
                    "kemi": "che",
                    "litteratur": "lit",
                    "ekonomi": "eco",
                    "fred": "pea",
                    "medicin": "med"}


# TODO 10p programmet skall ge en hjälpsam utskrift istället för en krasch om användaren skriver in fel input
# TODO 15p om användaren inte anger ett område som exempelvis fysik eller kemi så skall den parametern inte skickas med till apiet och vi får då alla priser det året

def print_help():
    print("Ange ett år och fält eller 'q' för att avsluta")
    print(f"Fält att välja på: {', '.join(FIELD_CATEGORIES.keys())}")
    print("Exempel: 1965 fysik")


def main():
    print_help()
    while True:

        user_input = input(">")

        if user_input.lower() == "q":
            break
        elif user_input.lower() == "h":
            print_help()

        else:

            year, field_swe = user_input.split()

            parameters = {"nobelPrizeYear": int(
                year), "nobelPrizeCategory": FIELD_CATEGORIES[field_swe]}

            res = requests.get(
                "http://api.nobelprize.org/2.1/nobelPrizes", params=parameters).json()
            # TODO 5p  Lägg till någon typ av avskiljare mellan pristagare, exempelvis --------------------------

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
                    print(laureate['knownName']['en'])
                    print(laureate['motivation']['en'])
                    portion = laureate['portion']


if __name__ == '__main__':
    main()
