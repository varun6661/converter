amount = float(input("Enter the amount: "))
currency_from = input("Enter the currency to convert from: ")
currency_to = input("Enter the currency to convert to: ")

rates = {
    'AUDUSD': 0.8371,
    'CADUSD': 0.8711,
    'USDCNY': 6.1715,
    'EURUSD': 1.2315,
    'GBPUSD': 1.5683,
    'NZDUSD': 0.7750,
    'USDJPY': 119.95,
    'EURCZK': 27.6028,
    'EURDKK': 7.4405,
    'EURNOK': 8.6651
}

if currency_from == currency_to:
    for currency in rates:
        if currency_from in currency:
            rate = 1.0
            print(f"{currency_from} {amount:.2f} = {currency_to} {amount:.2f}")
            break
    else:
        print(f"Unable to find rate for {currency_from}/{currency_to}")
elif f"{currency_from}{currency_to}" in rates:
    rate = rates[f"{currency_from}{currency_to}"]
    result = amount * rate
    print(f"{currency_from} {amount:.2f} = {currency_to} {result:.2f}")
elif f"{currency_to}{currency_from}" in rates:
    rate = 1 / rates[f"{currency_to}{currency_from}"]
    result = amount * rate
    print(f"{currency_from} {amount:.2f} = {currency_to} {result:.2f}")
else:
    cross_currency = None
    for currency in rates:
        if currency_from in currency:
            cross_currency = currency.replace(currency_from, '').replace(currency_to, '')
            break
        elif currency_to in currency:
            cross_currency = currency.replace(currency_to, '').replace(currency_from, '')
            break
    if cross_currency:
        if f"{currency_from}{cross_currency}" in rates and f"{cross_currency}{currency_to}" in rates:
            rate = rates[f"{cross_currency}{currency_to}"] * rates[f"{currency_from}{cross_currency}"]
            result = amount * rate
            print(f"{currency_from} {amount:.2f} = {currency_to} {result:.2f}")
        elif f"{cross_currency}{currency_from}" in rates and f"{currency_to}{cross_currency}" in rates:
            rate = 1 / (rates[f"{cross_currency}{currency_from}"] * rates[f"{currency_to}{cross_currency}"])
            result = amount * rate
            print(f"{currency_from} {amount:.2f} = {currency_to} {result:.2f}")
        else:
            print(f"Unable to find rate for {currency_from}/{currency_to}")
    else:
        print(f"Unable to find rate for {currency_from}/{currency_to}")