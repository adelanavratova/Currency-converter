import requests
import datetime
from forex_python.converter import CurrencyRates

def communication():
    while True:
        amount = input("Enter amount of the currency: ")
        try:
            amount = float(amount)
            break
        except ValueError:
            print("This input unfortunately is not a number.")

    from_currency = input("Enter the base currency: ").upper()

    with open("list_of_currencies.txt", "r") as lst_currencies:
        content = lst_currencies.read().split()

        if(from_currency not in content):
            from_currency = check_input(from_currency, content, "base")

        to_currency = input("Enter the target currency: ").upper()
        
        if(to_currency not in content):
            to_currency = check_input(to_currency, content, "target")
    
    return amount, from_currency, to_currency


def transfet_offline():
    amount, from_currency, to_currency = communication()

    with open("last_rates.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            parts = line.strip().split(':')
            currency_code = parts[0].strip()

            if currency_code == from_currency:
                rate_from = float(parts[1].strip())

            if currency_code == to_currency:
                rate_to = float(parts[1].strip())
    
    result = (rate_to / rate_from) * amount
    print(f"{amount} {from_currency} = {result} {to_currency}")


def currency_converter(amount, from_currency, to_currency):
    currency = CurrencyRates()
    converted_amount = currency.convert(from_currency, to_currency, amount)
    
    return converted_amount


def clue_amount(word, content):
    clue = set()

    for i in range(len(word), 0, -1):
        new_word = word[:i]

        for prvek in content:
            if new_word in prvek:
                clue.add(prvek)

        if clue:
            break

    return clue


def check_input(my_input, content, txt):
    while my_input not in content:
        print("This currency code does not exist. Did you perhaps mean something from this list?")
        clue = clue_amount(my_input, content)
        print(sorted(clue))
        my_input = input("Enter the " + txt + " currency: ").upper()
    
    return my_input


def transfer():
    amount, from_currency, to_currency = communication()

    converted_amount = currency_converter(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {converted_amount} {to_currency}")


def put_offline_rates():
    current_date = datetime.date.today()
    date_string = current_date.strftime("%Y-%m-%d")
    rates = CurrencyRates().get_rates('USD')

    with open("last_rates.txt", 'w') as f:
        f.write(date_string + "\n")
        f.write("USD : 1\n")

        for currency, rates in rates.items():
            f.write(str(currency) + " : " + str(rates) + "\n")


def is_not_connection():
    print("Unfortunately, your device is not connected to the internet, ")
    print("so it's not possible to access the current currency exchange rates.")
    print("However, it is possible to convert the currency using the exchange rate from: ")
    
    with open("last_rates.txt", 'r') as f:
        line = f.readline()
    
    print(line)
    print("Please type Y to confirm currency conversion using the exchange rate from that date,")
    print(" or N to decline.")
    
    answer = input().upper().strip()
    while answer != 'Y' and answer != 'N':
        print("We are unable to recognize this character.")
        print("Please enter the character again: ")
        answer = input().upper().strip()
        
    if answer == 'Y':
        transfet_offline()
        return

    print("Conversion requires an internet connection, unfortunately,")
    print(" we are currently unable to provide that.")


def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False


def main():
    print("Welcome to the currency converter.")
    print("------------------------------------")

    if(not check_internet_connection()):
        is_not_connection()
        return
    
    put_offline_rates()
    transfer()

if __name__ == "__main__":
    main()