def currency_exchange(original: str, target: str, quantity: float):
    """
    Function that changes the currency and tells you how much you will need to play in the original currency
    :param original: The original currency
    :param taarget: The currency you want to obtain
    :param quantity: The quantity of money in the target currency
    :return:
    """

    # Currencies available.
    currencies = ('EUR: (Euro)', 'YEN: (Yen)', 'USD: (US Dollar) ', 'GBP: (great Britain Pound) ')
    # Exchange rates (Date: 04-11-2021)
    rates = {('EUR', 'YEN'): 131.41,
             ('Yen', 'EUR'): 0.0076,
             ('EUR', 'USD'): 1.16,
             ('USD', 'EUR'): 0.87,
             ('EUR', 'GBP'): 0.86,
             ('GBP', 'EUR'): 1.17,
             ('USD', 'YEN'): 113.74,
             ('YEN', 'USD'): 0.0088,
             ('YEN', 'GBP'): 0.0065,
             ('GBP', 'YEN'): 153.57,
             ('USD', 'GBP'): 0.74,
             ('GBP', 'USD'): 1.35
             }

    if target == original:
        return round(quantity, 2)
    else:
        return round(rates[(original, target)] * quantity, 2)


currencies = ('EUR: (Euro)', 'YEN: (Yen)', 'USD: (US Dollar) ', 'GBP: (great Britain Pound) ')
print('these are the available currencies and their respective rates:')
for i in currencies:
    print(i)

original = input("Introduce the original currency: ").upper()
target = input('Introduce the target currency:  ').upper()
quantity = float(input('How much money do you want to change: '))
result = currency_exchange(original, target, quantity)
print(result)
