import requests


def get_nobel_prize(year: int, field: str | None = None) -> dict:
    if field is None:
        parameters = {"nobelPrizeYear": year}
    else:
        parameters = {"nobelPrizeYear": year, "nobelPrizeCategory": field}
    res = requests.get(
        "http://api.nobelprize.org/2.1/nobelPrizes", params=parameters).json()
    return res


def print_award(award: dict):
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
