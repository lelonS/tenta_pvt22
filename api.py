import requests


def get_nobel_prize(year: int, field: str | None = None) -> dict:
    if field is None:
        parameters = {"nobelPrizeYear": year}
    else:
        parameters = {"nobelPrizeYear": year, "nobelPrizeCategory": field}
    res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=parameters).json()
    return res


def calculate_prize_amount(prize_amount: int, portion_str: str) -> float:
    portion = portion_str.split("/")
    if len(portion) == 1:
        return float(prize_amount)
    else:
        return float(prize_amount) * float(portion[0]) / float(portion[1])


def print_laureate(laureate: dict, prize_amount: int, prize_adjusted: int):
    print(laureate['knownName']['en'])
    print(laureate['motivation']['en'])
    portion = laureate['portion']
    prize_money = calculate_prize_amount(prize_amount, portion)
    prize_money_adjusted = calculate_prize_amount(prize_adjusted, portion)
    print(f"They got {prize_money:0.3f} SEK which is {prize_money_adjusted:0.3f} SEK in today's money")


def print_award(award: dict):
    prize_amount = award["prizeAmount"]
    prize_adjusted = award["prizeAmountAdjusted"]
    print(
        f"{award['categoryFullName']['se']} prissumma {prize_amount} SEK")

    for laureate in award["laureates"]:
        print("-"*80)
        print_laureate(laureate, prize_amount, prize_adjusted)

    print("-"*80)
