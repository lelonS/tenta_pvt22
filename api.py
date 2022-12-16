import requests

API_URL = "http://api.nobelprize.org/2.1/nobelPrizes"


def get_nobel_prize(year: int, field: str | None = None) -> dict:
    """Get nobel prize data from API

    Args:
        year (int): The year. If below 1901 1901 is used by the api.
        field (str | None, optional): The field. If None only year is used. Defaults to None.

    Returns:
        dict: Dictionary with data from API
    """
    if field is None:
        parameters = {"nobelPrizeYear": year}
    else:
        parameters = {"nobelPrizeYear": year, "nobelPrizeCategory": field}
    res = requests.get(API_URL, params=parameters).json()
    return res


def calculate_prize_amount(prize_amount: int, portion_str: str) -> float:
    """Calculate prize amount based on portion

    Args:
        prize_amount (int): The total prize amount
        portion_str (str): The portion string. ex: "1/2"

    Returns:
        float: The prize amount for that portion
    """
    portion = portion_str.split("/")
    if len(portion) == 1:
        return float(prize_amount)
    else:
        return float(prize_amount) * float(portion[0]) / float(portion[1])


def print_laureate(laureate: dict, prize_amount: int, prize_adjusted: int):
    """Print laureate data

    Args:
        laureate (dict): Laureate data
        prize_amount (int): Prize amount
        prize_adjusted (int): Prize amount adjusted for inflation
    """
    # Check if laureate has a known name
    if "knownName" in laureate:
        print(laureate["knownName"]["en"])
    else:
        print("Unknown name")
    print(laureate['motivation']['en'])

    # Print prize money
    portion = laureate['portion']
    prize_money = calculate_prize_amount(prize_amount, portion)
    prize_money_adjusted = calculate_prize_amount(prize_adjusted, portion)
    print(f"They got {prize_money:0.3f} SEK which is {prize_money_adjusted:0.3f} SEK in today's money")


def print_award(award: dict):
    """Print award data

    Args:
        award (dict): Award data
    """
    print("="*80)
    prize_amount = award["prizeAmount"]
    prize_adjusted = award["prizeAmountAdjusted"]
    print(f"{award['categoryFullName']['se']} prissumma {prize_amount} SEK")

    for laureate in award["laureates"]:
        print("-"*80)
        print_laureate(laureate, prize_amount, prize_adjusted)

    print("-"*80)
